# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)
phrases = ['You talkin to me?', 'You talkin to me?', 'You talkin to me?', 'Well then who the hell else are you talkin’ to?', 'You talkin’ to me?', 'Well I’m the only one here. Who the fuck do you think you’re talkin’ to?', 'Oh yea? Huh?', 'Okay. Huh?']

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Are you talking to me?")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "What do you want?")

@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    #pass
    bot.reply_to(message, "Why are you showing this to me?")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
     bot.polling(none_stop=True)
