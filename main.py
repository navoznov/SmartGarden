#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
    InlineQueryHandler
)
import deviceBuilder
import garden
from options import options, Options
from config import config
import json
import buttonTitles
import states
import handlers

devices = garden.devices

updater = Updater(options.telegram_bot_token)
dispatcher = updater.dispatcher
conversation_handler = ConversationHandler(
    entry_points=[
        CommandHandler('start', handlers.start_state_handler),
    ],
    states={
        states.MAIN_STATE: [
            MessageHandler(Filters.text(buttonTitles.OPEN_BOTH_WINDOW_BUTTON), handlers.open_both_windows_handler),
            MessageHandler(Filters.text(buttonTitles.CLOSE_BOTH_WINDOW_BUTTON), handlers.close_both_windows_handler),
            MessageHandler(Filters.regex('Открыть .+') | Filters.regex('Включить .+'), handlers.open_device_handler),
            MessageHandler(Filters.regex('Закрыть .+') | Filters.regex('Выключить .+'), handlers.close_device_handler),
        ],
    },
    fallbacks=[CommandHandler('cancel', handlers.cancel)],
)
updater.dispatcher.add_handler(conversation_handler)
updater.start_polling()
updater.idle()


# ---------------------------------------------------------------------
# # получаем настройки устройств
# device_configs = config.get("devices", [])

# # составляем список устройств
# device_builder = DeviceBuilder()
# # REFACTORING: переписать цилк в одну строку
# # devices = [build_device(x) for x in device_configs]
# devices = []
# for device_config in device_configs:
#     device = device_builder.build_device(device_config)
#     devices.append(device)
