#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import onionGpio
import time
from hardware.device import Device
import hardware.deviceTypes as deviceTypes
import hardware.relayTypes as relayTypes
import hardware.switchStates as switchStates


class Relay(Device):
    """реле"""

    def __init__(self, id: str, pin: str, mqtt_topic: str,
                 name: str, description: str = None,
                 relay_type: str = None, state: str = None):
        self.pin = pin
        self.mqtt_topic = mqtt_topic
        self.relay_type = relay_type if relay_type != None else relayTypes.DEFAULT
        self.state = state if state != None else switchStates.OPENED

        super().__init__(id, deviceTypes.RELAY, name, description)

    def open(self, callback = None):
        self.state = true

        # TODO: установить пин в 1
        # TODO: уведомление об открытии
        if callback != None:
            callback()

    def close(self, callback = None):
        self.state = false
        # TODO: установить пин в 0
        # TODO: уведомление о закрытии
        if callback != None:
            callback()
