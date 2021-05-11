#!/usr/bin/env python
# -*- coding: utf-8 -*-

from options import options, Options
from config import config

import globalOptions
globalOptions.is_fake = options.is_fake_gpio_mode

import logging, json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, InlineQueryHandler
import states, buttonTitles, deviceBuilder, garden
import handlers

console_logging_handler = logging.StreamHandler()
logging.basicConfig(handlers=(console_logging_handler,), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

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
            MessageHandler(Filters.text(buttonTitles.VIEW_STATUS_BUTTON), handlers.view_status_handler),
            MessageHandler(Filters.regex('Открыть .+') | Filters.regex('Включить .+'), handlers.open_device_handler),
            MessageHandler(Filters.regex('Закрыть .+') | Filters.regex('Выключить .+'), handlers.close_device_handler),
        ],
    },
    fallbacks=[CommandHandler('cancel', handlers.cancel)],
)
updater.dispatcher.add_handler(conversation_handler)
updater.dispatcher.add_handler(CommandHandler('set', handlers.debug_set_pin_value))
updater.start_polling()
updater.idle()
