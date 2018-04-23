from logging import getLogger, DEBUG, INFO, WARNING, ERROR, StreamHandler

logger = getLogger('env')
logger.setLevel(WARNING)
logger.addHandler(StreamHandler())
