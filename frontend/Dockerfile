FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl dnsutils

WORKDIR /frontendapp

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py" ]

EXPOSE 5000
