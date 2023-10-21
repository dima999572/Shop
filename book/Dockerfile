FROM python:3.11.5

COPY requirements.txt /bookshop/requirements.txt

WORKDIR /bookshop/requirements.txt
RUN pip install -r requirements.txt

COPY . /bookshop
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]