import logging
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def set_pin_value(pin, value):
    logging.debug(f'Пин #{pin} <- {value}')
    gpio_value = GPIO.HIGH if bool(value) else GPIO.LOW
    GPIO.output(int(pin), gpio_value)
    pass

def setup_pin_out(pin):
    GPIO.setup(int(pin), GPIO.OUT)
    pass

# def setup_pin_in(pin):
#     # GPIO.setup(int(pin), GPIO.IN)
#     pass