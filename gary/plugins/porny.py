from gary.bot import respond_to
from gary.util import http
import requests
import json
import html

@respond_to('porny$')
def porny_random(message):
    "returns a random Porny comment"

    request = http.get_json("http://alfred.blny.me:5000/api/random")
    id = request["id"]
    comment = request["comment"]
    message.reply(comment)

@respond_to('porny (.*)')
def porny_comment(message, text):
    "(id) returns a specfic Porny comment"
    if text.isdigit():
        request = http.get_json("http://alfred.blny.me:5000/api/comment/{}".format(text.replace(" ", "+")))
        id = request["id"]
        comment = request["comment"]
        message.reply(comment)
    else:
        message.reply("Please enter a valid comment ID")
