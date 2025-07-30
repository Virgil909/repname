FROM python:3.12.2-bullseye

LABEL description="Health Monitor"


WORKDIR /usr/echipa1
COPY src .


RUN set -ex && pip install --no-cache-dir -r requirements.txt

EXPOSE 5009

CMD flask run --host=0.0.0.0 --port=5009

#docker build -t echipa1:tag