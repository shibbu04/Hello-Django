FROM python:3.11
WORKDIR /app
COPY Requirements.txt .
RUN pip install -r Requirements.txt
COPY . .