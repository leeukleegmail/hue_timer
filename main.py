import logging
import os

from phue import Bridge
import schedule
import time

logging.basicConfig(level=logging.INFO)

on_time = os.getenv('ON_TIME')
off_time = os.getenv('OFF_TIME')
light_number = os.getenv('LIGHT_NUMBER')

logging.info(f" On Time is {on_time}")
logging.info(f" Off Time is {off_time}")
logging.info(f" Light number is {light_number}")

b = Bridge('192.168.1.10')
b.connect()


def light_on():
    b.set_light(light_id=int(light_number), parameter='on', value=True)
    logging.info(f" Switching On Light Number {light_number}")


def light_off():
    b.set_light(light_id=int(light_number), parameter='on', value=False)
    logging.info(f" Switching Off Light Number {light_number}")


schedule.every().day.at(on_time).do(light_on)
schedule.every().day.at(off_time).do(light_off)

while True:
    schedule.run_pending()
    time.sleep(1)
