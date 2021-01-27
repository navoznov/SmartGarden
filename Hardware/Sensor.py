import onionGpio

class Sensor:
    def __init__(self, id, pin, mqtt_topic, name=None, description=None):
        self.__id = id
        self.__pin = onionGpio.OnionGpio(pin)
        self.__state = state
        self.__mqtt_topic = mqtt_topic
        self.__name = name if name != None else "Датчик " + str(pin)
        self.__description = description if description != None else "Датчик " + \
            str(pin)

    def read_value(self) -> str:
        return self.__pin.getValue()