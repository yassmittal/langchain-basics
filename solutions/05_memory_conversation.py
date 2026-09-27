from config import get_llm
from langchain_core.messages import HumanMessage, SystemMessage


def main():
    llm = get_llm()

    history = [SystemMessage("You are a terse pirate.")]

    questions = [
        "What's the capital of Japan?",
        "What's a popular dish from there?",
    ]

    for question in questions:
        history.append(HumanMessage(question))

        response = llm.invoke(history)

        history.append(response)

        print(f"Q: {question}")
        print(f"A: {response.content}\n")


if __name__ == "__main__":
    main()
