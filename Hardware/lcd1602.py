from hardware.device import Device
from hardware.deviceType import DeviceType

class Lcd1602(Device):
    """LCD-экран 16х2"""

    def __init__(self, id, pin, mqtt_topic, name=None, description=None):
        self.pin = onionGpio.OnionGpio(pin)
        self.state = state
        self.mqtt_topic = mqtt_topic
        super().__init__(id, DeviceType.LCD1602, name, description)

    def print(text):
        lines = text.split('\n')
        # TODO: релазиовать вывод текста на экран
        pass