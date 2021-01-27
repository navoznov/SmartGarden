import Hardware.TemperatureSensor import TemperatureSensor
import Hardware.Valve import Valve
import Hardware.Relay import Relay
import Hardware.Sensor import Sensor
import Hardware.DeviceType import DeviceType

class DeviceBuilder:


    def build_device(self, device_config):
        device_type = device_config.get("type", None)
        if device_type == DeviceType.TEMPERATURE_TYPE:
            return new TemperatureSensor()
        if device_type == DeviceType.VALVE_TYPE:
            return new Valve()
        if device_type == DeviceType.RELAY_TYPE:
            return new Relay()
        if device_type == DeviceType.SENSOR_TYPE:
            return new Sensor()
