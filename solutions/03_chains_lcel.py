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

    chain = prompt | llm | StrOutputParser()

    result = chain.invoke({"topic": "vector embeddings"})
    print(result)


if __name__ == "__main__":
    main()
