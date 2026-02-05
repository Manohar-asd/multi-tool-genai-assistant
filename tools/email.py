from azure_client import client
import os

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

def generate_email(prompt: str) -> str:
    response = client.chat.completions.create(
        model=deployment,
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
