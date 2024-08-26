# Dockerfile for Service-B
FROM python:3.9-slim

WORKDIR /app

# Install dependencies directly
RUN pip install Flask

# Copy the script
COPY hello_message.py .

CMD ["python", "hello_message.py"]
