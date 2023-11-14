import logging
import os
from datetime import datetime

from phue import Bridge
import schedule
import time

logging.basicConfig(level=logging.INFO)

bridge_ip = os.getenv('BRIDGE_IP')
group = os.getenv('GROUP_NAME')

logging.info(f" Bridge IP        : {bridge_ip}")
logging.info(f" Group Name       : {group}")

b = Bridge(bridge_ip)
b.connect()


def sofa_off():
    current_time = datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
    b.set_group(group, 'on', False)
    logging.info(f" Current time is {current_time} Switching Off {group}")


def log_message():
    current_time = datetime.now().strftime("%Y/%m/%d - %H:%M:%S")

    group_status =b.get_group("Sofa")["state"]["any_on"]

    if group_status:
        logging.info(f" Current time is {current_time}, Group {group} is On")
    else:
        logging.info(f" Current time is {current_time}, Group {group} is Off")


log_message()
schedule.every().day.at("02:00").do(sofa_off)
schedule.every().day.at("03:00").do(sofa_off)
schedule.every().day.at("04:00").do(sofa_off)
schedule.every().day.at("05:00").do(sofa_off)
schedule.every(15).minutes.do(log_message)

while True:
    schedule.run_pending()
    time.sleep(1)
