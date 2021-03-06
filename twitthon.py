import sys
import logging
import src.consumers as consumers
from src import variables

debug_level = variables.debug_level

if debug_level == "DEBUG":
    logging.basicConfig(level=logging.DEBUG)
elif debug_level == "INFO":
    logging.basicConfig(level=logging.INFO)
elif debug_level == "WARNING":
    logging.basicConfig(level=logging.WARNING)
elif debug_level == "ERROR":
    logging.basicConfig(level=logging.ERROR)
elif debug_level == "CRITICAL":
    logging.basicConfig(level=logging.CRITICAL)


if __name__ == '__main__':
    tasks = [
        consumers.Consumer()
    ]
    #lancement du thread de consomation du topic
    for t in tasks:
        t.start()

