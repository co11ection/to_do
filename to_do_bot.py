import telebot
from decouple import config


bot = telebot.TeleBot(config('TOKEN'))
