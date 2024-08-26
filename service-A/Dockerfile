
FROM python:3.9-slim

WORKDIR /app


RUN pip install Flask requests

COPY bitcoin_service.py .

CMD ["python", "bitcoin_service.py"]
