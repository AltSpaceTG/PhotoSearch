import telebot
from bing_image_urls import bing_image_urls
import random
import traceback
import logging
from telebot import types

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,
                     "👋 Привет! Я твой бот-помошник! Отправь мне любое слово или предложение, а я поищу это фото в гугле!")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Сейчас найду!")
    atemps = 1
    while True:
        try:
            url = bing_image_urls(message.text, limit=100)[random.randint(0, 99)]
            bot.send_photo(chat_id=message.from_user.id,
                           photo=url,
                           caption="Надеюсь это то что ты искал;)")
            print(f"нашел за {atemps} попыток")
            atemps=1
            break
        except Exception:
            atemps+=1


bot.polling(none_stop=True, interval=0)
