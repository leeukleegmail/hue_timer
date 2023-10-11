FROM python:3.12.0-alpine3.18

ARG container_name
ENV CONTAINER_NAME $container_name

ENV TZ="Europe/Amsterdam"

WORKDIR /$CONTAINER_NAME

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .python_hue /root/.python_hue

CMD [ "python", "main.py"]