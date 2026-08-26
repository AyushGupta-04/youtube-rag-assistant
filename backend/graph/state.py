from typing import TypedDict, List, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from langchain_core.documents import Document


class YTChatState(TypedDict, total=False):
    question: str
    context: str
    answer: str
    documents: List[Document]
    messages: Annotated[ List[BaseMessage],add_messages]
    mode: str
    number: int
    difficulty: str
    mcqs: object