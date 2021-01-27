import onionGpio


class Relay:
    NORMALLY_OPEN_TYPE = "NORMALLY_OPEN"
    NORMALLY_CLOSED_TYPE = "NORMALLY_CLOSED"

    OPEN_STATE = "OPEN"
    CLOSED_STATE = "CLOSED"

    def __init__(self, id:str, pin:int, mqtt_topic:str, name=None:str, description=None:str, type=NORMALLY_OPEN_TYPE:str, state=OPEN_STATE:str):
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
