from config import get_llm
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"It's sunny and 22C in {city}."


def main():
    llm = get_llm()

    llm_with_tools = llm.bind_tools([get_weather])

    messages = [HumanMessage("What's the weather in Tokyo right now?")]

    ai_msg = llm_with_tools.invoke(messages)

    print(ai_msg.tool_calls)

    if ai_msg.tool_calls:
        call = ai_msg.tool_calls[0]
        result = get_weather.invoke(call["args"])

        messages.append(ai_msg)
        messages.append(ToolMessage(content=result, tool_call_id=call["id"]))

        final = llm_with_tools.invoke(messages)
        print(final.content)


if __name__ == "__main__":
    main()
