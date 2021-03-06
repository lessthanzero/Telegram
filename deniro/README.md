# Creating bots in Telegram, Slack, Facebook Messenger

# Part I

## Telegram Bots API:

https://core.telegram.org/bots


## Slack Bots API:

https://api.slack.com/bot-users



## Facebook Messenger bots:

https://developers.facebook.com/docs/messenger-platform



## Tutorials:

https://habrahabr.ru/post/281559/ — creating bot for Facebook Messenger (in-depth)

https://vc.ru/p/bot-facebook — creating Facebook bot (easier)

https://medium.com/chatfuel-blog/how-to-create-an-automated-bot-on-telegram-without-coding-using-zapier-and-paquebot-5a635a3b867b#.mxf6hyali — creating Telegram bot with Zapier

https://medium.com/@rssilva/talking-with-arduino-using-telegram-and-javascript-d874a0b560cb#.sd85bhnvf — Telegram bot + Arduino

https://medium.com/@allenleein/18-best-tools-for-bot-development-eb083f5894b5#.d3j239ifo — a selection of tools and tutorials



## Tools:

https://botlist.co — a curated list of bots
https://bots.mockuuups.com — bot mockups
https://dev.kik.com/#/home — Kik messenger bot platform



## Media and Businesses:

https://chatfuel.com — bots platform startup

https://medium.com/chatfuel-blog — articles from ChatFuel

https://medium.com/meduza-dev/алан-телеграм-бот-медузы-или-еще-немного-об-elixir-dfbed7a55c18#.mcoxq81an — about Meduza’s bot

https://medium.com/@sevazhidkov/leonard-bot-open-source-virtual-assistant-in-messengers-by-russian-school-students-e2b5d1aac9a5#.xgfdoapzq — Seva Zhidkov on his own open-source bot creation

http://dangrover.com/blog/2014/12/01/chinese-mobile-app-ui-trends.html — case study of mobile trends coming from China, pt. 1

http://dangrover.com/blog/2016/01/31/more-chinese-mobile-ui-trends.html — pt. 2 of Chinese mobile trends study

http://dangrover.com/blog/2016/04/20/bots-wont-replace-apps.html — about bots

http://www.engadget.com/2016/04/13/here-are-all-the-facebook-messenger-bots-we-know-about-so-far/ — a list of Facebook bots

Miscellaneous:
https://medium.com/art-marketing/the-hidden-homescreen-70c794ff9ada#.7r7kog77g
https://medium.com/chris-messina/sorry-to-burst-your-chat-bubble-ae4dc6952447#.dx86zkrq1
http://www.bloomberg.com/news/articles/2016-04-18/the-humans-hiding-behind-the-chatbots
http://alistapart.com/article/all-talk-and-no-buttons-the-conversational-ui
http://alistapart.com/article/designing-the-conversational-ui

https://itunes.apple.com/us/app/quartz-news-in-a-whole-new-way/id1076683233?mt=8 — new way of consuming news
http://azumbrunnen.me — personal site emulating chat room


## Telegram bots:

https://telegram.me/sapsanasapbot — Sapsan ticket search
http://telegram.me/meduzaprobot — meduza.io
http://telegram.me/nplusone_bot — N+1

http://telegram.me/weatherman_bot — weather bot
http://telegram.me/delorean_bot — reminders
http://telegram.me/PronunciationBot — text to voice
http://telegram.me/Hotelrobot — book hotels
http://telegram.me/YTranslateBot — Yandex Translator  


# Pre-requisites for part II  

- Code editor of choice
- Token and set up bot from [BotFather](http://telegram.me/BotFather)
- Installed [Homebrew](http://brew.sh) (on Mac)
- Installed python3: `brew install python3`
- Installed pytelegrambotapi: `pip3 install pytelegrambotapi`
- Account in [Heroku](https://www.heroku.com/) or access to personal server with Python 3 support


# Part II

## Connecting to external APIs



## Bot analytics

1. http://botan.io/#botan_steps
2. https://github.com/botanio/sdk


## Uploading to server


### Personal hosting

1. Upload files to your hosting (It should support programming language of choice. In our case it's _Python_).
2. Check if necessary modules (i. e. _pytelegrambotapi_) installed or could be installed via tech support.
3. Check if bot works.
4. If it's not, double-check if it works from your computer.

### Working with Heroku (more here: http://gnclmorais.com/blog/deploy-your-python-bot-to-heroku/)

1. Log in to [Heroku](https://heroku.com)
2. Create new app and give it a clear name
3. Select "Deploy" tab
4. Select Dropbox, connect your Dropbox account
5. Place your code and necessary files in `Dropbox/Apps/Heroku/[name of your Heroku app]`
6. Specify `heroku/python` buildpack in app "Settings" tab
7. Go back to "Deploy" and click "Deploy" button

## Creating bots with Codenvy

1. Test your bot locally
2. If it works, make a zip file of your bot project directory. Remember not to include your config with tokens into archive
3. Create account at [Codenvy](https://codenvy.com/)
4. Create project from zip (put your zip file into public cloud, i. e. Dropbox). Make it private.
5. Open project in IDE
6. Create file `requirements.txt` in root. Include pip packages names into it — each on a separate line.\n
For example: \n
`request \n
python-telegram-bot`
7. Rename your main running file (here, `deniro.py` OR `bot.py`) to `main.py`
8. In bottom left corner select `Runners — Config` and select either `Python3.4` or `Python2.7` depending on what version you used in your main running file.
