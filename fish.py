import logging
import os
from datetime import datetime

from phue import Bridge
import schedule
import time

logging.basicConfig(level=logging.INFO)


def add_offset_to_time(time, offset):
    hours = time.split(":")[0]
    time_with_offset = int(hours) + int(offset)
    return f"{time_with_offset}:00"


on_time = os.getenv('ON_TIME')
on_duration = os.getenv('ON_DURATION')
off_time = add_offset_to_time(on_time, on_duration)

co2 = os.getenv('CO2_SOCKET')
bridge_ip = os.getenv('BRIDGE_IP')

logging.info(f"On duration is   : {on_duration} hours")
logging.info(f"CO2 on time      : {on_time}")
logging.info(f"CO2 off time     : {off_time}")
logging.info(f"CO2 socket       : {co2}")
logging.info(f"Bridge IP        : {bridge_ip}")

b = Bridge(bridge_ip)
b.connect()


def co2_on():
    current_time = datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
    b.set_light(light_id=int(co2), parameter='on', value=True)
    logging.info(f"{current_time}, Switching On CO2 {co2}")


def co2_off():
    current_time = datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
    b.set_light(light_id=int(co2), parameter='on', value=False)
    logging.info(f"{current_time}, Switching Off CO2 {co2}")


def log_message():
    co2_status = b.get_light(int(co2))["state"]["on"]

    current_time = datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
    if co2_status:
        logging.info(f"{current_time}, CO2 is On")
    else:
        logging.info(f"{current_time}, CO2 is Off")


log_message()
schedule.every().day.at(on_time).do(co2_on)
schedule.every().day.at(off_time).do(co2_off)

schedule.every(15).minutes.do(log_message)

while True:
    schedule.run_pending()
    time.sleep(1)
