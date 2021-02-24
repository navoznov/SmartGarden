#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hardware.temperatureSensor import TemperatureSensor
from hardware.valve import Valve
from hardware.relay import Relay
from hardware.sensor import Sensor
from hardware.linearActuator import LinearActuator
from hardware.deviceType import DeviceType


class DeviceBuilder:

    def build_device(self, device_config):
        id = device_config.get("id", None)
        device_type = device_config.get("type", None)
        name = device_config.get("name", None)
        description = device_config.get("description", None)
        pin = device_config.get("pin", None)
        mqtt_topic = device_config.get("mqttTopic", None)

        if device_type == DeviceType.TEMPERATURE:
            return TemperatureSensor()
        if device_type == DeviceType.VALVE:
            return Valve(id, pin, state, mqtt_topic, name, description)
        if device_type == DeviceType.RELAY:
            relay_type = device_config.get("relay_type", None)
            state = device_config.get("state", None)
            return Relay(id, pin, mqtt_topic, name, description,
                             relay_type, state)
        if device_type == DeviceType.SENSOR:
            return Sensor(id, pin, mqtt_topic, name, description)
        if device_type == DeviceType.LINEAR_ACTUATOR:
            state = device_config.get("state", None)
            open_close_timeout_in_sec = device_config.get(
                "open_close_timeout_in_sec", None)
            return LinearActuator(id, pin, mqtt_topic, name, description,
                                      state, open_close_timeout_in_sec)
