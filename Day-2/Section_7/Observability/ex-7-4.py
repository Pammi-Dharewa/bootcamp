import os

DEBUG = os.getenv('DEBUG', 'False') == 'True'

def log_with_verbosity(message):
    if DEBUG:
        logging.debug(message)
    else:
        logging.info(message)

log_with_verbosity("This is a debug log")
