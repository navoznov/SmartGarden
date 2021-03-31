from hardware.device import Device
import hardware.deviceTypes as deviceTypes

class Lcd1602(Device):
    """LCD-экран 16х2"""

    def __init__(self, id: str, pin, mqtt_topic: str, name: str=None, description: str=None):
        # self.pin = onionGpio.OnionGpio(pin)
        self.pin = pin
        self.state = state
        self.mqtt_topic = mqtt_topic
        super().__init__(id, deviceTypes.LCD1602, name, description)

    def print(text):
        lines = text.split('\n')
        # TODO: релазиовать вывод текста на экран
        pass