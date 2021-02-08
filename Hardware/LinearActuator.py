import onionGpio
from hardware.device import Device
from hardware.deviceType import DeviceType

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

    def __init__(self, id: str, pin: int, mqtt_topic: str,
                 name=None: str, description=None: str,
                 state=DEFAULT_STATE: str,
                 open_close_timeout_in_sec=DEFAULT_OPEN_CLOSE_TIMEOUT_IN_SEC: int):
        self.pin = onionGpio.OnionGpio(pin)
        self.mqtt_topic = mqtt_topic
        self.relay_type = relay_type if relay_type != None else DEFAULT_RELAY_TYPE
        self.state = state if state != None else DEFAULT_STATE
        self.open_close_timeout_in_sec = open_close_timeout_in_sec if open_close_timeout_in_sec != None else DEFAULT_OPEN_CLOSE_TIMEOUT_IN_SEC
        super().__init__(id, DeviceType.RELAY, name, description)

    def open(self):
        self.state = LinearActuator.WORKING_STATE
        # TODO: на время open_close_timeout_in_sec подавать 1 на пин
        self.state = LinearActuator.OPEN_STATE

    def close(self):
        self.state = LinearActuator.WORKING_STATE
        # TODO: на время open_close_timeout_in_sec подавать 0 на пин
        self.state = LinearActuator.CLOSED_STATE
