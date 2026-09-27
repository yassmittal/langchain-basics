"""
Lesson 07 - RAG basics (Retrieval-Augmented Generation)

Goal: answer questions using YOUR OWN text instead of relying on the model's
training data. Steps: split text into chunks -> embed each chunk -> store in a
vector store -> retrieve the most relevant chunks for a question -> stuff them
into the prompt as context.

Run with (from the project root): python -m lessons.07_rag_basics
"""

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

    # TODO 1: Split `document` into chunks with RecursiveCharacterTextSplitter.
    #         Create one with chunk_size=200, chunk_overlap=20, then call
    #         .split_text(document) to get a list of chunk strings.
    chunks = []  # <-- replace this

    # TODO 2: Build a vector store from those chunks:
    #         InMemoryVectorStore.from_texts(chunks, embeddings)
    vector_store = None  # <-- replace this

    question = "What does LCEL let you do?"

    # TODO 3: Retrieve the most relevant chunk(s):
    #         vector_store.similarity_search(question, k=2)
    relevant_chunks = []  # <-- replace this

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

    # TODO 4: Build `chain` = prompt | llm | StrOutputParser(), then call
    #         chain.invoke({"context": context, "question": question}) and print it.


if __name__ == "__main__":
    main()
