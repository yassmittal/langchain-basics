"""
Lesson 05 - Conversation memory

Goal: an LLM call is stateless by default - it only sees what you send it.
"Memory" in a chat app just means: keep a growing list of messages and resend
the whole list every turn, so the model can refer back to earlier context.

Run with (from the project root): python -m lessons.05_memory_conversation
"""

from config import get_llm
from langchain_core.messages import HumanMessage, SystemMessage


def main():
    llm = get_llm()

    # TODO 1: Create a `history` list starting with one SystemMessage that sets
    #         the assistant's persona (e.g. "You are a terse pirate.").
    history = []  # <-- replace this

    questions = [
        "What's the capital of Japan?",
        "What's a popular dish from there?",  # "there" only makes sense with memory
    ]

    for question in questions:
        # TODO 2: Append a HumanMessage(question) to `history`.

        # TODO 3: Call llm.invoke(history) and store the AIMessage in `response`.
        response = None  # <-- replace this

        # TODO 4: Append `response` itself (not just response.content) to
        #         `history`, so the next loop iteration includes it as context.

        print(f"Q: {question}")
        print(f"A: {response.content if response else '...'}\n")


if __name__ == "__main__":
    main()
