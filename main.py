import requests
from bs4 import BeautifulSoup
from telebot import *
from config import token

bot = telebot.TeleBot(token)

def makarovka(snils, mess):
    m = []
    fl = True
    soup = BeautifulSoup(requests.get('https://gumrf.ru/reserve/abitur/hod/?type=111').text, 'html.parser')
    tables = soup.find('table', {'class': 'table'})
    for i in range(6, 751):
        table = tables.findAll('tr')[i].find_all('td')
        if table[1].text == snils:
            fl = False
            m = [table[i].text for i in range(len(table))]
            bot.send_message(mess.chat.id, "место: " + str(m[0]))
            bot.send_message(mess.chat.id, "общий балл: " + str(m[2]))
            bot.send_message(mess.chat.id, "есть ли согласие: " + str(m[-3]))
            bot.send_message(mess.chat.id, "согласие на другом направлении: " + str(m[-2]))
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


