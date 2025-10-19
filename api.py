from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import Chatbot  # Import the Chatbot class

app = FastAPI()

# Initialize the chatbots once when the app starts with the specified data files
datanyx_chatbot = Chatbot(file_path="data/datanyx-general-info.json")

# Define request model
class ChatRequest(BaseModel):
    message: str

# Define chat route
@app.post("/chat/datanyx")
def chat_endpoint(req: ChatRequest):
    response = datanyx_chatbot.get_response(req.message)  # Use the get_response method
    return {"response": response}
