from config import get_llm
from pydantic import BaseModel


class Recipe(BaseModel):
    name: str
    ingredients: list[str]
    minutes_to_cook: int


def main():
    llm = get_llm()

    structured_llm = llm.with_structured_output(Recipe)

    result = structured_llm.invoke("Give me a simple recipe for pancakes.")

    print(result.name)
    print(result.ingredients)
    print(result.minutes_to_cook)


if __name__ == "__main__":
    main()
