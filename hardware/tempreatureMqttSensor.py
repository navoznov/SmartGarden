#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hardware.oneWire import OneWire
import hardware.deviceTypes as deviceTypes
from hardware.mqttSensor import MqttSensor

class TemperatureMqttSensor(MqttSensor):

    def __init__(self, id, mqtt_topic, mqtt_server, name, description):
        super().__init__(id, deviceTypes.TEMPERATURE, mqtt_topic, mqtt_server, name, description)

    def get_status(self) -> str:
        value = self.get_value()
        return f'{self.name}: {str(value) if value else "----"}'
