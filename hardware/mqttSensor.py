from hardware.device import Device
import paho.mqtt.client as mqtt

class MqttSensor(Device):
    def __init__(self, id, device_type, mqtt_topic, mqtt_server, name, description):
        self.__sensor_value = None

        self.mqtt_topic = mqtt_topic
        self.__mqtt_server = mqtt_server
        # TODO: использовать один инстанс mqtt-клиента для всех девайсов (и вообще для всех нужд)
        self.__mqtt_client = mqtt.Client(f'mqtt_{id}')

        try:
            self.__mqtt_client.connect(mqtt_server)
        except:
            print(f'Ошибка подключения к серверу MQTT: {self.mqtt_server}')

        self.__mqtt_client.subscribe(self.mqtt_topic)

        def handle_on_message(client, userdata, message):
            value = message.payload.decode('utf-8')
            self.__sensor_value = value

        self.__mqtt_client.on_message = handle_on_message
        self.__mqtt_client.loop_start()

        super().__init__(id, device_type, name, description)


    def get_value(self):
        return self.__sensor_value
