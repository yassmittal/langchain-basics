from config import get_llm
from langchain_core.prompts import ChatPromptTemplate


def main():
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a friendly cooking assistant."),
            ("human", "Suggest a recipe using these ingredients: {ingredients}"),
        ]
    )

    messages = prompt.invoke({"ingredients": "chicken, rice, and bell peppers"})

    response = llm.invoke(messages)
    print(response.content)


if __name__ == "__main__":
    main()
