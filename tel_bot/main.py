import telebot
import requests
from googletrans import Translator
import random


bot = telebot.TeleBot('5109539992:AAEbvVJlCCZb7Ooqr0B52LgkgaPAXy7vVL4')
compliments_api = "https://complimentr.com/api"
own_chat = 1058477695
her_chat = 1276335073
hearts = "❤🧡💛💚💜💙🤍"


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} '
    bot.send_message(message.chat.id, mess)


def get_compliment():
    res = requests.get("https://complimentr.com/api").json()['compliment']
    translator = Translator()
    compliment = translator.translate(res, dest='kk', src='en').text
    compliment = compliment + hearts[random.randint(0, 6)]
    return compliment


@bot.message_handler()
def get_user_text(message):

    if message.chat.id == her_chat:
        compliment = get_compliment()
        bot.send_message(her_chat, compliment)
        bot.send_message(own_chat, f'Она написала: {message.text} \n {compliment}')

    if 'send ' in message.text:
        my_mess = message.text.split('send ')[1]
        bot.send_message(her_chat, my_mess)


bot.polling(none_stop=True)
