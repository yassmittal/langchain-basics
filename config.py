"""Shared setup - not a lesson. Every lesson calls get_llm() to get a ready-to-use
chat model, so you don't have to repeat AWS/Bedrock wiring in each file.

Auth uses a Bedrock API key (bearer token), not IAM access/secret keys. boto3
reads the token from the AWS_BEARER_TOKEN_BEDROCK env var, so we copy our
BEDROCK_API_KEY value into it before creating any client."""

import os

from dotenv import load_dotenv
from langchain_aws import ChatBedrockConverse

load_dotenv()

os.environ["AWS_BEARER_TOKEN_BEDROCK"] = os.environ["BEDROCK_API_KEY"]


def get_llm(temperature: float = 0.7) -> ChatBedrockConverse:
    return ChatBedrockConverse(
        model_id=os.environ["BEDROCK_MODEL_ID"],
        region_name=os.environ["BEDROCK_REGION"],
        temperature=temperature,
    )
