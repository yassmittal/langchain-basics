# LangChain Basics (Python + DeepSeek-R1 on Amazon Bedrock)

A hands-on project for learning LangChain by typing the code yourself. Each
lesson has TODOs with hints; a matching, complete file lives in `solutions/`
for when you're stuck or want to check your work.

## Setup

1. Create and activate a virtualenv:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill it in:
   ```
   cp .env.example .env
   ```
   - Auth is a **Bedrock API key** (bearer token) - not IAM access/secret
     keys. Generate one in the AWS console under **Amazon Bedrock -> API
     keys**, and put it in `BEDROCK_API_KEY`. `config.py` copies it into the
     `AWS_BEARER_TOKEN_BEDROCK` env var that boto3 reads automatically - this
     requires a fairly recent `boto3`/`botocore` (already pinned in
     `requirements.txt`); if auth fails with an old-looking error, run
     `pip install --upgrade boto3 botocore`.
   - Set `BEDROCK_MODEL_ID` to a model you have access to - default is
     DeepSeek-R1 (`deepseek.r1-v1:0`), on-demand/serverless, no Marketplace
     subscription needed. Check the AWS console under **Amazon Bedrock ->
     Model access** for what's enabled and the exact ID in your region; some
     regions need a cross-region inference profile prefix (`us.`/`eu.`).

**Note on lessons 04 and 06:** structured output and tool-calling support on
Bedrock's Converse API varies by model. If `with_structured_output` or
`bind_tools` errors out on DeepSeek-R1, that's a model capability gap, not a
mistake in your code - check the "Tool use" column for your model on the
[Bedrock model support page](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html),
or temporarily point `BEDROCK_MODEL_ID` at a model that supports tools to get
the lesson's concept working end-to-end.

## Lessons

Run any lesson with `python lessons/<file>.py` from the project root.

| # | File | Concept |
|---|------|---------|
| 01 | `01_first_call.py` | Chat models, `.invoke()`, messages |
| 02 | `02_prompt_templates.py` | `ChatPromptTemplate` with variables |
| 03 | `03_chains_lcel.py` | Composing steps with LCEL's `\|` operator |
| 04 | `04_output_parsers.py` | Structured output via Pydantic models |
| 05 | `05_memory_conversation.py` | Multi-turn conversation history |
| 06 | `06_tools_and_agents.py` | Binding tools, handling tool calls |
| 07 | `07_rag_basics.py` | Retrieval-Augmented Generation basics |

Work through them in order - each builds on ideas from the last. Open the
lesson file, read the docstring and TODOs, and fill in the blanks yourself.
`config.py` (shared setup, not a lesson) is already complete.

## Stuck?

Compare against `solutions/<same file>.py` - same filename, complete
implementation.
# langchain-basics
