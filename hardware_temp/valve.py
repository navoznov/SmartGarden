#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import onionGpio
from hardware.device import Device
import hardware.deviceTypes as deviceTypes
import hardware.switchStates as switchStates


class Valve(Device):
    """Кран"""

    def __init__(self, id: str, pin: str, state: str, mqtt_topic: str, name: str, description: str = None):
        self.pin = pin
        self.state = switchStates.OPENED if state is None else state
        self.mqtt_topic = mqtt_topic

        super().__init__(id, deviceTypes.VALVE, name, description)

    def open(self, callback = None):
        self.state = switchStates.OPENED
        # TODO: установить пин в 1
        # TODO: уведомление об открытии
        if callback != None:
            callback()

    def close(self, callback = None):
        self.state = switchStates.CLOSED
        # TODO: установить пин в 0
        # TODO: уведомление о закрытии
        if callback != None:
            callback()
