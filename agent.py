from azure_client import client, DEPLOYMENT
from tools.email import generate_email
from tools.summarize import summarize_text
from tools.document_qa import document_qa

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "generate_email",
            "description": "Generate a professional email",
            "parameters": {
                "type": "object",
                "properties": {
                    "prompt": {"type": "string"}
                },
                "required": ["prompt"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "summarize_text",
            "description": "Summarize the given text",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"}
                },
                "required": ["text"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "document_qa",
            "description": "Search documents and answer questions from them",
            "parameters": {
                "type": "object",
                "properties": {
                    "question": {"type": "string"}
                },
                "required": ["question"]
            }
        }
    }
]

def agent_chat(user_input: str):
    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[{"role": "user", "content": user_input}],
        tools=TOOLS,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if message.tool_calls:
        tool_call = message.tool_calls[0]
        name = tool_call.function.name
        args = eval(tool_call.function.arguments)

        if name == "generate_email":
            return generate_email(args["prompt"])
        elif name == "summarize_text":
            return summarize_text(args["text"])
        elif name == "document_qa":
            return document_qa(args["question"])

    return message.content
