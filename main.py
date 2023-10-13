import logging
import os

from phue import Bridge
import schedule
import time

logging.basicConfig(level=logging.INFO)

on_time = os.getenv('ON_TIME')
off_time = os.getenv('OFF_TIME')
light_number = os.getenv('LIGHT_NUMBER')
bridge_ip = os.getenv('BRIDGE_IP')

logging.info(f" On Time is {on_time}")
logging.info(f" Off Time is {off_time}")
logging.info(f" Light number is {light_number}")
logging.info(f" Bridge IP address is {bridge_ip}")


b = Bridge(bridge_ip)
b.connect()


def light_on():
    b.set_light(light_id=int(light_number), parameter='on', value=True)
    logging.info(f" Switching On Light Number {light_number}")


def light_off():
    b.set_light(light_id=int(light_number), parameter='on', value=False)
    logging.info(f" Switching Off Light Number {light_number}")


def log_message():
    from datetime import datetime
    status = b.get_light(int(light_number))["state"]["on"]
    current_time = datetime.now().strftime("%H:%M:%S")
    if status:
        logging.info(f"Current time is {current_time}, Fish Light is On")
    else:
        logging.info(f"Current time is {current_time}, Fish Light is Off")


schedule.every().day.at(on_time).do(light_on)
schedule.every().day.at(off_time).do(light_off)
schedule.every(30).minutes.do(log_message)

while True:
    schedule.run_pending()
    time.sleep(1)
