import onionGpio
from hardware.device import Device
from hardware.deviceType import DeviceType

class Sensor(Device):
    """Просто датчик. Абстрактный датчик на одном пине"""

    def __init__(self, id, pin, mqtt_topic, name=None, description=None):
        self.pin = onionGpio.OnionGpio(pin)
        self.state = state
        self.mqtt_topic = mqtt_topic

        super().__init__(id, DeviceType.SENSOR,  name, description)

    def read_value(self) -> str:
        return self.pin.getValue()