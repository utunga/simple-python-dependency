import logging

logger = logging.getLogger(__name__)

class SimpleDependency(object):

    def __init__(self):
        pass

    def do_a_thing(self):
        logger.info("doing a thing")
