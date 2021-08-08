import inspect
import logging


def customlogger(loglevel=logging.INFO):
    # This method is for logging message in test steps
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler("testlogs.txt", mode='w')
    fileHandler.setLevel(loglevel)
    formatter = logging.Formatter('%(asctime)s -%(name)s -%(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
