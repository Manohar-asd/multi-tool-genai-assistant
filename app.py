from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent_chat

app = FastAPI(title="Azure AI Foundry Agent (Tool Calling)")

class ChatRequest(BaseModel):
    user_input: str

@app.post("/chat")
def chat(request: ChatRequest):
    return {"response": agent_chat(request.user_input)}
