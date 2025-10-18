# api.py

from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import chatbot_response  # ✅ Import your logic

app = FastAPI()

# Define request model
class ChatRequest(BaseModel):
    message: str

# Define chat route
@app.post("/chat")
def chat_endpoint(req: ChatRequest):
    response = chatbot_response(req.message)
    return {"response": response}
