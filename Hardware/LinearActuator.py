import time
import logging
import onionGpio
from hardware.device import Device
import hardware.deviceTypes as deviceTypes
import hardware.linearActuatorStates as linearActuatorStates
from typing import List


class LinearActuator(Device):
    """линейный актуатор"""

    # дефолтное максимальное время полного открыти (или закрытия) актуатора (в секундах)
    __DEFAULT_OPEN_CLOSE_TIMEOUT_IN_SEC = 5

    def __init__(self, id: str, pins: List[str], mqtt_topic: str,
                 name: str, description: str = None,
                 state: str = None, open_close_timeout_in_sec: int = None):
        # линейный актуатор подключается на два пина
        self.pin1, self.pin2 = pins
        self.mqtt_topic = mqtt_topic
        self.state = state if state != None else linearActuatorStates.DEFAULT
        self.open_close_timeout_in_sec = open_close_timeout_in_sec if open_close_timeout_in_sec != None else self.__DEFAULT_OPEN_CLOSE_TIMEOUT_IN_SEC

        super().__init__(id, deviceTypes.RELAY, name, description)

    def open(self, callback=None):
        if self.state == linearActuatorStates.WORKING:
            print(f'{self.name} дождитесь открытия/закрытия линейного актуатора')
            return

        if self.state == linearActuatorStates.OPENED:
            print(f'{self.name} уже открыт')
            return

        self.state = linearActuatorStates.WORKING
        time.sleep(self.open_close_timeout_in_sec)
        # TODO: на время open_close_timeout_in_sec подавать 1 на pin1
        self.state = linearActuatorStates.OPEN
        if callback != None:
            callback()

    def close(self, callback=None):
        if self.state == linearActuatorStates.WORKING:
            print(f'{self.name} дождитесь открытия/закрытия линейного актуатора')
            return

        if self.state == linearActuatorStates.CLOSED:
            print(f'{self.name} уже закрыт')
            return

        self.state = linearActuatorStates.WORKING
        time.sleep(self.open_close_timeout_in_sec)
        # TODO: на время open_close_timeout_in_sec подавать 1 на pin2
        self.state = linearActuatorStates.CLOSED
        if callback != None:
            callback()
