from gary.bot import respond_to
from gary.util import http

@respond_to('porny$')
def porny_random(message):
    """porny - returns a random porny comment"""
    request = http.get_json("http://alfred.cloud.blny.me:5000/api/random")
    id = request["id"]
    comment = request["comment"]
    message.reply("{} (ID:{})".format(comment, id))

@respond_to('porny (.*)')
def porny_comment(message, text):
    """porny (id) - returns a specific porny comment"""
    if text.isdigit():
        request = http.get_json("http://alfred.cloud.blny.me:5000/api/comment/{}".format(text.replace(" ", "+")))
        id = request["id"]
        source = request["source"]
        comment = request["comment"]
        message.reply("{} - {}".format(comment,source))
    else:
        message.reply("Please enter a valid comment ID")
