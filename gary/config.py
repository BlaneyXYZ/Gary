# -*- coding: utf-8 -*-
import logging
import os
import json
import sys
import time

if not os.path.exists("config.json"):
    # if there is no config, show an error and die
    logging.critical("No config file found, bot shutting down!")
    print("No config file found! Bot shutting down in five seconds.")
    print("Copy 'config-default.json' to 'config.json' for defaults.")
    time.sleep(5)
    sys.exit()
DEBUG = False

PLUGINS = [
    'gary.plugins',
]

ERRORS_TO = None

CONFIG_FILE = json.loads(open("./config.json").read())

ALIASES = '~'

HELP_COMANND = "help"

DEFAULT_REPLY = "Not sure what you mean. Try *{}*.".format(HELP_COMANND)


try:
    from slackbot_settings import *
except ImportError:
    try:
        from local_settings import *
    except ImportError:
        pass