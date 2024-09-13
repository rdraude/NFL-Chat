import os
from openai import OpenAI

# Retrieve the API token from environment variables
token = os.environ["GITHUB_TOKEN"]

# Define the endpoint and model name
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

# Initialization
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)
userQ = input("Enter your question: ")

# Query the API
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. You must only answer questions about the NFL, or the National Football League.",
        },
        {
            "role": "user",
            "content": userQ,
        }
    ],
    model=model_name,
)
print(response.choices[0].message.content)