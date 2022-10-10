import telebot
import requests
from random import randint
from telebot import types
from requests.models import Response

import config

bot = telebot.TeleBot(token=config.TOKEN)
@bot.callback_query_handler(func= lambda call:True)
def vtn_handl(call: telebot.types.CallbackQuery):
    if str(call.data =="B_1"):
        Animes(call.message)


@bot.message_handler(commands=["help"])
def helps(message:telebot.types.Message):
    bot.send_message(message.chat.id  , "Команды:\n/start\n/help")

@bot.message_handler(commands=["start"])
def start(message:telebot.types.Message):
    bot.send_message(message.chat.id ,"Приветствуем вас на наешм телеграм боте вы можете:\n1.Посмотреть наше аниме командой: /anime")


@bot.message_handler(commands = ["anime"])
def anime(message:telebot.types.Message):
    markup = types.InlineKeyboardMarkup()
    buttom1 = types.InlineKeyboardButton("Список аниме" , callback_data="B_1")
    markup.row(buttom1)
    bot.send_message(message.chat.id ,"нажми" ,  reply_markup=markup)


def Animes(message:telebot.types.Message):
    for i in config.data:
        bot.send_photo(message.chat.id,photo = i.get('animeImg'))
        bot.send_message(message.chat.id ,f"{i.get('animeTitle')}")
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='Наш сайт', url=i.get('episodeUrl'))
        markup.add(btn_my_site)
        bot.send_message(message.   chat.id, "перейди на  сайт чтобы посмотреть серию.", reply_markup = markup)
@bot.message_handler()
def Noni(message:telebot.types.Message):
    bot.send_message(message.chat.id ,"/help")
bot.polling(non_stop = True)