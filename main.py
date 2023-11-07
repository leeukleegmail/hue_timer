import datetime
import logging
import os

from phue import Bridge
import schedule
import time

logging.basicConfig(level=logging.INFO)

light_on_time = os.getenv('LIGHT_ON_TIME')
light_off_time = os.getenv('LIGHT_OFF_TIME')
co2_on_time = os.getenv('CO2_ON_TIME')
co2_off_time = os.getenv('CO2_OFF_TIME')
light = os.getenv('LIGHT_SOCKET')
co2 = os.getenv('CO2_SOCKET')
bridge_ip = os.getenv('BRIDGE_IP')

logging.info(f" Light On Time is {light_on_time}")
logging.info(f" Light Off Time is {light_off_time}")
logging.info(f" CO2 On Time is {co2_on_time}")
logging.info(f" CO2 Off Time is {co2_off_time}")
logging.info(f" Light socket is {light}")
logging.info(f" CO2 socket is {co2}")
logging.info(f" Bridge IP address is {bridge_ip}")

b = Bridge(bridge_ip)
b.connect()


def light_on():
    b.set_light(light_id=int(light), parameter='on', value=True)
    logging.info(f" Switching On Light {light}")


def co2_on():
    b.set_light(light_id=int(co2), parameter='on', value=True)
    logging.info(f" Switching On CO2 {co2}")


def light_off():
    b.set_light(light_id=int(light), parameter='on', value=False)
    logging.info(f" Switching Off Light {light}")


def co2_off():
    b.set_light(light_id=int(light), parameter='on', value=False)
    logging.info(f" Switching Off CO2 {co2}")


def log_message():
    from datetime import datetime
    light_status = b.get_light(int(light))["state"]["on"]
    co2_status = b.get_light(int(co2))["state"]["on"]

    current_time = datetime.now().strftime("%YYYY-%MM-%DD - %H:%M:%S")
    if light_status:
        logging.info(f"Current time is {current_time}, Fish Light is On")
    else:
        logging.info(f"Current time is {current_time}, Fish Light is Off")
    if co2_status:
        logging.info(f"Current time is {current_time}, Fish CO2 is On")
    else:
        logging.info(f"Current time is {current_time}, Fish CO2 is Off")


schedule.every().day.at(light_on_time).do(light_on)
schedule.every().day.at(light_off_time).do(light_off)
schedule.every().day.at(co2_on_time).do(co2_on)
schedule.every().day.at(co2_off_time).do(co2_off)
schedule.every(15).minutes.do(log_message)

while True:
    schedule.run_pending()
    time.sleep(1)
