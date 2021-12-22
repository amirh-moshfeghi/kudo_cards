FROM python:3.9.5-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "A.wsgi", ":8000"]