#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import onionGpio
from hardware.device import Device
import hardware.deviceType as deviceType

class Valve(Device):
    """Кран"""

    # состояние крана "полностью открыт"
    OPEN_STATE = "OPEN"
    # состояние крана "полностью закрыт"
    CLOSED_STATE = "CLOSED"

    def __init__(self, id: str, pin: str, state: str, mqtt_topic: str, name: str, description: str=None):
        self.pin = pin)
        self.state = state
        self.mqtt_topic = mqtt_topic

        super().__init__(id, deviceType.VALVE, name, description)

    def open(self):
        self.state = Valve.OPEN_STATE
        # TODO: установить пин в 1
        # TODO: уведомление об открытии

    def close(self):
        self.state = Valve.CLOSED_STATE
        # TODO: установить пин в 0
        # TODO: уведомление о закрытии
