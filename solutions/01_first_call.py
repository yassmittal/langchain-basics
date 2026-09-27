from config import get_llm
from langchain_core.messages import HumanMessage


def main():
    llm = get_llm()

    response = llm.invoke([HumanMessage("What is LangChain in one sentence?")])

    print(response.content)


if __name__ == "__main__":
    main()
