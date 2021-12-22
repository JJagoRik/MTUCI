import telebot
from telebot import types
import psycopg2
from datetime import datetime, timedelta


token = '2090088655:AAGp9HOySQaaMtSlHiXyAHMhGBju_g8BSyI'
bot = telebot.TeleBot(token)


conn = psycopg2.connect(database="tg_tables",
                        user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()
cursor_teach = conn.cursor()


def week_num():
    now = datetime.now()
    sep = datetime(now.year if now.month >= 9 else now.year - 1, 9, 1)

    d1 = sep - timedelta(days=sep.weekday())
    d2 = now - timedelta(days=now.weekday())

    parity = ((d2 - d1).days // 7) % 2
    week = ("{}".format("down" if parity else "Up"))
    return week


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('Расписание', 'Неделя')
    bot.send_message(message.chat.id, 'Привет! Выбери интересующую тебя информацию', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def soobshenia(message):
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
    days_comp = [x.lower() for x in days]
    if message.text.lower() in days_comp:
        for i in days:
            if i.lower() == message.text.lower():
                day_of_week = i
        if week_num() == 'down':
            cursor.execute("SELECT * FROM tables.timetable WHERE day=%s AND (week=%s OR week=%s)",
                           (str(day_of_week), ('Any'), ('down')))
        elif week_num() == 'Up':
            cursor.execute("SELECT * FROM tables.timetable WHERE day=%s AND (week=%s OR week=%s)",
                           (str(day_of_week), ('Any'), ('Up')))
        timetable = list(cursor.fetchall())
        table = ''
        if day_of_week == 'Четверг' and week_num() == 'down':
            bot.send_message(message.chat.id, 'Нижняя неделя, разрешено отдыхать')
        else:
            for i in range(len(timetable)):
                predmet = timetable[i][2]
                cursor_teach.execute("SELECT * FROM tables.teachers WHERE subject='%s'" % (str(predmet)))
                teacher = list(cursor_teach.fetchall())
                table += timetable[i][2] + '   каб. ' + timetable[i][3] + '   время начала: ' + timetable[i][4] + \
                         '   преподаватель: ' + str(teacher[0][1]) + '\n' + '\n'
            bot.send_message(message.chat.id, day_of_week + '\n' +
                             table + '\n')


    if message.text.lower() == 'расписание на текущую неделю':
        table = ''
        for day_of_week in days:
            if week_num() == 'down':
                cursor.execute("SELECT * FROM tables.timetable WHERE day=%s AND (week=%s OR week=%s)",
                               (str(day_of_week), ('Any'), ('down')))
            elif week_num() == 'Up':
                cursor.execute("SELECT * FROM tables.timetable WHERE day=%s AND (week=%s OR week=%s)",
                               (str(day_of_week), ('Any'), ('Up')))
            timetable = list(cursor.fetchall())
            if day_of_week == 'Четверг' and week_num() == 'down':
                table += day_of_week + '\n' + 'Нижняя неделя, разрешено отдыхать' + '\n' + '\n'
            else:
                table += day_of_week + '\n'
                for i in range(len(timetable)):
                    predmet = timetable[i][2]
                    cursor_teach.execute("SELECT * FROM tables.teachers WHERE subject='%s'" % (str(predmet)))
                    teacher = list(cursor_teach.fetchall())
                    table += timetable[i][2] + '   каб. ' + timetable[i][3] + '   время начала: ' + timetable[i][4] + \
                             '   преподаватель: ' + str(teacher[0][1]) + '\n' + '\n'
        bot.send_message(message.chat.id, table)

    if message.text.lower() == 'расписание на следующую неделю':
        table = ''
        for day_of_week in days:
            if week_num() == 'down':
                cursor.execute("SELECT * FROM tables.timetable WHERE day=%s AND (week=%s OR week=%s)",
                               (str(day_of_week), ('Any'), ('Up')))
            elif week_num() == 'Up':
                cursor.execute("SELECT * FROM tables.timetable WHERE day=%s AND (week=%s OR week=%s)",
                               (str(day_of_week), ('Any'), ('down')))
            timetable = list(cursor.fetchall())
            if day_of_week == 'Четверг' and week_num() == 'Up':
                table += day_of_week + '\n' + 'Нижняя неделя, разрешено отдыхать' + '\n' + '\n'
            else:
                table += day_of_week + '\n'
                for i in range(len(timetable)):
                    predmet = timetable[i][2]
                    cursor_teach.execute("SELECT * FROM tables.teachers WHERE subject='%s'" % (str(predmet)))
                    teacher = list(cursor_teach.fetchall())
                    table += timetable[i][2] + '   каб. ' + timetable[i][3] + '   время начала: ' + timetable[i][4] + \
                             '   преподаватель: ' + str(teacher[0][1]) + '\n' + '\n'
        bot.send_message(message.chat.id, table)

    if message.text.lower() == 'расписание':
        keyboard_2 = types.ReplyKeyboardMarkup()
        keyboard_2.row('Понедельник', 'Вторник', 'Среда')
        keyboard_2.row('Четверг', 'Пятница')
        keyboard_2.row('Расписание на текущую неделю', 'Расписание на следующую неделю')
        keyboard_2.row('Выход')
        bot.send_message(message.chat.id, 'Выберите, на какой день/неделю отбразить расписание',
                         reply_markup=keyboard_2)

    if message.text.lower() == 'неделя':
        if week_num() == 'Up':
            bot.send_message(message.chat.id, "Текущая неделя: верхняя")
        elif week_num() == 'down':
            bot.send_message(message.chat.id, "Текущая неделя: нижняя")

    if message.text.lower() == 'выход':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row('Расписание', 'Неделя')
        bot.send_message(message.chat.id, 'Выбери интересующую тебя информацию', reply_markup=keyboard)


bot.infinity_polling()