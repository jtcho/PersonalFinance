import yaml

from jt.util import logger

CONF_DIR = 'conf/'
CONF_SUFFIX = '.yaml'

def read_conf(service_name):
    conf = None
    with open(CONF_DIR+service_name+CONF_SUFFIX, 'r') as conf_stream:
        try:
            conf = yaml.load(conf_stream)
        except yaml.YAMLError as exc:
            logger.error(exc.message)
    return Config(conf)

class Config(object):
    """ Simple container object for YAML config files. """

    def __init__(self, config):
        if config is None:
            return
        for key in config:
            self.__setattr__(key, config[key])
