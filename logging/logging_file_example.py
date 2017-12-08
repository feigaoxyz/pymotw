# logging_file_example.py

import logging


LOG_FILENAME = 'logging_example.out'
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG
)

logging.debug('This message should go to the log file')

with open(LOG_FILENAME, 'rt') as fp:
    body = fp.read()

print('FILE:\n', body)
