from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
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


@app.get("/", response_class=HTMLResponse)
def root():
    """API documentation homepage"""
    # Load HTML from external file
    with open("UI-templates/index.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return html_content

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "ML Chatbot API",
        "version": "1.0.0",
        "active_chatbots": ["datanyx"]
    }