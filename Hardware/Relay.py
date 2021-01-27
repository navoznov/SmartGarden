import onionGpio
from Hardware.Device import Device
from Hardware.DeviceType import DeviceType


class Relay(Device):
    NORMALLY_OPEN_TYPE = "NORMALLY_OPEN"
    NORMALLY_CLOSED_TYPE = "NORMALLY_CLOSED"
    DEFAULT_RELAY_TYPE = NORMALLY_OPEN_TYPE

    OPEN_STATE = "OPEN"
    CLOSED_STATE = "CLOSED"
    DEFAULT_STATE = OPEN_STATE

    def __init__(self, id:str, pin:int, mqtt_topic:str, name=None:str, description=None:str, relay_type=DEFAULT_RELAY_TYPE:str, state=DEFAULT_STATE:str):
        self.pin = onionGpio.OnionGpio(pin)
        self.mqtt_topic = mqtt_topic
        self.relay_type = relay_type if relay_type != None else DEFAULT_RELAY_TYPE
        self.state = state if state != None else DEFAULT_STATE
        super().__init__(id, DeviceType.RELAY, name, description)

    def open(self):
        self.state = true
        # TODO: установить пин в 1
        # TODO: уведомление об открытии

    def close(self):
        self.state = false
        # TODO: установить пин в 0
        # TODO: уведомление о закрытии
