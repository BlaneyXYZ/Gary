from gary.bot import respond_to
from gary.util import http


@respond_to('doge$')
def dogpic(message):
    """doge - receives a dog picture"""
    picture = http.get_json("https://dog.ceo/api/breeds/image/random")
    message.reply("{}".format(picture["message"]))

@respond_to('doge (.*)')
def dogpic(message, text):
    """doge - receives a dog picture"""
    picture = http.get_json('https://dog.ceo/api/breed/{}/images/random'.format(text))
    message.reply("{}".format(picture["message"]))
