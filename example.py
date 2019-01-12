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

from controller import MPDMQTTController

# instanciating a controller
controller = MPDMQTTController(
    mqtt_broker='mpd.lan',
    mqtt_client_id='mpd_controller',
    mqtt_topicbase='music',
    mqtt_port=1883,
    mpd_server='sulfur',
    mpd_port=6600
)

# loop!
controller.loop_forever()


