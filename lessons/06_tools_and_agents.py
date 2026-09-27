"""
Lesson 06 - Tools

Goal: let the LLM call your own Python functions when it needs something it
doesn't know (like live data). This request/response loop - the model asking
for a tool call, you running it, feeding the result back - is the foundation
every agent is built on.

Note: tool-calling support varies by model on Bedrock's Converse API. If it
errors on your configured model, see the README's note on lessons 04/06.

Run with (from the project root): python -m lessons.06_tools_and_agents
"""

from config import get_llm
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool

# TODO 1: Define a function `get_weather(city: str) -> str` decorated with
#         @tool, that returns a fake hardcoded string like
#         f"It's sunny and 22C in {city}."
#         (In a real app this would call a real weather API.)


def main():
    llm = get_llm()

    # TODO 2: Bind your tool to the model: llm.bind_tools([get_weather])
    llm_with_tools = None  # <-- replace this

    messages = [HumanMessage("What's the weather in Tokyo right now?")]

    # TODO 3: Call llm_with_tools.invoke(messages) and store it in `ai_msg`.
    ai_msg = None  # <-- replace this

    # TODO 4: If the model decided to use the tool, it responds with a
    #         `tool_calls` list instead of a plain answer. Print
    #         ai_msg.tool_calls to see the tool name + arguments it wants to
    #         call with.

    # TODO 5 (bonus - completes the loop):
    #   - grab the first item in ai_msg.tool_calls (it has "name", "args", "id")
    #   - actually call get_weather(**that_call["args"])
    #   - append ai_msg to `messages`
    #   - append ToolMessage(content=<the result>, tool_call_id=that_call["id"])
    #     to `messages`
    #   - call llm_with_tools.invoke(messages) again and print the final,
    #     natural-language answer.


if __name__ == "__main__":
    main()
