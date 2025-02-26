FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    git

RUN pip install --no-cache-dir --upgrade -r requirements.txt
    
CMD ["fastapi", "run", "rag/app.py", "--port", "8000"]
