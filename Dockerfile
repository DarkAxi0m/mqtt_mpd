FROM python:3.11-rc-slim

ENV MQTT_BROKER='mpd.lan'
ENV MQTT_CLIENTID='mpd_controller'
ENV MQTT_TOPIC='music'
ENV MQTT_PORT=1883

ENV MPD_SERVER='mpd.lan'
ENV MPD_PORT=6600

WORKDIR /app
COPY requirements.txt /app/requirements.txt 

RUN pip install -r requirements.txt


COPY . /app
ADD dockermain.py  /app/mqtt_mpd

CMD [ "python3","-u","/app/mqtt_mpd" ]