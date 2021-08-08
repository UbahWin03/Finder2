import requests
from bs4 import BeautifulSoup
from telebot import *
from config import token

bot = telebot.TeleBot(token)

def makarovka(snils, mess):
    fl = True
    count = 0
    soup = BeautifulSoup(requests.get('https://gumrf.ru/reserve/abitur/hod/?type=111').text, 'html.parser')
    tables = soup.find('table', {'class': 'table'})
    napr = soup.find('summary', {'style': ' cursor: pointer;'})

    for i in range(6, 751):
        table = tables.findAll('tr')[i].find_all('td')
        if table[8].text == 'Да' and fl:
            count += 1
        if table[1].text == snils:
            fl = False
            m = [table[i].text for i in range(len(table))]
            bot.send_message(mess.chat.id, napr.text + '\n' + "место: " + str(m[0]) + '\n' + "общий балл: " + str(m[2]) + '\n' + "есть ли согласие: " + str(m[-3]) + '\n' + "согласие на другом направлении: " + str(m[-2]) + '\n' + 'мое место по согласиям: ' + str(count))

    if fl:
    	bot.send_message(mess.chat.id, 'нет такого снилса')

@bot.message_handler(commands=['start'])
def start(mess):
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #для будущих вузов
    # knopka1 = types.KeyboardButton('1')
    # knopka2 = types.KeyboardButton('2')
    # markup.add(knopka1,knopka2)
    bot.send_message(mess.chat.id, 'Привет, введи снилс')

@bot.message_handler(content_types=['text'])
def main(mess):
    makarovka(str(mess.text), mess)

bot.polling(none_stop=True)


