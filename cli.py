__title__ = "JokerDynDNS"
__author__ = "Paulo Antunes"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "MIT"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"
__version__ = "0.1.0"

import logging
import schedule
import time
import requests
import settings as s
from environs import Env


logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


env = Env()
env.read_env()


def job():
    for h in env.list('DOMAINS'):
        k = h.split('.')[-2]
        with env.prefixed(k):
            response = requests.get(
                s.URL.format(
                    username=env('.username'),
                    password=env('.password'),
                    hostname=h
                )
            )
            logger.info(response.text)


schedule.every(s.INTERVAL_IN_MINUTES).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
