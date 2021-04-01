#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging, re
from typing import List
from telegram import ParseMode, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Message
from telegram.ext import (
    Updater,
    CallbackContext,
    ConversationHandler
)

import hardware.gpioHelper as gpioHelper
import states, buttonTitles, hardware.deviceTypes, hardware.switchStates
from hardware.device import Device
from options import options, Options
import garden


def start_state_handler(update: Update, context: CallbackContext) -> int:
    reply_keyboard = __get_keyboard()
    keyboard_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text('Привет!\n' + __get_status_text(), reply_markup=keyboard_markup)
    return states.MAIN_STATE


def cancel(update: Update, context: CallbackContext) -> int:
    return states.MAIN_STATE


def open_both_windows_handler(update: Update, context: CallbackContext) -> int:
    logging.info(f'Команда открытие всех актуаторов')
    actuators = garden.get_devices_by_type(hardware.deviceTypes.LINEAR_ACTUATOR)
    original_message = update.message
    reply_message = None
    constant_text = ''
    for actuator in actuators:
        text = f'{actuator.name} открывается. Подождите {actuator.open_close_timeout_in_sec} секунд.\n'
        if reply_message:
            reply_message = reply_message.edit_text(constant_text + text)
        else:
            reply_message = original_message.reply_text(constant_text + text, reply_to_message_id=original_message.message_id)

        actuator.open()
        constant_text += f'{actuator.name} открыт.\n'
        reply_message.edit_text(constant_text)

    reply_keyboard = __get_keyboard()
    keyboard_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    original_message.reply_text(__get_status_text(), reply_markup=keyboard_markup)
    return states.MAIN_STATE


def close_both_windows_handler(update: Update, context: CallbackContext) -> int:
    logging.info(f'Команда закрытие всех актуаторов')
    # TODO: избавиться от дублирования кода в open_both_windows_handler и close_both_windows_handler
    actuators = garden.get_devices_by_type(hardware.deviceTypes.LINEAR_ACTUATOR)
    original_message = update.message
    reply_message = None
    constant_text = ''
    for actuator in actuators:
        text = f'{actuator.name} закрывается. Подождите {actuator.open_close_timeout_in_sec} секунд.'
        if reply_message:
            reply_message = reply_message.edit_text(constant_text + text)
        else:
            reply_message = original_message.reply_text(constant_text + text, reply_to_message_id=original_message.message_id)

        actuator.close()
        constant_text += f'{actuator.name} закрыт.\n'
        reply_message.edit_text(constant_text)

    reply_keyboard = __get_keyboard()
    keyboard_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    original_message.reply_text(__get_status_text(), reply_markup=keyboard_markup)
    return states.MAIN_STATE


def open_device_handler(update: Update, context: CallbackContext) -> int:
    match = re.match(r'Открыть (.+)', update.message.text)
    device_id = match.group(1)
    device = garden.get_device_by_id(device_id)
    logging.info(f'Команда открытие "{device.id}"')
    text = f'{device.id} открывается.'
    if hasattr(device, 'open_close_timeout_in_sec'):
        text += f' Подождите {device.open_close_timeout_in_sec} секунд.'
    message = update.message
    message = message.reply_text(text, reply_to_message_id=message.message_id)

    device.open()

    message.edit_text(f'{device.id} открыт.')

    reply_keyboard = __get_keyboard()
    keyboard_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    message.reply_text(__get_status_text(), reply_markup=keyboard_markup)
    return states.MAIN_STATE


def close_device_handler(update: Update, context: CallbackContext) -> int:
    match = re.match(r'Закрыть (.+)', update.message.text)
    device_id = match.group(1)
    device = garden.get_device_by_id(device_id)
    logging.info(f'Команда закрытие "{device.id}"')

    text = f'{device.id} закрывается.'
    if hasattr(device, 'open_close_timeout_in_sec'):
        text += f' Подождите {device.open_close_timeout_in_sec} секунд.'

    message = update.message
    message = message.reply_text(text, reply_to_message_id=message.message_id)

    device.close()

    message.edit_text(f'{device.id} закрыт.')

    reply_keyboard = __get_keyboard()
    keyboard_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(__get_status_text(), reply_markup=keyboard_markup)
    return states.MAIN_STATE


def debug_set_pin_value(update: Update, context: CallbackContext) -> int:
    message = update.message if update.message else update.edited_message
    text = message.text
    _, pinStr, valueStr = text.split(' ')
    gpioHelper.set_pin_value(pinStr, valueStr)


def __get_status_text() -> str:
    devices = garden.get_devices()
    if not devices:
        return ''

    statuses = [d.get_status() for d in devices]
    return '\n'.join(statuses)


def __get_keyboard() -> List[List[str]]:
    def __get_device_type_buttons(device_type):
        def __get_button_text_for_device(device):
            return f'{"Закрыть" if device.state == hardware.switchStates.OPENED else "Открыть"} {device.id}'

        device_finished_states = [hardware.switchStates.OPENED, hardware.switchStates.CLOSED]
        devices = [d for d in garden.get_devices_by_type(device_type) if d.state in device_finished_states]
        return [__get_button_text_for_device(d) for d in devices]

    buttons = []

    # окна
    actuator_buttons = __get_device_type_buttons(hardware.deviceTypes.LINEAR_ACTUATOR)
    buttons.append(actuator_buttons)
    actuators = garden.get_devices_by_type(hardware.deviceTypes.LINEAR_ACTUATOR)

    if len([a for a in actuators if a.state == hardware.switchStates.OPENED]) == 0:
        buttons.append([buttonTitles.OPEN_BOTH_WINDOW_BUTTON])

    if len([a for a in actuators if a.state == hardware.switchStates.CLOSED]) == 0:
        buttons.append([buttonTitles.CLOSE_BOTH_WINDOW_BUTTON])

    # краны
    valve_buttons = __get_device_type_buttons(hardware.deviceTypes.VALVE)
    buttons.append(valve_buttons)

    # реле
    valve_buttons = __get_device_type_buttons(hardware.deviceTypes.RELAY)
    buttons.append(valve_buttons)

    return buttons
