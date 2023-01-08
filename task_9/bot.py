# Добавить игру, реализованную ранее, с конфетами к боту.
# *' Условие игры: На столе лежит 117 конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

import telebot
from random import randint as rnd
from random import choice
from telebot import types
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5889432580:AAHILKQ-AExl-7YAlOYxImOClZXWFBurSt8')

candy = dict()
status = dict()
whos_move = dict()


def game_status(message):
    global status
    try:
        if status[message.chat.id] and 1 <= int(message.text) <= 28:
            return True
        else:
            return False
    except KeyError:
        status[message.chat.id] = False
        if status[message.chat.id] and 1 <= int(message.text) <= 28:
            return True
        else:
            return False


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Привет!')
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAEHK_9juqd7uvAw7rEBSldRMN4SLmYfOgACJwMAArVx2gYP9N7PoMXd7C0E')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('/Game_with_candy', 'Курс валюты')
    bot.send_message(message.chat.id,
                    'Выберите действие.', reply_markup=markup)

@bot.message_handler(commands=['Game_with_candy'])
def game(message):
    global candy, status, whos_move
    bot.send_message(message.chat.id,
                    'Привет, человечишка. \nСыграем в игру :)')
    candy[message.chat.id] = 117
    whos_move[message.chat.id] = choice(['User', 'Bot'])
    bot.send_message(message.chat.id, 
                    f'Начианет {whos_move[message.chat.id]}')
    status[message.chat.id] = True
    if whos_move[message.chat.id] == 'Bot':
        take = rnd(1, 28)
        candy[message.chat.id] -= take
        bot.send_message(message.chat.id,
                        f'Бот взял {take}\nОсталось конфет {candy[message.chat.id]}')
        whos_move[message.chat.id] = 'User'


@bot.message_handler(func=game_status)
def game(message):
    global candy, status, whos_move
    if whos_move[message.chat.id] == 'User':
        if candy[message.chat.id] > 28:
            bot.send_message(message.chat.id,
                            'Ходит User. \nВозьмите от 1 до 28 конфет')
            candy[message.chat.id] -= int(message.text)
            bot.send_message(message.chat.id,
                            f'Осталось конфет {candy[message.chat.id]}')
            if candy[message.chat.id] > 28:
                take = rnd(1, 28)
                candy[message.chat.id] -= take
                bot.send_message(message.chat.id,
                    f'Бот взял {take}\nОсталось конфет {candy[message.chat.id]}')
                if candy[message.chat.id] <= 28:
                    bot.send_message(message.chat.id, 'User win')
                    status[message.chat.id] = False
            else:
                bot.send_message(message.chat.id, 'Bot win')
                status[message.chat.id] = False
        else:
            bot.send_message(message.chat.id, 'Bot win')
            status[message.chat.id] = False


@bot.message_handler(content_types='text')
def course(message):
    if message.text == 'Курс валюты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('USD', 'EUR', '/start')
        bot.send_message(message.chat.id, 
                        'Выберите интересующую валюту', reply_markup=markup)   
    if message.text == 'USD':
        url = 'https://www.banki.ru/products/currency/usd/'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        mass = str(soup.find_all(class_='currency-table__large-text'))
        usd = mass[mass.find('text">')+6:mass.find('</div>'):]
        bot.send_message(message.chat.id, f'1 $ = {usd} ₽')

    elif message.text == 'EUR':
        url = 'https://www.banki.ru/products/currency/eur/'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        mass = str(soup.find_all(class_='currency-table__large-text'))
        eur = mass[mass.find('text">')+6:mass.find('</div>'):]
        bot.send_message(message.chat.id, f'1 € = {eur} ₽')


bot.infinity_polling(none_stop=True, interval=0)
