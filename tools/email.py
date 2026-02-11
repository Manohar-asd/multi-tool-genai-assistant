from openai_client import client, MODEL
import os

def generate_email(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "Write a professional email."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def generate_email_tool(prompt: str) -> dict:
    """Generate a professional email"""
    return {
        "name": "generate_email",
        "arguments": {
            "prompt": prompt
        }
    }
