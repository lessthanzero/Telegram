# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.

import config
import logging
import json
import telegram
import botan
from telegram.error import NetworkError, Unauthorized
from time import sleep


def main():
    # Telegram Bot Authorization Token
    bot = telegram.Bot(config.token)

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.getUpdates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            update_id = echo(bot, update_id)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot, update_id):

    # Request updates after the last update_id
    for update in bot.getUpdates(offset=update_id, timeout=10):
        # chat_id is required to reply to any message
        chat_id = update.message.chat_id
        update_id = update.update_id + 1
        text = update.message.text
        print update

        if text:

            botan_token = config.botan_token # Token got from @botaniobot
            uid = update.message.from_user.id
            message_dict = update.message.to_dict()
            event_name = update.message.text
            print uid
            original_url = 'http://yandex.ru' # some url you want to send to user
            short_url = botan.shorten_url(original_url, botan_token, uid)
            print short_url
            # # Reply to the message
            bot.sendMessage(chat_id=chat_id, text=short_url)

    return update_id


if __name__ == '__main__':
    main()
