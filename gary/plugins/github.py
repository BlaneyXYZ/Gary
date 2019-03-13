from gary.bot import respond_to
from gary.util import http

@app.route('/webhook', methods=['POST'])
def github_hook(message):
    """"""
    message.reply("this aint work")

