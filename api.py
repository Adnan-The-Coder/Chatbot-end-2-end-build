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
        "https://datanyx-2025-website.vercel.app/",
        "https://datanyx.in"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Initialize the chatbots once when the app starts with the specified data files
datanyx_chatbot = Chatbot(file_path="data/datanyx-general-info.json")

# Define request model
class ChatRequest(BaseModel):
    message: str

# Define chat route
@app.post("/chat/datanyx")
async def chat_endpoint(req: ChatRequest):
    try:
        response = datanyx_chatbot.get_response(req.message)
        return {"response": response}
    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )


@app.get("/", response_class=HTMLResponse)
def root():
    """Minimal API homepage"""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>ML Chatbot API</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #0a0e27;
            color: #e2e8f0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .container {
            max-width: 500px;
            width: 100%;
            background: #121630;
            padding: 40px 30px;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            text-align: center;
        }

        h1 {
            font-size: 2.6em;
            background: linear-gradient(135deg, #00d4ff, #7c3aed);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 15px;
        }

        p {
            font-size: 1.15em;
            color: #94a3b8;
            margin-bottom: 30px;
        }

        .cta-button {
            display: inline-block;
            padding: 14px 32px;
            border-radius: 10px;
            text-decoration: none;
            font-weight: 600;
            color: white;
            background: #1e2139;
            border: 1px solid #2d3550;
            transition: all 0.3s ease;
            margin-bottom: 20px;
        }

        .cta-button:hover {
            background: #00d4ff;
            color: #0a0e27;
            border-color: #00d4ff;
        }

        .status {
            font-size: 0.9em;
            color: #64748b;
            margin-top: 10px;
        }

        .author {
            margin-top: 25px;
            font-size: 0.95em;
            color: #94a3b8;
        }

        .author a {
            color: #00d4ff;
            text-decoration: none;
            font-weight: bold;
        }

        .author a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 ML Chatbot API</h1>
        <p>FastAPI-powered conversational engine with TF-IDF + Logistic Regression</p>

        <a class="cta-button" href="https://github.com/Adnan-The-Coder/Chatbot-end-2-end-build" target="_blank">
            💻 View on GitHub
        </a>

        <div class="status">
            🚀 Deployed & running | <code>/chat/datanyx</code> available
        </div>

        <div class="author">
            Engineered by <a href="https://adnanthecoder.com" target="_blank">Adnan</a>
        </div>
    </div>
</body>
</html>
    """

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "ML Chatbot API",
        "version": "1.0.0",
        "active_chatbots": ["datanyx"]
    }