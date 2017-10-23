from rx import Observer
from jt.util import logger

class ListCollector(Observer):
    """ Aggregates the items streamed from an observable into a list. """

    def __init__(self):
        self.results = []

    def on_next(self, value):
        self.results += [value]

    def on_completed(self):
        logger.info('Collected all emissions.')

    def on_error(self, error):
        logger.error('Error occurred while consuming value with message: ' + error.message)

