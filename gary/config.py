# -*- coding: utf-8 -*-

import os
import json
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