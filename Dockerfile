FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/
COPY api.py /app/
COPY chatbot.py /app/
COPY data /app/data/

RUN pip install --no-cache-dir -r requirements.txt

# Let Dockerfile expose default port
EXPOSE 8000

# Run Uvicorn with dynamic port from env (default to 8000)
CMD ["sh", "-c", "uvicorn api:app --host 0.0.0.0 --port ${PORT:-8000}"]
