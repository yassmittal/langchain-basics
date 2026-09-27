import os

from config import get_llm
from langchain_aws import BedrockEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

document = """
LangChain is a framework for building applications powered by language models.
It provides abstractions for prompts, chains, memory, tools, and retrieval.
LCEL (LangChain Expression Language) lets you compose these pieces with the
`|` operator. Retrieval-Augmented Generation (RAG) combines an LLM with a
search step over your own documents, so answers can be grounded in content
the model was never trained on.
""".strip()


def main():
    llm = get_llm()
    embeddings = BedrockEmbeddings(region_name=os.environ.get("AWS_REGION", "us-east-1"))

    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    chunks = splitter.split_text(document)

    vector_store = InMemoryVectorStore.from_texts(chunks, embeddings)

    question = "What does LCEL let you do?"

    relevant_chunks = vector_store.similarity_search(question, k=2)

    context = "\n".join(doc.page_content for doc in relevant_chunks)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Answer using ONLY the context below. If it's not there, say you "
                "don't know.\n\nContext:\n{context}",
            ),
            ("human", "{question}"),
        ]
    )

    chain = prompt | llm | StrOutputParser()

    result = chain.invoke({"context": context, "question": question})
    print(result)


if __name__ == "__main__":
    main()
