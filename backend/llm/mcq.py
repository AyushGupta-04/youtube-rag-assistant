from typing import List , Literal
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate


class MCQ(BaseModel):
    question: str = Field(description="Multiple choice question")

    option_a: str = Field(description="Option A")
    option_b: str = Field(description="Option B")
    option_c: str = Field(description="Option C")
    option_d: str = Field(description="Option D")

    correct_answer: Literal["A","B","C","D"] = Field(description="The correct answer letter.")
    explanation: str = Field(description="Short explanation of why the answer is correct.")

class MCQResponse(BaseModel):
    questions: List[MCQ] = Field(description="List of generated multiple-choice questions.")

mcq_prompt = ChatPromptTemplate.from_messages(
    [("system",
            """
            You are an educational quiz generator.
            Your task is to generate multiple-choice questions using ONLY the provided YouTube transcript.
            IMPORTANT RULES:
            1. Generate exactly {number} questions.
            2. Use ONLY information explicitly present in the transcript.
            3. Never use outside knowledge.
            4. Never invent information.
            5. Every question must have exactly four options.
            6. The four options must be A, B, C, and D.
            7. Exactly one option must be correct.
            8. correct_answer MUST be exactly one of:
            A
            B
            C
            D
            9. Every question must have a short explanation.
            10. Avoid duplicate questions.
            11. Questions must test understanding of the transcript.
            12. Follow the requested difficulty.
            13. Do not add any information that is not supported by the transcript.
            Difficulty:
            {difficulty}

            Number of questions:
            {number}

            VIDEO CONTEXT:
            {context}
            """) ]
)

def create_mcq_chain(llm):
    structured_llm = llm.with_structured_output(MCQResponse)
    chain = mcq_prompt | structured_llm
    return chain