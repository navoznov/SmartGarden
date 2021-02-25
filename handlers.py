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


def open_window_handler(update: Update, context: CallbackContext) -> int:
    match = re.match(r'Открыть (.+)', update.message.text)
    actuator_id = match.group(1)
    actuator = garden.get_device_by_id(actuator_id)

    message = update.message
    text = f'{actuator.name} открывается. Подождите {actuator.open_close_timeout_in_sec} секунд.'
    message.reply_text(text)

    actuator.open()

    message.reply_text(f'{actuator.name} открыт')
    reply_keyboard = __get_keyboard()
    keyboard_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    message.reply_text(__get_status_text(), reply_markup=keyboard_markup)
    return states.MAIN_STATE


def close_window_handler(update: Update, context: CallbackContext) -> int:
    match = re.match(r'Закрыть (.+)', update.message.text)
    actuator_id = match.group(1)
    actuator = garden.get_device_by_id(actuator_id)

    text = f'{actuator.name} закрывается. Подождите {actuator.open_close_timeout_in_sec} секунд.'
    update.message.reply_text(text)

    actuator.open()

    update.message.reply_text(f'{actuator.name} закрыт')
    reply_keyboard = __get_keyboard()
    keyboard_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(__get_status_text(), reply_markup=keyboard_markup)
    return states.MAIN_STATE


def __get_status_text() -> str:

    return 'Статус'


def __get_keyboard() -> List[List[str]]:
    # окна
    actuator_buttons = []
    actuators = garden.get_devices_by_type(hardware.deviceTypes.LINEAR_ACTUATOR)
    opened_actuators = [a for a in actuators if a.state == hardware.switchStates.OPENED]
    actuator_buttons = actuator_buttons + [f'Закрыть {a.id}' for a in opened_actuators]
    closed_actuators = [a for a in actuators if a.state == hardware.switchStates.CLOSED]
    actuator_buttons = actuator_buttons + [f'Открыть {a.id}' for a in closed_actuators]
    buttons.append(actuator_buttons)

    if len(actuators) == len(opened_actuators):
        buttons.append(buttonTitles.CLOSE_BOTH_WINDOW_BUTTON)

    if len(actuators) == len(closed_actuators):
        buttons.append(buttonTitles.OPEN_BOTH_WINDOW_BUTTON)

    # краны
    valve_buttons = []
    valves = garden.get_devices_by_type(hardware.deviceTypes.VALVE)
    opened_valves = [a for a in valves if a.state == hardware.switchStates.OPENED]
    valve_buttons = valve_buttons + [f'Закрыть {a.id}' for a in opened_valves]
    closed_valves = [a for a in valves if a.state == hardware.switchStates.CLOSED]
    valve_buttons = valve_buttons + [f'Открыть {a.id}' for a in closed_valves]
    buttons.append(actuator_buttons)



    return [[b] for b in buttons]
