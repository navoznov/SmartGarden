import onionGpio
from hardware.device import Device
from hardware.deviceType import DeviceType

class Sensor(Device):
    """Просто датчик. Абстрактный датчик на одном пине"""

    def __init__(self, id: str, pin: str, mqtt_topic: str, name: str, description: str=None):
        self.pin = pin
        self.state = state
        self.mqtt_topic = mqtt_topic

        super().__init__(id, DeviceType.SENSOR,  name, description)

    def read_value(self) -> str:
        pass