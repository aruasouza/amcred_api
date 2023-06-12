FROM python:3.11.4-slim-buster

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]