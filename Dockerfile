FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/
COPY api.py /app/
COPY chatbot.py /app/
COPY data /app/data/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
