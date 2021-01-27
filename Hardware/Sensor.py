import onionGpio
from Hardware.Device import Device
from Hardware.DeviceType import DeviceType

class Sensor(Device):
    def __init__(self, id, pin, mqtt_topic, name=None, description=None):
        self.__pin = onionGpio.OnionGpio(pin)
        self.__state = state
        self.__mqtt_topic = mqtt_topic

        super().__init__(id, DeviceType.SENSOR_TYPE,  name, description)

    def read_value(self) -> str:
        return self.__pin.getValue()