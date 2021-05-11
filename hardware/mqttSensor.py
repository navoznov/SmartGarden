from hardware.device import Device
import paho.mqtt.client as mqtt

class MqttSensor(Device):
    def __init__(self, id, device_type, mqtt_topic, mqtt_server, name, description):
        self.mqtt_topic = mqtt_topic
        self.__mqtt_server = mqtt_server
        self.__sensor_value = None
        # TODO: использовать один инстанс mqtt-клиента для всех девайсов (и вообще для всех нужд)
        self.__mqtt_client = mqtt.Client(f'mqtt_{id}')

        try:
            self.__mqtt_client.connect(mqtt_server)
        except:
            print(f'Ошибка подключения к серверу MQTT: {self.mqtt_server}')

        self.__mqtt_client.subscribe(self.mqtt_topic)
        self.on_message = self.__handle_on_message

        super().__init__(id, device_type, name, description)


    def __handle_on_message(self, client, userdata, message):
        self.__sensor_value = message

    def get_value(self):
        return self.__sensor_value
