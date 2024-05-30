"""
Utilities module
"""

import logging
from logging.handlers import RotatingFileHandler


def configure_logging(file_path='logs/logs.log', level=logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(level)

    file_handler = RotatingFileHandler(file_path, maxBytes=100000, backupCount=10)
    file_handler.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    # stream_handler = logging.StreamHandler()
    # stream_handler.setLevel(level)
    # stream_handler.setFormatter(formatter)
    # logger.addHandler(stream_handler)

    return logger
