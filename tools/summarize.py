from openai_client import client, MODEL
import os

def summarize_text(text: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
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
