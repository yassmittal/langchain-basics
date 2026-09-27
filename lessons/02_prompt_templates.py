"""
Lesson 02 - Prompt templates

Goal: stop hardcoding strings into messages. A ChatPromptTemplate defines a
prompt with placeholders you fill in at call time - the foundation for
reusable, parameterized chains.

Run with: python lessons/02_prompt_templates.py
"""

from config import get_llm
from langchain_core.prompts import ChatPromptTemplate


def main():
    llm = get_llm()

    # TODO 1: Build a ChatPromptTemplate with ChatPromptTemplate.from_messages([...])
    #         using a list of (role, template_string) tuples:
    #   - ("system", ...) telling the model it's a friendly cooking assistant
    #   - ("human", "Suggest a recipe using these ingredients: {ingredients}")
    prompt = None  # <-- replace this

    # TODO 2: Turn the template into actual messages by calling
    #         prompt.invoke({"ingredients": "..."}) with ingredients of your choice.
    messages = None  # <-- replace this

    # TODO 3: Pass `messages` to llm.invoke(...) and print the response's .content.


if __name__ == "__main__":
    main()
