# Dockerfile for Service-A
FROM python:3.9-slim

WORKDIR /app

# Install dependencies directly
RUN pip install Flask requests

# Copy the script
COPY bitcoin_service.py .

CMD ["python", "bitcoin_service.py"]
