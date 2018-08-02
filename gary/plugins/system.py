import re
from gary.bot import respond_to
from gary import bot
import os
import time
import platform
from datetime import timedelta

try:
    import psutil
except ImportError:
    psutil = None

@respond_to('about$', re.IGNORECASE)
def about(message):
    """returns basic information about the bot"""
    message.reply("{}, version {} run by {} - https://github.com/Mu5tank05/Gary".format(bot.name, bot.version, bot.owner))

@respond_to('system$', re.IGNORECASE)
def system(message):
    """-- Retrieves information about the host system."""

    # Get general system info
    sys_os = platform.platform()
    python_implementation = platform.python_implementation()
    python_version = platform.python_version()
    sys_architecture = '-'.join(platform.architecture())
    sys_cpu_count = platform.machine()

    message.reply(
        "OS: {}, Python: {} {}, Architecture: {} ({})" .format(sys_os, python_implementation, python_version, sys_architecture,  sys_cpu_count)
    )

    if psutil:
        process = psutil.Process(os.getpid())

        # get the data we need using the Process we got
        cpu_usage = process.cpu_percent()
        thread_count = process.num_threads()
        uptime = timedelta(seconds=round(time.time() - process.create_time()))

        message.reply("Uptime: {}, Threads: {}, CPU Usage: {}, " .format(uptime, thread_count, cpu_usage))