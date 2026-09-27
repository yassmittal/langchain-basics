"""
Lesson 01 - Your first call to an LLM through LangChain

Goal: understand the two building blocks you'll use in every lesson:
  1. A "chat model" object (LangChain's wrapper around a specific LLM API)
  2. .invoke(...)  - the simplest way to send it a message and get a response back

"""

from config import get_llm
from langchain_core.messages import HumanMessage

def main():
    llm = get_llm()

    response = llm.invoke([HumanMessage("What is langchain in one sentence?")])

    print("response" , response.content);

if __name__ == "__main__":
    main()