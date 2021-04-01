import time
import logging
from hardware.device import Device
import hardware.deviceTypes as deviceTypes
import hardware.switchStates as switchStates
from typing import List
import hardware.gpioHelper as gpioHelper

class LinearActuator(Device):
    """линейный актуатор"""

    # дефолтное максимальное время полного открыти (или закрытия) актуатора (в секундах)
    __DEFAULT_OPEN_CLOSE_TIMEOUT_IN_SEC = 15

    def __init__(self, id: str, pins: List[str], mqtt_topic: str,
                 name: str, description: str = None,
                 state: str = None, open_close_timeout_in_sec: int = None):
        # линейный актуатор подключается на два пина
        self.pin1, self.pin2 = pins

        self.mqtt_topic = mqtt_topic
        self.state = state if state != None else switchStates.CLOSED
        self.open_close_timeout_in_sec = open_close_timeout_in_sec if open_close_timeout_in_sec != None else self.__DEFAULT_OPEN_CLOSE_TIMEOUT_IN_SEC

        super().__init__(id, deviceTypes.LINEAR_ACTUATOR, name, description)

        gpioHelper.setup_pin_out(self.pin1)
        gpioHelper.setup_pin_out(self.pin2)

    def get_status(self) -> str:
        status = f'Линейный актуатор "{self.name}" '

        if self.state == switchStates.OPENED:
            status += 'открыт.'
        elif self.state == switchStates.CLOSED:
            status += 'закрыт.'
        elif self.state == switchStates.WORKING:
            status += 'в процессе открытия или закрытия.'
        else:
            raise NotImplementedError(f'Неизвестное состояние линейного актуатора {self.id}')

        return status

    def open(self, callback=None):
        if self.state == switchStates.WORKING:
            print(f'{self.name} дождитесь открытия/закрытия линейного актуатора')
            return

        if self.state == switchStates.OPENED:
            print(f'{self.name} уже открыт')
            return

        self.state = switchStates.WORKING

        gpioHelper.set_pin_value(self.pin1, 0)
        gpioHelper.set_pin_value(self.pin2, 1)

        time.sleep(self.open_close_timeout_in_sec)

        gpioHelper.set_pin_value(self.pin1, 0)
        gpioHelper.set_pin_value(self.pin2, 0)

        self.state = switchStates.OPENED
        if callback != None:
            callback()

    def close(self, callback=None):
        if self.state == switchStates.WORKING:
            print(f'{self.name} дождитесь открытия/закрытия линейного актуатора')
            return

        if self.state == switchStates.CLOSED:
            print(f'{self.name} уже закрыт')
            return

        self.state = switchStates.WORKING

        gpioHelper.set_pin_value(self.pin1, 1)
        gpioHelper.set_pin_value(self.pin2, 0)

        time.sleep(self.open_close_timeout_in_sec)

        gpioHelper.set_pin_value(self.pin1, 1)
        gpioHelper.set_pin_value(self.pin2, 1)

        self.state = switchStates.CLOSED
        if callback != None:
            callback()
