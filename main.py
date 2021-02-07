from GardenConfigParser import GardenConfigParser
from DeviceBuilder import DeviceBuilder


def main():
    # получаем конфиг
    config_json_str = open("gardenConfig.json").read()
    config = GardenConfigParser.parse(config_json_str)

    # получаем настройки устройств
    device_configs = config.get("devices", [])

    # составляем список устройств
    device_builder = new DeviceBuilder()
    # REFACTORING: переписать цилк в одну строку
    # devices = [build_device(x) for x in device_configs]
    devices = []
    for device_config in device_configs:
        device = device_builder.build_device(device_config)
        devices.append(device)


if __name__ == '__main__':
    main()
