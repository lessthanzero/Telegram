# 1. Set encoding like 'charset' in HTML

# -*- coding: utf-8 -*-

# 2. Import external files/classes

import config
import random
import requests
#import xml.etree.ElementTree as etree
import telebot
from telebot import types

# 3. Set global variables

# 3.1 Set main working instance of TeleBot class
bot = telebot.TeleBot(config.token)

# 3.2 In this example we're creating an array of random phrases
phrases = ['You talkin to me?', 'You talkin to me?', 'You talkin to me?', 'Well then who the hell else are you talkin’ to?', 'You talkin’ to me?', 'Well I’m the only one here. Who the fuck do you think you’re talkin’ to?', 'Oh yea? Huh?', 'Okay. Huh?']

# 4. Command handler and photo sending

@bot.message_handler(commands=['start'])
def send_welcome(message):
    photo = open('tmp/photo.png', 'rb')
    bot.send_photo(message.chat.id, photo)

# 5. Command handler with reply to user

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, phrases[random.randint(0, 7)])

# 6. Display custom 'keyboard'

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

# 7. Making a request to external API

@bot.message_handler(commands=['request'])
def make_request(message):
    r = requests.get('https://export.yandex.ru/weather-ng/forecasts/27612.xml')
    #r = requests.get('https://api.github.com/events')
    #print(r.text)
    bot.send_message(message.chat.id, r.encoding)

# 8. Command handling with a reply message

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "What do you want?")

# 9. Handling attachement files sent by user

@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    #pass
    bot.reply_to(message, "Why are you showing this to me?")

# 10. Simple conditions in user message parser

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    #bot.send_message(message.chat.id, message.text)

    if message.text == "a":
        types.ReplyKeyboardHide()
        bot.send_message(message.chat.id, "You've typed 'a' on virtual keyboard")
    else:
        bot.reply_to(message, phrases[random.randint(0, 7)])

# Important! Start a bot loop (keep it 'alive')

bot.polling()
