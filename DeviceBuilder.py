import Hardware.TemperatureSensor import TemperatureSensor
import Hardware.Valve import Valve

class DeviceBuilder:
    # температурный датчик
    TEMPERATURE_TYPE = "temperature"
    # клапан
    VALVE_TYPE = "temperature"

    def build_device(self, device_config):
        device_type = device_config.get("type", None)
        if device_type == self.TEMPERATURE_TYPE:
            return new TemperatureSensor()
        if device_type == self.VALVE_TYPE:
            return new Valve()
