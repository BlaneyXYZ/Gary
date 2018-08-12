# coding: UTF-8
import random
import re
from gary.bot import respond_to
from gary.bot import listen_to


@respond_to('palindrome (.*)')
def palindrome(message, text):
    """palindrome (text) - checks if text is a palindrome"""
    string = text.lower()
    if string == string[::-1]:
        message.reply("{} is a palindrome".format(string))
    else:
        message.reply("{} is not a palindrome".format(string))


@respond_to('piglatin (.*)')
def piglatin(message, text):
    """piglatin (text) - returns word in pig latin format"""
    word = text.lower()
    vowels = 'aeiou'
    pig = 'ay'
    first = word[0]
    if first in vowels:
        newword = word + pig
    else:
        newword = word[1:] + first + pig
    message.reply("{} becomes {}".format(word, newword))


@listen_to('database', re.IGNORECASE)
@listen_to('mysql', re.IGNORECASE)
def databasepig(message):
    num = random.randint(0, 10)
    if num >= 5:
        message.reply("fuck off you gimp")
    elif num >= 10:
        message.reply("confirmed your a fuckpig")
    else:
        message.reply("just because you love to be fisted by ten database engineers")


@listen_to('pepe')
def pepe(message):
    message.react('pepe')


@listen_to('cloud')
def cloud(message):
    message.react('cloud')


@respond_to('fuck', re.IGNORECASE)
def fuck(message):
    """fuck - responds to user's how rude!"""
    message.reply('Fuck you!')
