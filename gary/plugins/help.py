import re
from gary.bot import respond_to


@respond_to('help', re.IGNORECASE)
def help(message):
    """help - returns commands the bot knows"""
    message.direct_reply('I currently know!:')
    message.direct_reply(message.docs_reply())
