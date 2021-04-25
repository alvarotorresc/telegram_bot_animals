# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]
