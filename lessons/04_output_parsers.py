"""
Lesson 04 - Structured output

Goal: get the LLM to return data in a shape your code can use directly (not a
blob of text you'd have to regex apart), using a Pydantic model plus
`llm.with_structured_output(...)`.

Note: this relies on tool-calling support, which varies by model on Bedrock's
Converse API. If it errors on your configured model, see the README's note
on lessons 04/06.

Run with (from the project root): python -m lessons.04_output_parsers
"""

from config import get_llm
from pydantic import BaseModel


# TODO 1: Define a Pydantic model called `Recipe` with fields:
#   - name: str
#   - ingredients: list[str]
#   - minutes_to_cook: int
class Recipe(BaseModel):
    pass  # <-- replace this


def main():
    llm = get_llm()

    # TODO 2: Create a structured version of the model with
    #         llm.with_structured_output(Recipe)
    structured_llm = None  # <-- replace this

    # TODO 3: Call structured_llm.invoke("...") with a plain-string prompt asking
    #         for a recipe, and print the result. It should come back as a `Recipe`
    #         instance - try printing result.name, result.ingredients,
    #         result.minutes_to_cook individually.


if __name__ == "__main__":
    main()
