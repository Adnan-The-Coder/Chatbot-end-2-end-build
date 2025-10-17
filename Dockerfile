# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container (if you have it)
# For now, I'm assuming it's not present based on your folder structure
COPY requirements.txt /app/

# Install the dependencies (if requirements.txt exists)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main Python script and the data folder into the container
COPY main.py /app/
COPY data /app/data/

# Expose port (optional, useful if you want to run a web interface)
# EXPOSE 5000

# Set the default command to run the chatbot script
CMD ["python", "main.py"]
