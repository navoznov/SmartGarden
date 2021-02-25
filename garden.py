# import RPi.GPIO as GPIO
from config import config
from hardware.device import Device
import deviceBuilder
from typing import List


def __get_devices() -> List[Device]:
    # получаем настройки устройств
    device_configs = config.get("devices", [])

    # составляем список устройств
    # REFACTORING: переписать цилк в одну строку
    # devices = [build_device(x) for x in device_configs]
    devices = []
    for device_config in device_configs:
        device = deviceBuilder.build_device(device_config)
        devices.append(device)
    return devices


devices = __get_devices()


def get_devices_by_type(device_type: str) -> List[Device]:
    return [d for d in devices if d.device_type == device_type]


def get_device_by_id(id) -> Device:
    return {d.id: d for d in devices}.get(id, None)
