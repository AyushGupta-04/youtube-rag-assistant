from langchain_core.messages import AIMessage
from langgraph.graph import StateGraph, START, END

from backend.graph.state import YTChatState
from backend.llm.prompt import prompt


def build_graph(retriever, model, checkpointer):
    graph = StateGraph(YTChatState)
    def retrieve_node(state: YTChatState):
        question = state["question"]
        print(f"Retrieving context for: {question}")

        docs = retriever.invoke(question)
        if not docs:
            context = "No relevant context found."
        else:
            context_parts = []
            for doc in docs:
                source = doc.metadata.get("video_url","Unknown")
                content = doc.page_content
                context_parts.append(f"""
                Source: {source}
                Content: {content}
                """ )
            context = "\n\n".join(context_parts)

        return {
            "documents": docs,
            "context": context
        }

    def generate_node(state: YTChatState):
        print("Generating answer...")

        prompt_value = prompt.invoke({
            "context": state["context"],
            "messages": state.get("messages", []),
        })

        response = model.invoke(prompt_value)
        answer = response.content

        if not isinstance(answer, str):
            answer = str(answer)

        return {
            "answer": answer,
            "messages": [AIMessage(content=answer)]
            }

    graph.add_node("retrieve",retrieve_node)
    graph.add_node("generate",generate_node)
    graph.add_edge(START,"retrieve")
    graph.add_edge("retrieve","generate")
    graph.add_edge("generate",END)

    return graph.compile(checkpointer=checkpointer)