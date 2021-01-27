import onionGpio
from Hardware.Device import Device
from Hardware.DeviceType import DeviceType

class Valve(Device):
    def __init__(self, id, pin, state, mqtt_topic, name=None, description=None):
        self.pin = onionGpio.OnionGpio(pin)
        self.state = state
        self.mqtt_topic = mqtt_topic
        super().__init__(id, DeviceType.VALVE, name, description)

    def open(self):
        self.state = true
        # TODO: установить пин в 1
        # TODO: уведомление об открытии

    def close(self):
        self.state = false
        # TODO: установить пин в 0
        # TODO: уведомление о закрытии
