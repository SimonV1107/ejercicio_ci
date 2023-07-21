FROM python:3.10-alpine

RUN pip install --upgrade pip

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt

CMD uvicorn api:app
