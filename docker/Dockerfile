FROM python:3.8-slim

WORKDIR /app
COPY app/requirements.txt /app
COPY app/flask_app.py /app
RUN pip install -r requirements.txt
EXPOSE 8080

CMD ["python", "flask_app.py"]
