from openai_client import client, MODEL
from tools.email import generate_email
from tools.summarize import summarize_text
from tools.document_qa import document_qa
import json

MOCK_MODE = True

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
    messages = [{"role": "user", "content": user_input}]
    step = 1

    while True:
        print(f"\n===== AGENT LOOP STEP {step} =====")

        if MOCK_MODE:
            print("Mock LLM responding...")

            if step == 1:
                class ToolCall:
                    id = "1"
                    function = type("obj", (), {
                        "name": "document_qa",
                        "arguments": '{"question": "architecture"}'
                    })

                message = type("obj", (), {
                    "tool_calls": [ToolCall()],
                    "content": None
                })

            elif step == 2:
                class ToolCall:
                    id = "2"
                    function = type("obj", (), {
                        "name": "summarize_text",
                        "arguments": '{"text": "Some document content"}'
                    })

                message = type("obj", (), {
                    "tool_calls": [ToolCall()],
                    "content": None
                })

            elif step == 3:
                class ToolCall:
                    id = "3"
                    function = type("obj", (), {
                        "name": "generate_email",
                        "arguments": '{"prompt": "Summary of architecture"}'
                    })

                message = type("obj", (), {
                    "tool_calls": [ToolCall()],
                    "content": None
                })

            else:
                message = type("obj", (), {
                    "tool_calls": None,
                    "content": "Final response from agent."
                })

        else:
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                tools=TOOLS,
                tool_choice="auto"
            )
            message = response.choices[0].message

        if not message.tool_calls:
            print("No more tool calls. Final answer returned.")
            return message.content

        for tool_call in message.tool_calls:
            print(f"Tool requested: {tool_call.function.name}")

            tool_name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            if MOCK_MODE:
                print(f"(Mock execution) Running {tool_name}")

                if tool_name == "document_qa":
                    result = "Mock document content about architecture."
                elif tool_name == "summarize_text":
                    result = "Mock summary of the architecture."
                elif tool_name == "generate_email":
                    result = "Mock email about architecture."
                else:
                    result = "Mock tool result"

            else:
                if tool_name == "generate_email":
                    result = generate_email(args["prompt"])
                elif tool_name == "summarize_text":
                    result = summarize_text(args["text"])
                elif tool_name == "document_qa":
                    result = document_qa(args["question"])
                else:
                    result = "Tool not implemented"

            print(f"Tool executed: {tool_name}")

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })

        step += 1
