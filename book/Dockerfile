FROM python:3.12-slim

WORKDIR /bookapp

RUN apt update && \
    apt install -y libpq-dev python3-dev gcc

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py" ]

EXPOSE 5002
