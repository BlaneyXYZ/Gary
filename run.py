#!/usr/bin/env python
import os
import sys
import logging
import logging.config
import time

from gary.bot import Bot


def main():
    kw = {
        'format': '[%(asctime)s] %(message)s',
        'datefmt': '%m/%d/%Y %H:%M:%S',
        'level': logging.DEBUG, #TODO config for debug
        'stream': sys.stdout,
    }
    logging.basicConfig(**kw)
    logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)
    bot = Bot()
    bot.run()

if __name__ == '__main__':
    main()