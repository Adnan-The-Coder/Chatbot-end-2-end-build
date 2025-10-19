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
    """Professional API documentation homepage"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ML Chatbot API - Dynamic AI-Powered Conversations</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #333;
                line-height: 1.6;
                min-height: 100vh;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            
            .hero {
                background: rgba(255, 255, 255, 0.95);
                border-radius: 20px;
                padding: 60px 40px;
                margin-bottom: 30px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                text-align: center;
            }
            
            .hero h1 {
                font-size: 3em;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 10px;
            }
            
            .hero .tagline {
                font-size: 1.3em;
                color: #666;
                margin-bottom: 30px;
            }
            
            .badges {
                display: flex;
                gap: 15px;
                justify-content: center;
                flex-wrap: wrap;
                margin-bottom: 20px;
            }
            
            .badge {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 8px 20px;
                border-radius: 20px;
                font-size: 0.9em;
                font-weight: 600;
            }
            
            .author {
                margin-top: 20px;
                font-size: 1.1em;
                color: #555;
            }
            
            .author a {
                color: #667eea;
                text-decoration: none;
                font-weight: 600;
                transition: all 0.3s;
            }
            
            .author a:hover {
                color: #764ba2;
                text-decoration: underline;
            }
            
            .section {
                background: rgba(255, 255, 255, 0.95);
                border-radius: 15px;
                padding: 40px;
                margin-bottom: 30px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            }
            
            .section h2 {
                color: #667eea;
                margin-bottom: 20px;
                font-size: 2em;
                display: flex;
                align-items: center;
                gap: 10px;
            }
            
            .endpoint {
                background: #f8f9fa;
                border-left: 4px solid #667eea;
                padding: 20px;
                margin: 20px 0;
                border-radius: 8px;
            }
            
            .endpoint-header {
                display: flex;
                align-items: center;
                gap: 15px;
                margin-bottom: 15px;
            }
            
            .method {
                background: #28a745;
                color: white;
                padding: 5px 15px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 0.9em;
            }
            
            .method.post {
                background: #007bff;
            }
            
            .path {
                font-family: 'Courier New', monospace;
                font-size: 1.1em;
                color: #333;
                font-weight: 600;
            }
            
            .code-block {
                background: #2d2d2d;
                color: #f8f8f2;
                padding: 20px;
                border-radius: 8px;
                overflow-x: auto;
                margin: 15px 0;
                font-family: 'Courier New', monospace;
            }
            
            .features {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-top: 20px;
            }
            
            .feature-card {
                background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
                padding: 25px;
                border-radius: 10px;
                border: 2px solid #667eea30;
                transition: transform 0.3s;
            }
            
            .feature-card:hover {
                transform: translateY(-5px);
            }
            
            .feature-card h3 {
                color: #667eea;
                margin-bottom: 10px;
            }
            
            .cta-buttons {
                display: flex;
                gap: 20px;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 30px;
            }
            
            .btn {
                padding: 15px 30px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: 600;
                transition: all 0.3s;
                display: inline-block;
            }
            
            .btn-primary {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            
            .btn-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
            }
            
            .btn-secondary {
                background: white;
                color: #667eea;
                border: 2px solid #667eea;
            }
            
            .btn-secondary:hover {
                background: #667eea;
                color: white;
            }
            
            .status-indicator {
                display: inline-flex;
                align-items: center;
                gap: 8px;
                background: #d4edda;
                color: #155724;
                padding: 8px 15px;
                border-radius: 20px;
                font-size: 0.9em;
                margin-top: 10px;
            }
            
            .status-dot {
                width: 10px;
                height: 10px;
                background: #28a745;
                border-radius: 50%;
                animation: pulse 2s infinite;
            }
            
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.5; }
            }
            
            .tech-stack {
                display: flex;
                gap: 10px;
                flex-wrap: wrap;
                margin-top: 15px;
            }
            
            .tech-badge {
                background: #e9ecef;
                padding: 5px 12px;
                border-radius: 5px;
                font-size: 0.85em;
                color: #495057;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="hero">
                <h1>🤖 ML Chatbot API</h1>
                <p class="tagline">Dynamic AI-Powered Conversational Intelligence</p>
                <div class="badges">
                    <span class="badge">Machine Learning</span>
                    <span class="badge">NLP Powered</span>
                    <span class="badge">FastAPI</span>
                    <span class="badge">Scikit-learn</span>
                </div>
                <div class="status-indicator">
                    <span class="status-dot"></span>
                    <span>System Operational</span>
                </div>
                <div class="author">
                    Created by <a href="https://AdnanTheCoder.com" target="_blank">Adnan</a> | 
                    <a href="https://github.com/Adnan-The-Coder" target="_blank">@Adnan-The-Coder</a>
                </div>
            </div>
            
            <div class="section">
                <h2>📚 Overview</h2>
                <p>This API provides intelligent chatbot responses using Machine Learning models trained on custom intent datasets. Built with FastAPI and powered by Logistic Regression with TF-IDF vectorization for accurate natural language understanding.</p>
                
                <div class="tech-stack">
                    <span class="tech-badge">Python 3.x</span>
                    <span class="tech-badge">FastAPI</span>
                    <span class="tech-badge">Scikit-learn</span>
                    <span class="tech-badge">NLTK</span>
                    <span class="tech-badge">TF-IDF</span>
                    <span class="tech-badge">Docker</span>
                </div>
            </div>
            
            <div class="section">
                <h2>🎯 Features</h2>
                <div class="features">
                    <div class="feature-card">
                        <h3>🧠 ML-Powered</h3>
                        <p>Trained using Logistic Regression and TF-IDF vectorization for accurate intent classification</p>
                    </div>
                    <div class="feature-card">
                        <h3>⚡ Fast & Efficient</h3>
                        <p>Built on FastAPI for high-performance asynchronous request handling</p>
                    </div>
                    <div class="feature-card">
                        <h3>🔧 Customizable</h3>
                        <p>Easily train on custom datasets with your own intents and responses</p>
                    </div>
                    <div class="feature-card">
                        <h3>🐳 Docker Ready</h3>
                        <p>Fully containerized for easy deployment anywhere</p>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>🔌 API Endpoints</h2>
                
                <div class="endpoint">
                    <div class="endpoint-header">
                        <span class="method post">POST</span>
                        <span class="path">/chat/datanyx</span>
                    </div>
                    <p><strong>Description:</strong> Get intelligent responses from the DataNyx chatbot trained on company information and general queries.</p>
                    <p><strong>Training Data:</strong> <a href="https://github.com/Adnan-The-Coder/Chatbot-end-2-end-build/blob/main/data/datanyx-general-info.json" target="_blank">datanyx-general-info.json</a></p>
                    
                    <p style="margin-top: 15px;"><strong>Request Body:</strong></p>
                    <div class="code-block">{
  "message": "Hello, how can you help me?"
}</div>
                    
                    <p><strong>Response:</strong></p>
                    <div class="code-block">{
  "response": "Hello! I'm here to help you.",
  "chatbot": "datanyx"
}</div>
                </div>
                
                <div class="endpoint">
                    <div class="endpoint-header">
                        <span class="method">GET</span>
                        <span class="path">/</span>
                    </div>
                    <p><strong>Description:</strong> API documentation homepage (this page)</p>
                </div>
                
                <div class="endpoint">
                    <div class="endpoint-header">
                        <span class="method">GET</span>
                        <span class="path">/swagger</span>
                    </div>
                    <p><strong>Description:</strong> Interactive Swagger UI documentation</p>
                </div>
                
                <div class="endpoint">
                    <div class="endpoint-header">
                        <span class="method">GET</span>
                        <span class="path">/redoc</span>
                    </div>
                    <p><strong>Description:</strong> ReDoc API documentation</p>
                </div>
            </div>
            
            <div class="section">
                <h2>💻 Quick Start</h2>
                <p><strong>cURL Example:</strong></p>
                <div class="code-block">curl -X POST "http://localhost:8080/chat/datanyx" \
  -H "Content-Type: application/json" \
  -d '{"message": "What services do you offer?"}'</div>
                
                <p style="margin-top: 20px;"><strong>Python Example:</strong></p>
                <div class="code-block">import requests

response = requests.post(
    "http://localhost:8080/chat/datanyx",
    json={"message": "What services do you offer?"}
)
print(response.json())</div>

                <p style="margin-top: 20px;"><strong>JavaScript Example:</strong></p>
                <div class="code-block">fetch('http://localhost:8080/chat/datanyx', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ message: 'What services do you offer?' })
})
.then(res => res.json())
.then(data => console.log(data));</div>
            </div>
            
            <div class="section">
                <h2>🚀 Deploy Your Own</h2>
                <p>Clone the repository and deploy your custom chatbot:</p>
                <div class="code-block">git clone https://github.com/Adnan-The-Coder/Chatbot-end-2-end-build.git
cd Chatbot-end-2-end-build
pip install -r requirements.txt
uvicorn api:app --reload</div>
                
                <p style="margin-top: 20px;"><strong>Docker Deployment:</strong></p>
                <div class="code-block">docker build -t ml-chatbot-api .
docker run -p 8080:8000 ml-chatbot-api</div>
            </div>
            
            <div class="section" style="text-align: center;">
                <h2>📖 Documentation & Resources</h2>
                <div class="cta-buttons">
                    <a href="/swagger" class="btn btn-primary">Swagger UI</a>
                    <a href="/redoc" class="btn btn-primary">ReDoc</a>
                    <a href="https://github.com/Adnan-The-Coder/Chatbot-end-2-end-build" target="_blank" class="btn btn-secondary">GitHub Repository</a>
                    <a href="https://AdnanTheCoder.com" target="_blank" class="btn btn-secondary">Author's Website</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content