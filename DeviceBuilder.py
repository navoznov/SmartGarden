import Hardware.TemperatureSensor import TemperatureSensor
import Hardware.Valve import Valve
import Hardware.Relay import Relay
import Hardware.Sensor import Sensor
import Hardware.LinearActuator import LinearActuator
import Hardware.DeviceType import DeviceType


class DeviceBuilder:

    def build_device(self, device_config):
        id = device_config.get("id", None)
        device_type = device_config.get("type", None)
        name = device_config.get("name", None)
        description = device_config.get("description", None)
        pin = device_config.get("pin", None)
        mqtt_topic = device_config.get("mqttTopic", None)

        if device_type == DeviceType.TEMPERATURE:
            return new TemperatureSensor()
        if device_type == DeviceType.VALVE:
            return new Valve(id, pin, state, mqtt_topic, name, description)
        if device_type == DeviceType.RELAY:
            relay_type = device_config.get("relay_type", None)
            state = device_config.get("state", None)
            return new Relay(id, pin, mqtt_topic, name, description,
                             relay_type, state)
        if device_type == DeviceType.SENSOR:
            return new Sensor(id, pin, mqtt_topic, name, description)
        if device_type == DeviceType.LINEAR_ACTUATOR:
            state = device_config.get("state", None)
            open_close_timeout_in_sec = device_config.get(
                "open_close_timeout_in_sec", None)
            return new LinearActuator(id, pin, mqtt_topic, name, description,
                                      state, open_close_timeout_in_sec)
