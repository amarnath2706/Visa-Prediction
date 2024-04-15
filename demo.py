from visa_prediction.logger import logging
from visa_prediction.exception import visaException
import sys


logging.info('Welcome to our custom log')

try:
    a = 20/"2"

except Exception as e:
    logging.info(e)
    raise visaException(e, sys) from e