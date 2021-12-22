import requests
import telebot
from telebot import types
from bs4 import BeautifulSoup


token = "2126640533:AAGA92YYddXzbklU6_6Z0Gin4GPwF69CfgU"
bot = telebot.TeleBot(token)


#Всё для статистики по коронавирусу
WOM_corona = requests.get("https://www.worldometers.info/coronavirus/")
corona = BeautifulSoup(WOM_corona.text, 'lxml')
amount = corona.find_all('div', class_='maincounter-number')
Coronavirus_Cases, Deaths, Recovered = [x.text for x in amount]


#Всё для погоды
pogoda = requests.get('https://weather.rambler.ru/v-moskve/now/')
weather = BeautifulSoup(pogoda.text, 'lxml')
degreece = weather.find_all('div', class_='_1HBR _3p4E')[0].text
Feels_like = weather.find_all('span', class_='_29Kw')[0].text


#Всё про про-игроков CS:GO
ssilka = requests.get('https://www.hltv.org/stats/players?startDate=2020-11-10&endDate=2021-11-10&rankingFilter=Top20')
HLTV = BeautifulSoup(ssilka.text, 'lxml')
names = HLTV.find_all('td', class_="playerCol")
stats = HLTV.find_all('td', class_='ratingCol')
Full_stats = ''
for i in range(20):
        Full_stats += str(i + 1) + '. ' +  str(names[i].text) + ' - ' + str(stats[i].text) + '\n'


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("МТУСИ", "Coronavirus status")
    keyboard.row("Weather", "CS:GO Stats")
    keyboard.row("/help")
    keyboard.row('Расписание')
    bot.send_message(message.chat.id, 'Привет! Выбери интересующую тебя информацию', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Список команд:\n' +
                     'МТУСИ\n' +
                     'Coronavirus status\n' +
                     'Weather\n' +
                     'CS:GO Stats\n' +
                     'Расписание')


@bot.message_handler(content_types=['text'])
def soobshenia(message):
    if message.text.lower() == "coronavirus status":
        bot.send_photo(message.chat.id, 'http://i1.ytimg.com/vi/A8IhYUQLZxc/maxresdefault.jpg')
        bot.send_message(message.chat.id, 'Полная статистика по коронавирусу в мире\n' + '\n' +
                         'Кол-во заболевших: ' + str(Coronavirus_Cases).strip() + '\n' + '\n' +
                         'Кол-во смертей: ' + str(Deaths).strip() + '\n' + '\n' +
                         'Кол-во выздоровевших: ' + str(Recovered).strip() + '\n')
    if message.text.lower() == "мтуси":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    if message.text.lower() == "weather":
        bot.send_message(message.chat.id, 'Погода в Москве сейчса:\n' +
                         str(degreece) + ', Ощущается как: ' + str(Feels_like))
    if message.text.lower() == 'cs:go stats':
        bot.send_photo(message.chat.id, 'https://cdn.cloudflare.steamstatic.com/steam/apps/730/capsule_616x353.jpg?t=1635269541')
        bot.send_message(message.chat.id, 'Топ 20 игроков cs:go из топ 20 команд за последние 12 месяцев\n' +
                         Full_stats)
    if message.text.lower() == 'расписание':
        keyboard_2 = types.ReplyKeyboardMarkup()
        keyboard_2.row('Понедельник', 'Вторник', 'Среда')
        keyboard_2.row('Четверг', 'Пятинца')
        keyboard_2.row('Расписание на текущую неделю', 'Расписание на следующую неделю')
        keyboard_2.row('Выход')
        bot.send_message(message.chat.id, 'Привет! Выбери интересующую тебя информацию', reply_markup=keyboard_2)
    else:
        bot.send_message(message.chat.id, 'Извините, я Вас не понял')


bot.infinity_polling()
