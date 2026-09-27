"""
Lesson 01 - Your first call to an LLM through LangChain

Goal: understand the two building blocks you'll use in every lesson:
  1. A "chat model" object (LangChain's wrapper around a specific LLM API)
  2. .invoke(...) - the simplest way to send it a message and get a response back

We're using Claude on Amazon Bedrock via `langchain_aws.ChatBedrockConverse`,
already configured for you in config.py (get_llm()).

Run with: python lessons/01_first_call.py
"""

from config import get_llm
from langchain_core.messages import HumanMessage


def main():
    llm = get_llm()

    # TODO 1: Call llm.invoke(...) with a list containing one HumanMessage,
    #         asking any question you like (e.g. "What is LangChain in one sentence?").
    #         Store the result in `response`.
    response = None  # <-- replace this

    # TODO 2: `response` is an AIMessage object, not a plain string.
    #         Print the text of the reply. Hint: it has a `.content` attribute.


if __name__ == "__main__":
    main()
