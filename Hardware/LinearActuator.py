import time
import onionGpio
from hardware.device import Device
import hardware.deviceTypes as deviceTypes


class LinearActuator(Device):
    """линейный актуатор"""

    # состояние актуатора "полностью открыт"
    OPEN_STATE = "OPEN"
    # состояние актуатора "полностью закрыт"
    CLOSED_STATE = "CLOSED"
    # состояние "в процессе открытия или закрытия"
    WORKING_STATE = "WORKING"
    # дефолтное состояние актуатора
    DEFAULT_STATE = OPEN_STATE

    # дефолтное максимальное время полного открыти (или закрытия) актуатора (в секундах)
    DEFAULT_OPEN_CLOSE_TIMEOUT_IN_SEC = 10

    def __init__(self, id: str, pin: str, mqtt_topic: str,
                 name: str, description: str = None,
                 state: str = None, open_close_timeout_in_sec: int = None):
        self.pin = onionGpio.OnionGpio(int(pin))
        self.mqtt_topic = mqtt_topic
        self.state = state if state != None else self.DEFAULT_STATE
        self.open_close_timeout_in_sec = open_close_timeout_in_sec if open_close_timeout_in_sec != None else self.DEFAULT_OPEN_CLOSE_TIMEOUT_IN_SEC

        super().__init__(id, deviceTypes.RELAY, name, description)

    def open(self, callback):
        self.state = LinearActuator.WORKING_STATE
        time.sleep(actuator.open_close_timeout_in_sec)
        # TODO: на время open_close_timeout_in_sec подавать 1 на пин
        self.state = LinearActuator.OPEN_STATE
        if callback != None:
            callback()

    def close(self, callback):
        self.state = LinearActuator.WORKING_STATE
        time.sleep(actuator.open_close_timeout_in_sec)
        # TODO: на время open_close_timeout_in_sec подавать 0 на пин
        self.state = LinearActuator.CLOSED_STATE
        if callback != None:
            callback()
