# Set encoding like 'charset' in HTML

# -*- coding: utf-8 -*-

# Import external files/classes

import config
import random
import requests
#import xml.etree.ElementTree as etree
import telebot
import botan # class for bot metrics
from telebot import types


# Set global variables

# Set main working instance of TeleBot class
bot = telebot.TeleBot(config.token)

# In this example we're creating an array of random phrases
phrases = ['You talkin to me?', 'You talkin to me?', 'You talkin to me?', 'Well then who the hell else are you talkin’ to?', 'You talkin’ to me?', 'Well I’m the only one here. Who the fuck do you think you’re talkin’ to?', 'Oh yea? Huh?', 'Okay. Huh?']


# Command handler: reply and send photo

@bot.message_handler(commands=['start'])
def send_welcome(message):
    photo = open('tmp/photo.png', 'rb')
    bot.reply_to(message, phrases[random.randint(0, 7)])
    bot.send_photo(message.chat.id, photo)


# Get metrics

# @bot.message_handler(commands=['metrics'])
# def send_welcome(message):
#     # Start metrics
#     uid = message.from_user
#     # message_dict = message.to_dict()
#     # event_name = update.message.text
#     print(botan.track(config.botan_token, uid, message, 'Message'))
#     original_url = 'http://yandex.ru' # some url you want to send to user
#     short_url = botan.shorten_url(original_url, config.botan_token, uid)
#     bot.send_message(message.chat.id, short_url)

# Display custom 'keyboard'

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

# Making a request to external API

@bot.message_handler(commands=['request'])
def make_request(message):
    r = requests.get('https://export.yandex.ru/weather-ng/forecasts/27612.xml')
    #r = requests.get('https://api.github.com/events')
    #print(r.text)
    bot.send_message(message.chat.id, r.encoding)

# Command handling with a reply message

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "What do you want?")

# Handling attachement files sent by user

@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    #pass
    bot.reply_to(message, "Why are you showing this to me?")

# Simple conditions in user message parser

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
