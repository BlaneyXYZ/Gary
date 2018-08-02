from gary.bot import respond_to
from gary.util import http


# https://raw.githubusercontent.com/AwesomePowered/CloudBot/b7ee83746eca892a62d39c7bc1b86bc91138849f/plugins/giphy.py
@respond_to('gif$')
def gif_random(message):
    """returns a random gif """
    gif = http.get_json("http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&rating=r")
    gif_url = "http://i.giphy.com/" + gif["data"]["id"] + ".gif"
    message.reply("Have a gif you stupid muppet! {} ".format(gif_url))


@respond_to('gif (.*)')
def gif_tag(message, text):
    """(tag) returns a gif based on the tag"""
    gif = http.get_json("http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag={}&rating=r".format(text.replace(" ", "+")))
    gif_url = "http://i.giphy.com/" + gif["data"]["id"] + ".gif"
    message.reply("Have a gif you stupid muppet! {} ".format(gif_url))
