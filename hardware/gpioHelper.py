# import onionGpio
import logging
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def set_pin_value(pin, value):
    logging.debug(f'Пин №{pin} <- {value}')
    # onionGpio.OnionGpio.setValue()
    GPIO.output(int(pin), value)
    pass

def setup_pin_out(pin):
    GPIO.setup(int(pin), GPIO.OUT)
    pass

def setup_pin_in(pin):
    GPIO.setup(int(pin), GPIO.IN)
    pass