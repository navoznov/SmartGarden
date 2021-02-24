#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import onionGpio
from hardware.device import Device
import hardware.deviceType as deviceType
import hardware.valveStates as valveStates

class Valve(Device):
    """Кран"""

    def __init__(self, id: str, pin: str, state: str = None, mqtt_topic: str, name: str, description: str=None):
        self.pin = pin
        self.state = valveStates.OPENED if state is None else state
        self.mqtt_topic = mqtt_topic

        super().__init__(id, deviceType.VALVE, name, description)

    def open(self):
        self.state = valveStates.OPENED
        # TODO: установить пин в 1
        # TODO: уведомление об открытии

    def close(self):
        self.state = valveStates.CLOSED
        # TODO: установить пин в 0
        # TODO: уведомление о закрытии
