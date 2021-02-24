#!/usr/bin/env python
# -*- coding: utf-8 -*-

from options import Options
from optionsParser import OptionsParser
from telegram.telegramBot import TelegramBot
import GardenConfigParser
from deviceBuilder import DeviceBuilder


def main():
    # # получаем настройки приложения
    options = OptionsParser.parse()

    # получаем конфиг
    config_json_str = open("gardenConfig.json").read()
    config = GardenConfigParser.parse(config_json_str)

    # получаем настройки устройств
    device_configs = config.get("devices", [])

    # составляем список устройств
    device_builder = DeviceBuilder()
    # REFACTORING: переписать цилк в одну строку
    # devices = [build_device(x) for x in device_configs]
    devices = []
    for device_config in device_configs:
        device = device_builder.build_device(device_config)
        devices.append(device)

if __name__ == '__main__':
    main()
