import onionGpio
from hardware.device import Device
import hardware.deviceType as deviceType

class Sensor(Device):
    """Просто датчик. Абстрактный датчик на одном пине"""

    def __init__(self, id: str, pin: str, mqtt_topic: str, name: str, description: str=None):
        self.pin = pin
        self.state = state
        self.mqtt_topic = mqtt_topic

        super().__init__(id, deviceType.SENSOR,  name, description)

    def read_value(self) -> str:
        pass