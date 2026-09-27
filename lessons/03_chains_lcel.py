"""
Lesson 03 - Chains with LCEL (LangChain Expression Language)

Goal: instead of calling prompt.invoke() then llm.invoke() by hand, LangChain
lets you compose steps with the `|` operator into a single runnable "chain".

Run with: python lessons/03_chains_lcel.py
"""

from config import get_llm
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


def main():
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You explain concepts to a total beginner in 2-3 short sentences."),
            ("human", "Explain: {topic}"),
        ]
    )

    # TODO 1: Build `chain` by piping: prompt | llm | StrOutputParser()
    #         StrOutputParser() extracts the plain string from the AIMessage for you,
    #         so the chain's final output is already a str, not a message object.
    chain = None  # <-- replace this

    # TODO 2: Call chain.invoke({"topic": "..."}) with a topic of your choice
    #         and print the result directly (no .content needed this time).


if __name__ == "__main__":
    main()
