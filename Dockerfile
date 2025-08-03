FROM python:3-alpine

ENV TZ="Europe/Amsterdam"

WORKDIR /$CONTAINER_NAME

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .python_hue /root/.python_hue
COPY $SCRIPT_NAME /$CONTAINER_NAME

CMD python $SCRIPT_NAME
