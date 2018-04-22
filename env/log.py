from logging import getLogger, DEBUG, INFO, WARNING, ERROR, StreamHandler

logger = getLogger('env')
logger.setLevel(DEBUG)
logger.addHandler(StreamHandler())
