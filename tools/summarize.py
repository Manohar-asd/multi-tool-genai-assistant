from azure_client import client
import os

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

def summarize_text(text: str) -> str:
    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "Summarize the text clearly."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

def summarize_text_tool(text: str) -> dict:
    """Summarize the given text"""
    return {
        "name": "summarize_text",
        "arguments": {
            "text": text
        }
    }
