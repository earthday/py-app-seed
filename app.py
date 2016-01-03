#!/usr/bin/env python

import os
import logging.config
import codecs
import yaml
import ConfigParser
import sys
import time

cfg = ConfigParser.ConfigParser()
current_folder = os.path.dirname(os.path.realpath(__file__))

# config the logging
logging_config_filename = os.path.join(current_folder, 'config', 'logging.yaml')
logging.config.dictConfig(yaml.load(codecs.open(logging_config_filename, 'r', 'utf-8')))
#logging.Formatter.converter = time.localtime # (Default) LocalTime
#logging.Formatter.converter = time.gmtime # GMT
logger = logging.getLogger('commonLog')

if __name__ == "__main__":
    logger.info('App is running...')
