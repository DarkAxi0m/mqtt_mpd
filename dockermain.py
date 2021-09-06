#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# test_it.py
#
# Copyright © 2019 Mathieu Gaborit (matael) <mathieu@matael.org>
#
# Licensed under the "THE BEER-WARE LICENSE" (Revision 42):
# Mathieu (matael) Gaborit wrote this file. As long as you retain this notice
# you can do whatever you want with this stuff. If we meet some day, and you
# think this stuff is worth it, you can buy me a beer or coffee in return
#

"""

"""

import os
import string

MQTT_BROKER =  (os.getenv('MQTT_BROKER') or 'mpd.lan').strip()
MQTT_CLIENTID = (os.getenv('MQTT_CLIENTID') or 'mpd_controller').strip()
MQTT_TOPIC = (os.getenv('MQTT_TOPIC') or 'music').strip()
MQTT_PORT = int(os.getenv('MQTT_PORT') or 1883)

MPD_SERVER = (os.getenv('MPD_SERVER') or 'mpd.lan').strip()
MPD_PORT = int(os.getenv('MPD_PORT') or 6600)


print('MQTT Connecting to: {MQTT_BROKER}:{MQTT_PORT}'.format(MQTT_BROKER=MQTT_BROKER,MQTT_PORT=MQTT_PORT))
print('MPD  Connecting to: {MPD_SERVER}:{MPD_PORT}'.format(MPD_SERVER=MPD_SERVER,MPD_PORT=MPD_PORT))


from mqttmpd import MQTTMPDController




# instanciating a controller
controller = MQTTMPDController(
    mqtt_broker=MQTT_BROKER,
    mqtt_client_id=MQTT_CLIENTID,
    mqtt_topicbase=MQTT_TOPIC,
    mqtt_port=MQTT_PORT,
    mpd_server=MPD_SERVER,
    mpd_port=MPD_PORT
)

# loop!
controller.loop_forever()


