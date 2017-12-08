import logging


logging.basicConfig(level=logging.WARNING)

logger1 = logging.getLogger('pkg1.module1')
logger2 = logging.getLogger('pkg1.module2')

logger1.warning('This comes from one module')
logger2.warning('This comes from another module')
