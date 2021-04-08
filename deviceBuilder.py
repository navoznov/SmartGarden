#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hardware.temperatureSensor import TemperatureSensor
from hardware.tempreatureMqttSensor import TemperatureMqttSensor
from hardware.valve import Valve
from hardware.relay import Relay
from hardware.sensor import Sensor
from hardware.linearActuator import LinearActuator
import hardware.deviceTypes as deviceTypes


def build_device(device_config):
    id = device_config.get("id", None)
    device_type = device_config.get("type", None)
    name = device_config.get("name", None)
    description = device_config.get("description", None)
    pin = device_config.get("pin", None)
    pins = device_config.get("pins", None)

    mqtt_topic = device_config.get("mqttTopic", None)
    mqtt_server = device_config.get("mqttServer", None)
    state = device_config.get("state", None)

    if device_type == deviceTypes.TEMPERATURE:
        return TemperatureSensor(id, pin, mqtt_topic, name, description)
    elif device_type == deviceTypes.TEMPERATURE_MQTT:
        return TemperatureMqttSensor(id, mqtt_topic, mqtt_server, name, description)
    elif device_type == deviceTypes.VALVE:
        return Valve(id, pin, state, mqtt_topic, name, description)
    elif device_type == deviceTypes.RELAY:
        relay_type = device_config.get("relay_type", None)
        return Relay(id, pin, mqtt_topic, name, description, relay_type, state)
    elif device_type == deviceTypes.SENSOR:
        return Sensor(id, pin, mqtt_topic, name, description)
    elif device_type == deviceTypes.LINEAR_ACTUATOR:
        open_close_timeout_in_sec = device_config.get("open_close_timeout_in_sec", None)
        return LinearActuator(id, pins, mqtt_topic, name, description, state, open_close_timeout_in_sec)
