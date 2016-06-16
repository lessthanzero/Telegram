# -*- coding: utf-8 -*-

# Import external files/classes

import config
import random
import requests
import json
import telebot
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

# Making a request to external API (weather service in our case)

@bot.message_handler(commands=['weather'])
def make_request(message):
    r = requests.get('http://api.openweathermap.org/data/2.5/forecast/city?q=Moscow,ru&APPID='+config.openweather_token+'')
    weather = r.json()['list'][0]['weather'][0]['main']
    print(weather)
    bot.send_message(message.chat.id, weather)

# Command handling with a reply message

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "What do you want?")

# Handling attachement files sent by user

@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
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
