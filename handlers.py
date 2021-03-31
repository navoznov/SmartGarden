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

import states
import buttonTitles
import hardware.deviceTypes
import hardware.switchStates
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
    actuators = garden.get_devices_by_type(hardware.deviceTypes.LINEAR_ACTUATOR)
    for actuator in actuators:
        text = f'{actuator.name} открывается. Подождите {actuator.open_close_timeout_in_sec} секунд.'
        update.message.reply_text(text)
        actuator.open()
        update.message.reply_text(f'{actuator.name} открыт')

    reply_keyboard = __get_keyboard()
    keyboard_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(__get_status_text(), reply_markup=keyboard_markup)
    return states.MAIN_STATE


def close_both_windows_handler(update: Update, context: CallbackContext) -> int:
    actuators = garden.get_devices_by_type(hardware.deviceTypes.LINEAR_ACTUATOR)
    for actuator in actuators:
        text = f'{actuator.name} закрывается. Подождите {actuator.open_close_timeout_in_sec} секунд.'
        update.message.reply_text(text)
        actuator.close()
        update.message.reply_text(f'{actuator.name} закрыт')

    reply_keyboard = __get_keyboard()
    keyboard_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(__get_status_text(), reply_markup=keyboard_markup)
    return states.MAIN_STATE


def open_device_handler(update: Update, context: CallbackContext) -> int:
    match = re.match(r'Открыть (.+)', update.message.text)
    device_id = match.group(1)
    device = garden.get_device_by_id(device_id)

    text = f'{device.id} открывается.'
    if hasattr(device, 'open_close_timeout_in_sec'):
        text += f' Подождите {device.open_close_timeout_in_sec} секунд.'
    message = update.message
    message = update.message.reply_text(text, reply_to_message_id=message.message_id)

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

    text = f'{device.id} закрывается.'
    if hasattr(device, 'open_close_timeout_in_sec'):
        text += f' Подождите {device.open_close_timeout_in_sec} секунд.'

    message = update.message.reply_text(text)

    device.close()

    message.edit_text(f'{device.id} закрыт.')

    reply_keyboard = __get_keyboard()
    keyboard_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(__get_status_text(), reply_markup=keyboard_markup)
    return states.MAIN_STATE


def __get_status_text() -> str:
    # TODO: соформировать текст статуса
    return 'Статус'


def __get_keyboard() -> List[List[str]]:
    def __get_device_type_buttons(device_type):
        devices = garden.get_devices_by_type(device_type)
        opened_devices = [a for a in devices if a.state == hardware.switchStates.OPENED]
        closed_devices = [a for a in devices if a.state == hardware.switchStates.CLOSED]
        return [f'Закрыть {a.id}' for a in opened_devices] + [f'Открыть {a.id}' for a in closed_devices]

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
