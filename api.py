from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from chatbot import Chatbot  # Import the Chatbot class

app = FastAPI()

# CORS Configuration - MUST be before routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "https://localhost:3000",
        "http://127.0.0.1:3000",
        "*"  # For development only - remove in production
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Initialize the chatbots once when the app starts with the specified data files
datanyx_chatbot = Chatbot(file_path="data/datanyx-general-info.json")

# Define request model
class ChatRequest(BaseModel):
    message: str

# Define chat route
@app.post("/chat/datanyx")
async def chat_endpoint(req: ChatRequest):
    """Chat endpoint for Datanyx chatbot"""
    try:
        response = datanyx_chatbot.get_response(req.message)
        return JSONResponse(
            content={"response": response},
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "*",
            }
        )
    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500,
            headers={
                "Access-Control-Allow-Origin": "*",
            }
        )

# Add OPTIONS handler for preflight
@app.options("/chat/datanyx")
async def chat_options():
    """Handle preflight OPTIONS request"""
    return JSONResponse(
        content={"message": "OK"},
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )

@app.get("/", response_class=HTMLResponse)
def root():
    """API documentation homepage"""
    try:
        with open("UI-templates/index.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        return html_content
    except FileNotFoundError:
        return HTMLResponse(content="<h1>Welcome to ML Chatbot API</h1>")

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "ML Chatbot API",
        "version": "1.0.0",
        "active_chatbots": ["datanyx"]
    }