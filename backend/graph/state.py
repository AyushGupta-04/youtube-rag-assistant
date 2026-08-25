from typing import TypedDict, List, Annotated
from langchain_core.documents import Document
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class Citation(TypedDict):
    source_id: str
    video_url: str
    start_time: float
    end_time: float
    text: str


class YTChatState(TypedDict):
    question: str
    context: str
    answer: str
    documents: list[Document]
    citations: List[Citation]
    messages: Annotated[List[BaseMessage],add_messages]