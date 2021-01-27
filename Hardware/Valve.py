import onionGpio

class Valve:
    def __init__(self, id, pin, state, mqtt_topic, name=None, description=None):
        self.__id = id
        self.__pin = onionGpio.OnionGpio(pin)
        self.__state = state
        self.__mqtt_topic = mqtt_topic

    def open(self):
        self.__state = true
        # TODO: установить пин в 1
        # TODO: уведомление об открытии

    def close(self):
        self.__state = false
        # TODO: установить пин в 0
        # TODO: уведомление о закрытии
