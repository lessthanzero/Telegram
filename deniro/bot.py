# -*- coding: utf-8 -*-
import config
import random
import requests
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)
phrases = ['You talkin to me?', 'You talkin to me?', 'You talkin to me?', 'Well then who the hell else are you talkin’ to?', 'You talkin’ to me?', 'Well I’m the only one here. Who the fuck do you think you’re talkin’ to?', 'Oh yea? Huh?', 'Okay. Huh?']

@bot.message_handler(commands=['start'])
def send_welcome(message):
    photo = open('tmp/photo.png', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, phrases[random.randint(0, 7)])

@bot.message_handler(commands=['keyboard'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('a')
    itembtnv = types.KeyboardButton('b')
    itembtnc = types.KeyboardButton('c')
    itembtnd = types.KeyboardButton('d')
    itembtne = types.KeyboardButton('🚕')
    markup.row(itembtna, itembtnv)
    markup.row(itembtnc, itembtnd, itembtne)
    bot.send_message(message.chat.id, "Choose something:", reply_markup=markup)

@bot.message_handler(commands=['request'])
def make_request(message):
    r = requests.get('https://api.github.com/events')
    bot.send_message(message.chat.id, r.encoding)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "What do you want?")

@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    #pass
    bot.reply_to(message, "Why are you showing this to me?")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    #bot.send_message(message.chat.id, message.text)

    if message.text == "a":
        types.ReplyKeyboardHide()
        bot.send_message(message.chat.id, "You've typed 'a' on virtual keyboard")
    else:
        bot.reply_to(message, phrases[random.randint(0, 7)])


if __name__ == '__main__':
     bot.polling(none_stop=True)
