import onionGpio
from Hardware.Device import Device
from Hardware.DeviceType import DeviceType

class Sensor(Device):
    def __init__(self, id, pin, mqtt_topic, name=None, description=None):
        self.pin = onionGpio.OnionGpio(pin)
        self.state = state
        self.mqtt_topic = mqtt_topic

        super().__init__(id, DeviceType.SENSOR,  name, description)

    def read_value(self) -> str:
        return self.pin.getValue()