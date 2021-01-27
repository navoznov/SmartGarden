import onionGpio
from Hardware.Device import Device
from Hardware.DeviceType import DeviceType

class Valve(Device):
    """Кран"""

    # состояние крана "полностью открыт"
    OPEN_STATE = "OPEN"
    # состояние крана "полностью закрыт"
    CLOSED_STATE = "CLOSED"

    def __init__(self, id, pin, state, mqtt_topic, name=None, description=None):
        self.pin = onionGpio.OnionGpio(pin)
        self.state = state
        self.mqtt_topic = mqtt_topic
        super().__init__(id, DeviceType.VALVE, name, description)

    def open(self):
        self.state = Valve.OPEN_STATE
        # TODO: установить пин в 1
        # TODO: уведомление об открытии

    def close(self):
        self.state = Valve.CLOSED_STATE
        # TODO: установить пин в 0
        # TODO: уведомление о закрытии
