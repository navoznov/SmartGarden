#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import onionGpio
from hardware.device import Device
import hardware.deviceTypes as deviceTypes
import hardware.relayTypes as relayTypes

class Relay(Device):
    """реле"""



    # состояние реле "открыто"
    OPEN_STATE = "OPEN"
    # состояние реле "закрыто"
    CLOSED_STATE = "CLOSED"
    # дефолтное состояние реле
    DEFAULT_STATE = OPEN_STATE

    def __init__(self, id: str, pin: str, mqtt_topic: str,
                 name: str, description: str=None,
                 relay_type: str=None, state: str=None):
        self.pin = pin
        self.mqtt_topic = mqtt_topic
        self.relay_type = relay_type if relay_type != None else relayTypes.DEFAULT
        self.state = state if state != None else self.DEFAULT_STATE

        super().__init__(id, deviceTypes.RELAY, name, description)

    def open(self):
        self.state = true
        # TODO: установить пин в 1
        # TODO: уведомление об открытии

    def close(self):
        self.state = false
        # TODO: установить пин в 0
        # TODO: уведомление о закрытии
