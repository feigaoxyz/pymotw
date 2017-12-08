import logging
import logging.handlers
import glob


LOG_FILE = 'logging_rotatingfile_example.out'

# set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')  # type: logging.Logger
my_logger.setLevel(logging.DEBUG)

# add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
    LOG_FILE,
    maxBytes=20,
    backupCount=5
)
my_logger.addHandler(handler)

# log some message
for i in range(20):
    my_logger.debug(f'i = {i}')

logfiles = glob.glob(f'{LOG_FILE}*')
for fn in logfiles:
    print(fn)
