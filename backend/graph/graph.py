from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langgraph.graph import StateGraph,START,END
from backend.llm.mcq import create_mcq_chain
from backend.graph.state import YTChatState

# CHAT PROMPT
chat_prompt = ChatPromptTemplate.from_messages([(
            "system",
            """
            You are an AI assistant that answers questions
            about a YouTube video.

            RULES:
            1. Answer ONLY using the provided video transcript context.
            2. If the answer is not present in the context, reply exactly:
            "The video doesn't mention this"
            3. Be concise, clear and accurate.
            4. Do not invent information.
            5. Maintain conversation history for follow-up questions.
            6. Use previous conversation to understand follow-up questions.
            7. Use video context for factual answers.

            VIDEO CONTEXT:
            {context} 
            """
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)


# BUILD GRAPH
def build_graph(retriever, model,checkpointer):

    chat_chain = chat_prompt| model| StrOutputParser()
    mcq_chain = create_mcq_chain(model)

    graph = StateGraph( YTChatState)

    # RETRIEVE
    def retrieve_node(state: YTChatState):
        query = state.get("question","important topics from the video")

        docs = retriever.invoke(query)
        if not docs:
            context = ("No relevant context found.")

        else:
            context_parts = []
            for doc in docs:
                source = doc.metadata.get("video_url","Unknown")
                content = doc.page_content
                context_parts.append(
                    f"""Source: {source}
                    Content:{content}
                    """
                )

            context = "\n\n".join(context_parts)
        return {
            "documents": docs,
            "context": context
        }

    # CHAT
    def chat_node(state: YTChatState):
        response = chat_chain.invoke(
            {
                "context": state["context"],
                "messages": state.get("messages",[])
            }
        )

        return {
            "answer": response,
            "messages": [AIMessage(content=response)]
        }

    # MCQ
    def mcq_node(state: YTChatState):
        number = state.get("number",5)
        difficulty = state.get("difficulty","Medium")
        result = mcq_chain.invoke(
            {
                "context": state["context"],
                "number": number,
                "difficulty": difficulty
            }
        )
        return { "mcqs": result}

    # ROUTER
    def route_mode(state: YTChatState):
        mode = state.get("mode","chat")
        if mode == "mcq":
            return "mcq"

        return "chat"

    # NODES
    graph.add_node("retrieve",retrieve_node)
    graph.add_node("chat",chat_node)
    graph.add_node("mcq",mcq_node)

    # EDGES
    graph.add_edge(START, "retrieve")
    graph.add_conditional_edges("retrieve",route_mode, {"chat": "chat","mcq": "mcq"})
    graph.add_edge("chat",END)
    graph.add_edge("mcq",END)

    return graph.compile(checkpointer=checkpointer)