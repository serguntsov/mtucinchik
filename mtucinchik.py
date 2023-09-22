import telebot
from telebot import types
import sqlite3
import random

bot = telebot.TeleBot("YOUR TOKEN")

def start_markup():
    markup = types.InlineKeyboardMarkup(row_width=True)
    link_keyboard = types.InlineKeyboardButton(text="Подписаться", url="https://t.me/mtucinchik")
    check_keyboard = types.InlineKeyboardButton(text="Проверить", callback_data="check")
    markup.add(link_keyboard, check_keyboard)
    return markup

def admin_markup():
    markup = types.InlineKeyboardMarkup(row_width=3)
    mailing_keyboard = types.InlineKeyboardButton(text="Рассылка", callback_data="mailing")
    markup.add(mailing_keyboard)
    return markup
    

def proverka_markup():
    markupp = types.InlineKeyboardMarkup(row_width=True)
    link_keyboard = types.InlineKeyboardButton(text="Подписаться", url="https://t.me/mtucinchik")
    check_keyboard = types.InlineKeyboardButton(text="Проверить", callback_data="проверить")
    markupp.add(link_keyboard, check_keyboard)
    return markupp

def start_markup2():
    markup2 = types.InlineKeyboardMarkup(row_width=True)
    btn1 = types.InlineKeyboardButton(text="Парни", callback_data="парни")
    btn2 = types.InlineKeyboardButton(text="Девушки", callback_data="девушки")
    btn3 = types.InlineKeyboardButton(text="Все равно", callback_data="все равно")
    markup2.add(btn1, btn2, btn3)
    return markup2


def start_markup22():
    markup22 = types.InlineKeyboardMarkup(row_width=True)
    btn122 = types.InlineKeyboardButton(text="Парни", callback_data="парни2")
    btn222 = types.InlineKeyboardButton(text="Девушки", callback_data="девушки2")
    btn322 = types.InlineKeyboardButton(text="Все равно", callback_data="все равно2")
    markup22.add(btn122, btn222, btn322)
    return markup22


def start_markup3():
    markup3 = types.InlineKeyboardMarkup(row_width=True)
    btn11 = types.InlineKeyboardButton(text="Я парень", callback_data='пол1')
    btn12 = types.InlineKeyboardButton(text="Я девушка", callback_data='пол2')
    markup3.add(btn11, btn12)
    return markup3


def start_markup4():
    markup4 = types.InlineKeyboardMarkup(row_width=True)
    btn13 = types.InlineKeyboardButton(text="Да", callback_data='да')
    btn14 = types.InlineKeyboardButton(text="Посмотреть свою анкету", callback_data='просмотранкеты')
    btn15 = types.InlineKeyboardButton(text="Изменить анкету", callback_data='нованкета')
    markup4.add(btn13, btn14, btn15)
    return markup4


def start_markup5():
    markup5 = types.InlineKeyboardMarkup(row_width=True)
    btn16 = types.InlineKeyboardButton(text="Все верно!", callback_data='верно')
    btn17 = types.InlineKeyboardButton(text="Нет, зарегистрируюсь заново", callback_data='новрег')
    markup5.add(btn16, btn17)
    return markup5


def start_markup6():
    markup6 = types.InlineKeyboardMarkup(row_width=True)
    btn61 = types.InlineKeyboardButton(text="Я парень", callback_data='пол3')
    btn62 = types.InlineKeyboardButton(text="Я девушка", callback_data='пол4')
    markup6.add(btn61, btn62)
    return markup6


def start_markup7():
    markup7 = types.InlineKeyboardMarkup(row_width=True)
    btn71 = types.InlineKeyboardButton(text="Парни", callback_data="парни1")
    btn72 = types.InlineKeyboardButton(text="Девушки", callback_data="девушки1")
    btn73 = types.InlineKeyboardButton(text="Все равно", callback_data="все равно1")
    markup7.add(btn71, btn72, btn73)
    return markup7

def start_anketa():
    markup8 = types.InlineKeyboardMarkup(row_width=True)
    btn1 = types.InlineKeyboardButton(text="Просмотр своей анкеты", callback_data="мояанкета")
    btn2 = types.InlineKeyboardButton(text="Оценка чужих анкет", callback_data="оценка")
    markup8.add(btn1, btn2)
    return markup8

def grade_anketa():
    markup9 = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text="👍", callback_data="лайк")
    btn2 = types.InlineKeyboardButton(text="👎", callback_data="дизлайк")
    markup9.add(btn1, btn2)
    return markup9

def grade_anketa1():
    markup10 = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text="👍", callback_data="👍")
    btn2 = types.InlineKeyboardButton(text="👎", callback_data="👎")
    btn3 = types.InlineKeyboardButton(text="Продолжить просмотр анкет", callback_data="оценка")
    markup10.add(btn1, btn2)
    markup10.add(btn3)
    return markup10

def vzanketa():
    markup11 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Посмотреть анкеты, которые меня оценили")
    markup11.add(btn1)
    return markup11

def vzanketa1():
    markup12 = types.InlineKeyboardMarkup(row_width=True)
    btn1 = types.InlineKeyboardButton(text="Просмотр своей анкеты", callback_data="мояанкета")
    btn2 = types.InlineKeyboardButton(text="Изменить анкету", callback_data="нованкета")
    btn3 = types.InlineKeyboardButton(text="Оценка чужих анкет", callback_data="оценка")
    markup12.add(btn1, btn2, btn3)
    return markup12

def dlya_moya_anketa():
    markup13 = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text="Изменить анкету", callback_data="нованкета")
    btn2 = types.InlineKeyboardButton(text="Оценка чужих анкет", callback_data="оценка")
    markup13.add(btn1, btn2)
    return markup13

def mailing(message):
    if message.text:
        message = message.text
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM login_id")
        login = [item[0] for item in cursor.fetchall()]
        connect.close()
        for i in login:
            bot.send_message(i, f"{message}", parse_mode='html')
    elif message.photo:
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS mailing_id(id INTEGER, photo BLOB)""")
        connect.commit()
        file_i = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_i.file_path)
        cursor.execute("INSERT INTO mailing_id VALUES(?, ?);", (message.chat.id, downloaded_file))
        connect.commit()
        bug = bot.send_message(message.chat.id, f"Напишите текст, он отобразится под фотографией\
            \nЧтобы отправить только фото, отправьте '<code>0</code>'", parse_mode='html')
        bot.register_next_step_handler(bug, photo_mal)
    
def photo_mal(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute(f"SELECT photo FROM mailing_id WHERE id = {message.chat.id}")
    data_photo = cursor.fetchone()
    if data_photo is not None: #проверка на наличие фото по айди
        photo_data = data_photo[0] #фотография из бд
        if message.text == str(0):
            cursor.execute("SELECT * FROM login_id")
            login = [item[0] for item in cursor.fetchall()]
            for i in login:
                bot.send_photo(i, photo = photo_data)
        else:
            message = message.text
            cursor.execute("SELECT * FROM login_id")
            login = [item[0] for item in cursor.fetchall()]
            connect.close()
            for i in login:
                bot.send_photo(i, photo = photo_data, caption = message, parse_mode='html')

    
@bot.message_handler(commands=['start'])
def start(message):
    first_name = message.chat.first_name
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
        id INTEGER
    )""")
    connect.commit()
    # check id in fields
    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        # add values in fields
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
        connect.commit()
        bot.send_message(message.chat.id, f'Привет {first_name}!\n'
                                        f'Чтобы пользоваться ботом подпишитесь на наш канал!',
                        reply_markup=start_markup())
    elif data is not None:
        cursor.execute(f"SELECT id FROM photo_id WHERE id = {people_id}")
        data1 = cursor.fetchone()
        if data1 is None:
            bot.send_message(message.chat.id,f'{first_name}, анкета была заполнена не полностью. Пожалуйста, пройдите регистрацию заново')
            connect.close()
            restart(message)
        else:
            bot.send_message(message.chat.id, 'Ваш аккаунт уже зарегистрирован\n'
                                            'Хотите продолжить?',
                            reply_markup=start_markup4())  # изменить на регистрация по новой или идем дальше
            connect.close()

@bot.message_handler(commands=['admin'])
def admin(message):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'administrator' or 'creator':
        bot.send_message(message.chat.id, "Приветсвую, администратор мтусинчика!", reply_markup=admin_markup())
    else:
        bot.send_message(message.chat.id, "У вас нет прав администратора")
        

def check3(call):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=call.message.chat.id).status == 'member' or 'administrator' or 'creator':
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute(f"SELECT years_id.years, sex_id.sex, name_id.name FROM name_id \
                INNER JOIN years_id ON name_id.id = years_id.id \
                    INNER JOIN sex_id ON name_id.id = sex_id.id \
                        WHERE name_id.id = {call.message.chat.id}")
        data_text = cursor.fetchone() #массив с данными из таблиц бд
        if data_text is not None:
            years, sex, name = data_text
            bot.send_message(call.message.chat.id, f'Хорошо, давай поменяем твою анкету\n\
    Как нам уже известно, ты {sex}\n\
    Тебя зовут {name}\n\
    Тебе {years} лет, все верно?', reply_markup=start_markup5())  # ТАКЖЕ ВЗЯТЬ ИЗ БД
        connect.close()
    else:
        bot.send_message(call.message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())

def verno(call):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=call.message.chat.id).status == 'member' or 'administrator' or 'creator':
        bot.send_message(call.message.chat.id, 'Отлично, тогда давай продолжим!\n'
                                            'Кто тебе интересен?', reply_markup=start_markup22())
    else:
        bot.send_message(call.message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())


def novreg(call):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=call.message.chat.id).status == 'member' or 'administrator' or 'creator':
        bot.send_message(call.message.chat.id, 'Хорошо, сделаем тебе новую анкету!\n'
                                            'Давай определимся с твоим полом',
                        reply_markup=start_markup6())  # СДЕЛАТЬ ПОЛНОСТЬЮ НОВРЕГ КРОМЕ ID
    else:
        bot.send_message(call.message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())
    
def restart(message):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'member':
        bot.send_message(message.chat.id, 'Давай определимся с твоим полом', reply_markup=start_markup6()) 
    else:
        bot.send_message(message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())
    
def check(call):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id='-1001720626187', user_id=call.message.chat.id).status:
            markup = types.InlineKeyboardMarkup(row_width=True)
            btn1 = types.InlineKeyboardButton(text="Регистрация", callback_data="регистрация")
            markup.add(btn1)
            bot.send_message(call.message.chat.id, "Спасибо что подписались на канал!", reply_markup=markup)
            break
    else:
        bot.send_message(call.message.chat.id, "Подпишитесь на канал!", reply_markup=start_markup())
        

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'check':
            check(call)
            
    if call.data == "mailing":
        mes_mailing = bot.send_message(call.message.chat.id, "Напишите сообщение для рассылки!")
        bot.register_next_step_handler(mes_mailing, mailing)
        
    if call.data == 'проверить':
        status = ['creator', 'administrator', 'member']
        for i in status:
            if i == bot.get_chat_member(chat_id='-1001720626187', user_id=call.message.chat.id).status:
                start(call.message)
                break
        else:
            bot.send_message(call.message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())
        
    if call.data == 'парни':
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS interest_id(
        id INTEGER, interest TEXT
        )""")
        connect.commit()
        cursor.execute(f"SELECT id FROM interest_id WHERE id = {call.message.chat.id}")
        data = cursor.fetchone()
        if data is None:
            # add values in fields
            cursor.execute("INSERT INTO interest_id VALUES(?, ?);", (call.message.chat.id, "Парни"))
            connect.commit()
        connect.close()
        kurs1(call)

    if call.data == 'девушки':
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS interest_id(
        id INTEGER, interest TEXT
        )""")
        connect.commit()
        cursor.execute(f"SELECT id FROM interest_id WHERE id = {call.message.chat.id}")
        data = cursor.fetchone()
        if data is None:
            # add values in fields
            cursor.execute("INSERT INTO interest_id VALUES(?, ?);", (call.message.chat.id, "Девушки"))
            connect.commit()
        connect.close()
        kurs1(call)

    if call.data == 'все равно':
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS interest_id(
        id INTEGER, interest TEXT
        )""")
        connect.commit()
        cursor.execute(f"SELECT id FROM interest_id WHERE id = {call.message.chat.id}")
        data = cursor.fetchone()
        if data is None:
            # add values in fields
            cursor.execute("INSERT INTO interest_id VALUES(?, ?);", (call.message.chat.id, "Все равно"))
            connect.commit()
        connect.close()
        kurs1(call)

    if call.data == 'пол1':
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS sex_id(
        id INTEGER, sex TEXT
        )""")
        connect.commit()
        cursor.execute(f"SELECT id FROM sex_id WHERE id = {call.message.chat.id}")
        data = cursor.fetchone()
        if data is None:
            # add values in fields
            cursor.execute("INSERT INTO sex_id VALUES(?, ?);", (call.message.chat.id, "Парень"))
            connect.commit()
        connect.close()
        interes(call)
            
    if call.data == 'пол2':
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS sex_id(
        id INTEGER, sex TEXT
        )""")
        connect.commit()
        cursor.execute(f"SELECT id FROM sex_id WHERE id = {call.message.chat.id}")
        data = cursor.fetchone()
        if data is None:
            # add values in fields
            cursor.execute("INSERT INTO sex_id VALUES(?, ?);", (call.message.chat.id, "Девушка"))
            connect.commit()
        connect.close()
        interes(call)

    if call.data == 'да':
        anketa_list(call)
    if call.data == 'просмотранкеты':
        svoya_anketa(call)
    if call.data == 'нованкета':
        check3(call)
    if call.data == 'верно':
        verno(call)
    if call.data == 'новрег':
        novreg(call)
    if call.data == 'пол3':
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS sex_id(
        id INTEGER, sex TEXT
        )""")
        connect.commit()
        cursor.execute(f"SELECT id FROM sex_id WHERE id = {call.message.chat.id}")
        data = cursor.fetchone()
        if data is not None:
            # Изменение в таблице
            cursor.execute("UPDATE sex_id SET sex = ? WHERE id = ?", ("Парень", call.message.chat.id)) #я апдейт
            connect.commit()
            interes1(call)
        else:
            # Запись в таблицу под рестарт
            cursor.execute("INSERT INTO sex_id VALUES(?, ?);", (call.message.chat.id, "Парень")) #запись
            connect.commit()
            interes1(call)
            
    if call.data == 'пол4':
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS sex_id(
        id INTEGER, sex TEXT
        )""")
        connect.commit()
        cursor.execute(f"SELECT id FROM sex_id WHERE id = {call.message.chat.id}")
        data = cursor.fetchone()
        if data is not None:
            # Изменение в таблице
            cursor.execute("UPDATE sex_id SET sex = ? WHERE id = ?", ("Девушка", call.message.chat.id)) #я апдейт
            connect.commit()
            interes1(call)
        else:
            # Запись в таблицу под рестарт
            cursor.execute("INSERT INTO sex_id VALUES(?, ?);", (call.message.chat.id, "Девушка")) #запись
            connect.commit()
            interes1(call)
            
    if call.data == 'парни1': #я апдейт
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS interest_id(
        id INTEGER, interest TEXT
        )""")
        connect.commit()
        cursor.execute(f"SELECT id FROM interest_id WHERE id = {call.message.chat.id}")
        data = cursor.fetchone()
        if data is not None:
            # Изменение в таблице
            cursor.execute("UPDATE interest_id SET interest = ? WHERE id = ?", ("Парни", call.message.chat.id)) #я апдейт
            connect.commit()
            kurs_update(call)
        else:
            # Запись в таблицу под рестарт
            cursor.execute("INSERT INTO interest_id VALUES(?, ?);", (call.message.chat.id, "Парни")) #запись
            connect.commit()
            kurs_update(call)
        
            
    if call.data == 'девушки1': #я апдейт
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS interest_id(
        id INTEGER, interest TEXT
        )""")
        connect.commit()
        cursor.execute(f"SELECT id FROM interest_id WHERE id = {call.message.chat.id}")
        data = cursor.fetchone()
        if data is not None:
            # Изменение в таблице
            cursor.execute("UPDATE interest_id SET interest = ? WHERE id = ?", ("Девушки", call.message.chat.id)) #я апдейт
            connect.commit()
            kurs_update(call)
        else:
            # Запись в таблицу под рестарт
            cursor.execute("INSERT INTO interest_id VALUES(?, ?);", (call.message.chat.id, "Девушки")) #запись
            connect.commit()
            kurs_update(call)    
        
            
    if call.data == 'все равно1':
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS interest_id(
        id INTEGER, interest TEXT
        )""")
        connect.commit()
        cursor.execute(f"SELECT id FROM interest_id WHERE id = {call.message.chat.id}")
        data = cursor.fetchone()
        if data is not None:
            # Изменение в таблице
            cursor.execute("UPDATE interest_id SET interest = ? WHERE id = ?", ("Все равно", call.message.chat.id)) #я апдейт
            connect.commit()
            kurs_update(call)
        else:
            # Запись в таблицу под рестарт
            cursor.execute("INSERT INTO interest_id VALUES(?, ?);", (call.message.chat.id, "Все равно")) #запись
            connect.commit()
            kurs_update(call)

    if call.data == 'парни2':
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS interest_id(
        id INTEGER, interest TEXT
        )""")
        connect.commit()
        cursor.execute(f"SELECT id FROM interest_id WHERE id = {call.message.chat.id}")
        data = cursor.fetchone()
        if data is not None:
            # Изменение в таблице
            cursor.execute("UPDATE interest_id SET interest = ? WHERE id = ?", ("Парни", call.message.chat.id)) #я апдейт
            connect.commit()
        connect.close()
        kurs2(call)
            
    if call.data == 'девушки2':
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS interest_id(
        id INTEGER, interest TEXT
        )""")
        connect.commit()
        cursor.execute(f"SELECT id FROM interest_id WHERE id = {call.message.chat.id}")
        data = cursor.fetchone()
        if data is not None:
            # Изменение в таблице
            cursor.execute("UPDATE interest_id SET interest = ? WHERE id = ?", ("Девушки", call.message.chat.id)) #я апдейт
            connect.commit()
        connect.close()
        kurs2(call)
            
    if call.data == 'все равно2':
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS interest_id(
        id INTEGER, interest TEXT
        )""")
        connect.commit()
        cursor.execute(f"SELECT id FROM interest_id WHERE id = {call.message.chat.id}")
        data = cursor.fetchone()
        if data is not None:
            # Изменение в таблице
            cursor.execute("UPDATE interest_id SET interest = ? WHERE id = ?", ("Все равно", call.message.chat.id)) #я апдейт
            connect.commit()
        connect.close()
        kurs2(call)
            
    if call.data == 'мояанкета':
        svoya_anketa(call)
        
    if call.data == 'оценка':
        anketa_list(call)
            
    if call.data == 'лайк':
        if bot.get_chat_member(chat_id='-1001720626187', user_id=call.message.chat.id).status == 'member' or 'administrator' or 'creator':
            bot.send_message(call.message.chat.id, "Лайк отправлен, ждём ответа")
            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS like(
                        id INTEGER, like_id 
                    )""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS vzaim_like(
                        id INTEGER, vzlike_id 
                    )""")
            cursor.execute(f"SELECT drugie_id1 FROM like_dizlike WHERE id = ?", (call.message.chat.id,))
            like = [item[0] for item in cursor.fetchall()]
            like1 = like.pop(0)
            if 1 == 1:
                cursor.execute(f"SELECT like_id FROM like WHERE id = ?", (call.message.chat.id,))
                data_like = cursor.fetchone()
                print("дата лайк обычный:", data_like)
                print("////////////")
                # Извлечь как строку
                if data_like:
                    data_like = data_like[0] 
                else:
                    data_like = ""
                print("дата лайк:", data_like)
                if not data_like:
                    cursor.execute("INSERT INTO like VALUES(?, ?);", (call.message.chat.id, like1))
                else:
                    cursor.execute(f"SELECT like_id FROM like WHERE id = ?", (call.message.chat.id,))
                    data_like1 = [item[0] for item in cursor.fetchall()]
                    data_like1_list = ','.join(map(str, data_like1))
                    if str(like1) in data_like1_list:
                        bot.send_message(call.message.chat.id, 'Вы ранее ставили лайк данной анкете.\nПока не получили обратного ответа от пользователя!\nОжидайте!')
                    else:
                        print("426 строка")
                        like3 = f"{data_like}, {like1}"
                        cursor.execute("UPDATE like SET like_id = ? WHERE id = ?", (like3, call.message.chat.id))
                        connect.commit()
            if 2 == 2:
                cursor.execute(f"SELECT vzlike_id FROM vzaim_like WHERE id = ?", (call.message.chat.id,))
                vzlike = [item[0] for item in cursor.fetchall()]
                vzlike1 = ','.join(map(str, vzlike))
                if str(like1) not in vzlike1:
                    cursor.execute("INSERT INTO vzaim_like VALUES(?, ?);", (call.message.chat.id, like1))
                    bot.send_message(like1, 'Ваша анкета кому-то понравилась', reply_markup = vzanketa())
            print("LIKE1:", like1)
            like2 = ','.join(map(str, like))
            cursor.execute("UPDATE like_dizlike SET drugie_id1 = ? WHERE id = ?", (like2, call.message.chat.id))
            connect.commit()
            connect.close()
            anketa1(call.message.chat.id)
        else:
            bot.send_message(call.message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())
        
    if call.data == 'дизлайк':
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute(f"SELECT drugie_id1 FROM like_dizlike WHERE id = ?", (call.message.chat.id,))
        dizlike = [item[0] for item in cursor.fetchall()]
        dizlike.pop(0)
        dizlike1 = ','.join(map(str, dizlike))
        cursor.execute("UPDATE like_dizlike SET drugie_id1 = ? WHERE id = ?", (dizlike1, call.message.chat.id))
        connect.commit()
        connect.close()
        anketa1(call.message.chat.id)
        
    if call.data == 'регистрация':
        start_message(call)
        
    if call.data == '👍':
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute(f"SELECT vz_ank FROM vzaim_ank WHERE id = ?", (call.message.chat.id,))
        anketa = [item[0] for item in cursor.fetchall()]
        num = anketa.pop(0)
        print("NUM", num)
        cursor.execute(f"SELECT photo FROM photo_id WHERE id = {call.message.chat.id}")
        data_photo = cursor.fetchone()
        photo_data = data_photo[0] #фотография из бд
        #обьединение таблиц по айди пользователя (inner join) 
        cursor.execute(f"SELECT years_id.years, sex_id.sex, name_id.name, kurs_id.kurs, interest_id.interest, description_id.description FROM name_id \
            INNER JOIN years_id ON name_id.id = years_id.id \
                INNER JOIN sex_id ON name_id.id = sex_id.id \
                    INNER JOIN kurs_id ON name_id.id = kurs_id.id \
                        INNER JOIN interest_id ON name_id.id = interest_id.id \
                            INNER JOIN description_id ON name_id.id = description_id.id \
                                WHERE name_id.id = {call.message.chat.id}")
        data_text = cursor.fetchone() #массив с данными из таблиц бд
        if 2 == 2:
                cursor.execute(f"DELETE FROM vzaim_like WHERE id = {call.message.chat.id} and vzlike_id = {num}")
                cursor.execute(f"DELETE FROM vzaim_ank WHERE id = {call.message.chat.id} and vz_ank = {num}")
                cursor.execute(f"SELECT like_id FROM like WHERE id = ?", (num,))
                likee10 = cursor.fetchone()[0]
                print("LIKEE10:", likee10)
                if len(str(likee10) )> 11:
                    likee = list(map(int, likee10.split(',')))
                    if likee is not None:
                        likee.remove(call.message.chat.id)
                        likee1 = ','.join(map(str, likee))
                        cursor.execute("UPDATE like SET like_id = ? WHERE id = ?", (likee1, num))
                        connect.commit()
                else:
                    cursor.execute(f"DELETE FROM like WHERE id = {num}")
                connect.commit()
        if data_text is not None:
            years, sex, name, kurs, interest, description = data_text 
            message_text = f"{name} {years} ({sex})\nКурс: {kurs}\nИнтересы: {interest}\nО себе: {description}\n"
            bot.send_photo(num, photo = photo_data, caption = message_text)
            if 1 == 1:
                bot.send_message(num,f"Взаимная симпатия! -> @{call.message.chat.username}", reply_markup=vzanketa1())
        if 2 == 2:
            cursor.execute(f"SELECT photo FROM photo_id WHERE id = {num}")
            data_photo1 = cursor.fetchone()
            photo_data1 = data_photo1[0] #фотография из бд
            #обьединение таблиц по айди пользователя (inner join) 
            cursor.execute(f"SELECT years_id.years, sex_id.sex, name_id.name, kurs_id.kurs, interest_id.interest, description_id.description FROM name_id \
                INNER JOIN years_id ON name_id.id = years_id.id \
                    INNER JOIN sex_id ON name_id.id = sex_id.id \
                        INNER JOIN kurs_id ON name_id.id = kurs_id.id \
                            INNER JOIN interest_id ON name_id.id = interest_id.id \
                                INNER JOIN description_id ON name_id.id = description_id.id \
                                    WHERE name_id.id = {num}")
            data_text1 = cursor.fetchone() #массив с данными из таблиц бд
            if data_text1 is not None:
                years, sex, name, kurs, interest, description = data_text1 
                message_text1 = f"{name} {years} ({sex})\nКурс: {kurs}\nИнтересы: {interest}\nО себе: {description}\n"
                bot.delete_message(call.message.chat.id, call.message.id)
                bot.send_photo(call.message.chat.id, photo = photo_data1, caption = message_text1)
                if 3 == 3:
                    chat_info = bot.get_chat(num)
                    user_name = chat_info.username
                    bot.send_message(call.message.chat.id,f"Начните общение прямо сейчас! -> @{user_name}", reply_markup=vzanketa1())
        connect.close()

    if call.data == '👎':
        dizl = 2
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute(f"SELECT vz_ank FROM vzaim_ank WHERE id = ?", (call.message.chat.id,))
        anketa = [item[0] for item in cursor.fetchall()]
        num = anketa.pop(0)
        if 2 == 2:
                cursor.execute(f"DELETE FROM vzaim_like WHERE id = {call.message.chat.id} and vzlike_id = {num}")
                cursor.execute(f"DELETE FROM vzaim_ank WHERE id = {call.message.chat.id} and vz_ank = {num}")
                cursor.execute(f"SELECT like_id FROM like WHERE id = ?", (num,))
                likee10 = cursor.fetchone()[0]
                if len(str(likee10) )> 11:
                    likee = list(map(int, likee10.split(',')))
                    if likee is not None:
                        likee.remove(call.message.chat.id)
                        likee1 = ','.join(map(str, likee))
                        cursor.execute("UPDATE like SET like_id = ? WHERE id = ?", (likee1, num))
                        connect.commit()
                    connect.commit()
                else:
                    cursor.execute(f"DELETE FROM like WHERE id = {num}")
        connect.close()
        vzlike_ank(call.message, dizl)

@bot.message_handler(content_types=['text'])
def vzlike_ank(message, dizl=None):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'member' or 'administrator' or 'creator':
        try:
            if (dizl == 2) or (message and message.text.lower() == "посмотреть анкеты, которые меня оценили"):
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()  
                cursor.execute("""CREATE TABLE IF NOT EXISTS vzaim_ank(
                            id INTEGER, vz_ank 
                        )""")
                cursor.execute(f"SELECT id FROM vzaim_like WHERE vzlike_id = ?", (message.chat.id,))
                vzlike1 = [item[0] for item in cursor.fetchall()]
                try:
                    num = vzlike1.pop(0)
                    if 1 == 1:
                        cursor.execute(f"DELETE FROM vzaim_like WHERE vzlike_id = ? and id =?", (message.chat.id, num))
                        connect.commit()
                    if 2 == 2:
                        cursor.execute(f"SELECT vz_ank FROM vzaim_ank WHERE id = ?", (message.chat.id,))
                        vzank = [item[0] for item in cursor.fetchall()]
                        if num not in vzank:
                            cursor.execute("INSERT INTO vzaim_ank VALUES(?, ?);", (message.chat.id, num))
                            connect.commit()
                    cursor.execute(f"SELECT photo FROM photo_id WHERE id = {num}")
                    data_photo = cursor.fetchone()
                    photo_data = data_photo[0] #фотография из бд
                    #обьединение таблиц по айди пользователя (inner join) 
                    cursor.execute(f"SELECT years_id.years, sex_id.sex, name_id.name, kurs_id.kurs, interest_id.interest, description_id.description FROM name_id \
                        INNER JOIN years_id ON name_id.id = years_id.id \
                            INNER JOIN sex_id ON name_id.id = sex_id.id \
                                INNER JOIN kurs_id ON name_id.id = kurs_id.id \
                                    INNER JOIN interest_id ON name_id.id = interest_id.id \
                                        INNER JOIN description_id ON name_id.id = description_id.id \
                                            WHERE name_id.id = {num}")
                    data_text = cursor.fetchone() #массив с данными из таблиц бд
                    if data_text is not None:
                        if vzlike1 is not None:
                            years, sex, name, kurs, interest, description = data_text 
                            message_text = f"{name} {years} ({sex})\nКурс: {kurs}\nИнтересы: {interest}\nО себе: {description}"
                            bot.send_photo(message.chat.id, photo = photo_data, caption = message_text, reply_markup=grade_anketa1())         
                except:
                    bot.send_message(message.chat.id, f'Анкет нет!\nОцените кого-то вы, возможно, оценка будет взаимной!', reply_markup=start_anketa())
        except:
            bot.send_message(message.chat.id, 'Вашу анкету не мог никто оценить.\nДля начала заполните профиль!')
    else:
        bot.send_message(message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())



# НИЖЕ НУЖНО СДЕЛАТЬ ЗАПИСИ В БД

def start_message(call):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=call.message.chat.id).status == 'member' or 'administrator' or 'creator':
        bot.send_message(call.message.chat.id, 'Давай определимся с твоим полом', reply_markup=start_markup3())
    else:
        bot.send_message(call.message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())

def interes(call):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=call.message.chat.id).status == 'member' or 'administrator' or 'creator':
        bot.send_message(call.message.chat.id, 'Кто тебе интересен?', reply_markup=start_markup2())
    else:
        bot.send_message(call.message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())


def kurs1(call):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=call.message.chat.id).status == 'member' or 'administrator' or 'creator':
        msg = bot.send_message(call.message.chat.id, 'Как тебя зовут?')
        bot.register_next_step_handler(msg, age)
    else:
        bot.send_message(call.message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())


def age(message):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'member' or 'administrator' or 'creator':
        if message.text:
            if (message.text.isalpha()) and (len(message.text)<17):   #ISALPHA ПРОВЕРЯЕТ ТОЛЬКО ИЗ БУКВ СОСТОИТ СТРОКА ИЛИ НЕТ
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS name_id(
                id INTEGER, name TEXT
                )""")
                connect.commit()
                cursor.execute(f"SELECT id FROM name_id WHERE id = {message.chat.id}")
                data = cursor.fetchone()
                if data is None:
                    # add values in fields
                    cursor.execute("INSERT INTO name_id VALUES(?, ?);", (message.chat.id, message.text))
                    connect.commit()
                    connect.close()
                msg4 = bot.send_message(message.chat.id, 'Сколько тебе лет?')
                bot.register_next_step_handler(msg4, course)
            else:
                bug10 = bot.send_message(message.chat.id, 'В имени не должны присутствовать цифры или посторонние символы кроме букв!\n'
                                                        'Напишите ваше имя без цифр')
                bot.register_next_step_handler(bug10, age)
        else:
            bug = bot.send_message(message.chat.id, 'Сообщение должно быть в текстовом формате!\n'
                                                    'Пожалуйста, напишите как вас зовут')
            bot.register_next_step_handler(bug, age)
    else:
        bot.send_message(message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())


def course(message):            # если тип в возрасте отправил не цифры! ебни проверку!!
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'member' or 'administrator' or 'creator':
        if message.text:
            if (message.text.isdigit()) and (len(message.text)<3) and (len(message.text)>1):    #КАК Я ПОНЯЛ ISDIGIT ПРОВЕРЯЕТ ТОЛЬКО ЦИФРЫ В СООБЩЕНИИ ИЛИ НЕТ
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS years_id(
                id INTEGER, years INTEGER
                )""")
                connect.commit()
                cursor.execute(f"SELECT id FROM years_id WHERE id = {message.chat.id}")
                data = cursor.fetchone()
                if data is None:
                    # add values in fields
                    cursor.execute("INSERT INTO years_id VALUES(?, ?);", (message.chat.id, message.text))
                    connect.commit()
                    connect.close()
                msg5 = bot.send_message(message.chat.id, 'С какого ты курса?')
                bot.register_next_step_handler(msg5, bio)
            else:
                bug = bot.send_message(message.chat.id, 'В сообщении присутствуют не только числа, либо вы слишком малы!\nОтправь только число')
                bot.register_next_step_handler(bug, course)
        else:
            bug = bot.send_message(message.chat.id, 'Сообщение должно быть в текстовом формате!\n'
                                                    'Пожалуйста, напишите сколько вам лет')
            bot.register_next_step_handler(bug, course)
    else:
        bot.send_message(message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())

def bio(message):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'member' or 'administrator' or 'creator':
        if message.text:
            if (message.text.isdigit()) and (len(message.text)<2):
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS kurs_id(
                id INTEGER, kurs INTEGER
                )""")
                connect.commit()
                cursor.execute(f"SELECT id FROM kurs_id WHERE id = {message.chat.id}")
                data = cursor.fetchone()
                if data is None:
                    # add values in fields
                    cursor.execute("INSERT INTO kurs_id VALUES(?, ?);", (message.chat.id, message.text))
                    connect.commit()
                    connect.close()
                msg6 = bot.send_message(message.chat.id, 'Расскажи немного о себе!\nЭто поможет лучше подобрать тебе компанию.')
                bot.register_next_step_handler(msg6, photos)
            else:
                bug1 = bot.send_message(message.chat.id, 'В сообщении присутствуют не только числа, либо такого курса не существует!\n'
                                                        'Отправь только число или верный курс')
                bot.register_next_step_handler(bug1, bio)
        else:
            bug = bot.send_message(message.chat.id, 'Сообщение должно быть в текстовом формате!\n'
                                                    'Пожалуйста, напишите с какого вы курса')
            bot.register_next_step_handler(bug, bio)
    else:
        bot.send_message(message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())
        
def photos(message):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'member' or 'administrator' or 'creator':
        if message.text:
            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS description_id(
            id INTEGER, description TEXT
            )""")
            connect.commit()
            cursor.execute(f"SELECT id FROM description_id WHERE id = {message.chat.id}")
            data = cursor.fetchone()
            if data is None:
                # add values in fields
                cursor.execute("INSERT INTO description_id VALUES(?, ?);", (message.chat.id, message.text))
                connect.commit()
                connect.close()
            msg7 = bot.send_message(message.chat.id, 'Пришли свою фотографию!')
            bot.register_next_step_handler(msg7, photoss)
        else:
            bug = bot.send_message(message.chat.id, 'Сообщение должно быть в текстовом формате!\n'
                                                    'Пожалуйста, напишите немного о себе')
            bot.register_next_step_handler(bug, photos)
    else:
        bot.send_message(message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())

# сохранение фото на сервере
def photoss(message):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'member' or 'administrator' or 'creator':
        if message.photo: #проверка что отправили фото
            file_info = bot.get_file(message.photo[-1].file_id)
            if file_info is not None:
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS photo_id(
                    id INTEGER, photo BLOB
                )""")
                connect.commit()
                # проверка записи по айди
                cursor.execute(f"SELECT id FROM photo_id WHERE id = {message.chat.id}")
                data = cursor.fetchone()
                if data is None:
                    # сохранение в бд фото и айди
                    downloaded_file = bot.download_file(file_info.file_path)
                    cursor.execute("INSERT INTO photo_id (id, photo) VALUES (?, ?);", (message.chat.id, downloaded_file))
                    connect.commit()
                cursor.execute(f"SELECT photo FROM photo_id WHERE id = {message.chat.id}")
                bot.send_message(message.chat.id, 'Фото сохранено!\nВыбери дальнейшее действие!', reply_markup=start_anketa())
                connect.close()
        else:
            bug = bot.send_message(message.chat.id, 'Необходимо отправить именно фото!')
            bot.register_next_step_handler(bug, photoss)
    else:
        bot.send_message(message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())

def svoya_anketa(call): #анкета
    if bot.get_chat_member(chat_id='-1001720626187', user_id=call.message.chat.id).status == 'member' or 'administrator' or 'creator':
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute(f"SELECT photo FROM photo_id WHERE id = {call.message.chat.id}")
        data_photo = cursor.fetchone()
        if data_photo is not None: #проверка на наличие фото по айди
            photo_data = data_photo[0] #фотография из бд
            #обьединение таблиц по айди пользователя (inner join) 
            cursor.execute(f"SELECT years_id.years, sex_id.sex, name_id.name, kurs_id.kurs, interest_id.interest, description_id.description FROM name_id \
                INNER JOIN years_id ON name_id.id = years_id.id \
                    INNER JOIN sex_id ON name_id.id = sex_id.id \
                        INNER JOIN kurs_id ON name_id.id = kurs_id.id \
                            INNER JOIN interest_id ON name_id.id = interest_id.id \
                                INNER JOIN description_id ON name_id.id = description_id.id \
                                    WHERE name_id.id = {call.message.chat.id}")
            data_text = cursor.fetchone() #массив с данными из таблиц бд
            if data_text is not None:
                years, sex, name, kurs, interest, description = data_text 
                message_text = f"{name} {years} ({sex})\nКурс: {kurs}\nИнтересы: {interest}\nО себе: {description}"
                bot.send_message(call.message.chat.id, 'Вот ваша анкета!')
                bot.send_photo(call.message.chat.id, photo = photo_data, caption = message_text, reply_markup = dlya_moya_anketa())
                connect.close()
    else:
        bot.send_message(call.message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())
            
#ЧТОБЫ ВСЯ ЭТА ХУЙНЯ СНИЗУ РАБОТАЛА, НАДО ЧТОБЫ В ANKETA_ID5 ВСЕГДА БЫЛА ОДНА СТРОКА С ЗАПОЛНЕННЫМИ ДАННЫМИ!!!
            
def anketa_list(call):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=call.message.chat.id).status == 'member' or 'administrator' or 'creator':
        chat_id = call.message.chat.id
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute(f"SELECT interest FROM interest_id WHERE id = {chat_id}")
        data = cursor.fetchone()
        if data is not None:
            data_1 = str(data[0])
            print("data_1: ", data_1)
            if data_1 == "Парни":
                cursor.execute(f"SELECT id FROM sex_id WHERE sex = ? AND id != ?", ('Парень', call.message.chat.id))
                result_list = [item[0] for item in cursor.fetchall()]
                random.shuffle(result_list)
                print("result_list1: ", result_list)
                anketa_p(chat_id, result_list)
            elif data_1 == "Девушки":
                cursor.execute(f"SELECT id FROM sex_id WHERE sex = ? AND id != ?", ('Девушка', chat_id))
                result_list = [item[0] for item in cursor.fetchall()]
                random.shuffle(result_list)
                print("result_list2: ", result_list)
                anketa_p(chat_id, result_list)
            elif data_1 == "Все равно":
                cursor.execute(f"SELECT id FROM sex_id WHERE id != ?", (chat_id))
                result_list = [item[0] for item in cursor.fetchall()]
                random.shuffle(result_list)
                print("result_list3: ", result_list)
                anketa_p(chat_id, result_list)
            connect.close()
        else:
            bot.send_message(call.message.chat.id, 'Ваша анкета заполнена не полносью!')
    else:
        bot.send_message(call.message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())
        
def anketa_p(chat_id, result_list):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=chat_id).status == 'member' or 'administrator' or 'creator':
        print("result_list_anketa_p: ", result_list)
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS anketa_id5(
                    id INTEGER, drugie_id 
                )""")
        result_list2 =  ','.join(map(str, result_list)) #Делаем просто строку из id убрав список, для того, чтобы записать в бд
        cursor.execute(f"SELECT id FROM anketa_id5 WHERE id = ?", (chat_id,))
        id_polz = cursor.fetchone()
        if id_polz is None:
            cursor.execute("INSERT INTO anketa_id5 (id, drugie_id) VALUES (?, ?);", (chat_id, result_list2))
        cursor.execute(f"SELECT drugie_id FROM anketa_id5 WHERE id =?;", (chat_id,))
        drugie_id_polz = [item[0] for item in cursor.fetchall()]
        if len(drugie_id_polz) < 3: #ПОЧЕМУ-ТО НЕ СРАБАТЫВАЕТ (МОЖНО СНАЧАЛА ПРОСТО ЗАПОЛНИТЬ СДЕЛАВ 12 == drugie_id_polz) НО ПОЛСЕ ТОГО, КАК СНОВА СТАНЕТ ПУСТОЙ НАДО ЗАПОЛНИТЬ СУКА!!
            cursor.execute("UPDATE anketa_id5 SET drugie_id = ? WHERE id = ?", (result_list2, chat_id))
            connect.commit()
        connect.close()
        anketa1(chat_id)
    else:
        bot.send_message(chat_id, "Подпишитесь на канал!", reply_markup=proverka_markup())


def anketa1(chat_id):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=chat_id).status == 'member' or 'administrator' or 'creator':
        try:
            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS like_dizlike(
                    id INTEGER, drugie_id1 
                )""")
            cursor.execute(f"SELECT drugie_id FROM anketa_id5 WHERE id = ?", (chat_id,))
            anketa = cursor.fetchone()[0]
            if anketa is not None:
                sanketa = list(map(int, anketa.split(',')))
                random.shuffle(sanketa)
            if sanketa is not None:
                num = sanketa.pop(0) # Получаем первую анкету из списка и удаляем ее в списке
                if 2 == 2:
                    cursor.execute(f"SELECT drugie_id1 FROM like_dizlike WHERE id = ?", (chat_id,))
                    num1 = [item[0] for item in cursor.fetchall()]
                    cursor.execute(f"SELECT id FROM like_dizlike")
                    idnum = [item[0] for item in cursor.fetchall()]
                    if (len(num1) < 3) and (chat_id not in idnum):
                        cursor.execute("INSERT INTO like_dizlike (id, drugie_id1) VALUES (?, ?)", (chat_id, num))
                    if chat_id in idnum:
                        cursor.execute("UPDATE like_dizlike SET drugie_id1 = ? WHERE id = ?", (num, chat_id))
                        connect.commit()
                if 1 == 1:
                    sanketa1 =  ','.join(map(str, sanketa))
                    cursor.execute("UPDATE anketa_id5 SET drugie_id = ? WHERE id = ?", (sanketa1, chat_id))
                    connect.commit()
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute(f"SELECT photo FROM photo_id WHERE id = {num}")
                data_photo = cursor.fetchone()
                photo_data = data_photo[0] #фотография из бд
                #обьединение таблиц по айди пользователя (inner join) 
                cursor.execute(f"SELECT years_id.years, sex_id.sex, name_id.name, kurs_id.kurs, interest_id.interest, description_id.description FROM name_id \
                    INNER JOIN years_id ON name_id.id = years_id.id \
                        INNER JOIN sex_id ON name_id.id = sex_id.id \
                            INNER JOIN kurs_id ON name_id.id = kurs_id.id \
                                INNER JOIN interest_id ON name_id.id = interest_id.id \
                                    INNER JOIN description_id ON name_id.id = description_id.id \
                                        WHERE name_id.id = {num}")
                data_text = cursor.fetchone() #массив с данными из таблиц бд
                if data_text is not None:
                    if sanketa is not None:
                        years, sex, name, kurs, interest, description = data_text 
                        message_text = f"{name} {years} ({sex})\nКурс: {kurs}\nИнтересы: {interest}\nО себе: {description}"
                        bot.send_photo(chat_id, photo = photo_data, caption = message_text, reply_markup=grade_anketa())
                    else:
                        bot.send_message(chat_id, 'Анкеты закончились!')    
            else:
                bot.send_message(chat_id, 'Анкеты закончились!')
        except:
            bot.send_message(chat_id, 'Анкеты закончились!', reply_markup=start_anketa()) 
    else:
        bot.send_message(chat_id, "Подпишитесь на канал!", reply_markup=proverka_markup())

# ПРИ ОТВЕТЕ ВСЕ ВЕРНО
def kurs2(call):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=call.message.chat.id).status == 'member' or 'administrator' or 'creator':
        novmsg2 = bot.send_message(call.message.chat.id, 'С какого ты курса?')
        bot.register_next_step_handler(novmsg2, novbio2)
    else:
        bot.send_message(call.message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())


def novbio2(message):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'member':
        if message.text:
            if (message.text.isdigit()) and (len(message.text) < 2):
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS kurs_id(
                id INTEGER, kurs TEXT
                )""")
                connect.commit()
                cursor.execute(f"SELECT id FROM kurs_id WHERE id = {message.chat.id}")
                data = cursor.fetchone()
                if data is not None:
                    # Изменение в таблице
                    cursor.execute("UPDATE kurs_id SET kurs = ? WHERE id = ?", (message.text, message.chat.id)) #я апдейт
                    connect.commit()
                    connect.close()
                novmsg26 = bot.send_message(message.chat.id, 'Расскажи немного о себе!\nЭто поможет лучше подобрать тебе компанию.')
                bot.register_next_step_handler(novmsg26, novphotos2)
            else:
                bug5 = bot.send_message(message.chat.id, 'В сообщении присутствуют не только числа, либо такого курса не существует!'
                                                        'Отправь только число или верный курс')
                bot.register_next_step_handler(bug5 , novbio)
        else:
            bug = bot.send_message(message.chat.id, 'Сообщение должно быть в текстовом формате!\n'
                                                    'Пожалуйста, напишите с какого вы курса')
            bot.register_next_step_handler(bug, novbio2)
    else:
        bot.send_message(message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())
        
def novphotos2(message):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'member' or 'administrator' or 'creator':
        if message.text:
            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS description_id(
            id INTEGER, description TEXT
            )""")
            connect.commit()
            cursor.execute(f"SELECT id FROM description_id WHERE id = {message.chat.id}")
            data = cursor.fetchone()
            if data is not None:
                # Изменение в таблице
                cursor.execute("UPDATE description_id SET description = ? WHERE id = ?", (message.text, message.chat.id)) #я апдейт
                connect.commit()
                connect.close()
            novmsg27 = bot.send_message(message.chat.id, 'Пришли свою фотографию!')
            bot.register_next_step_handler(novmsg27, novphotoss2)
        else:
            bug = bot.send_message(message.chat.id, 'Сообщение должно быть в текстовом формате!\n'
                                                    'Пожалуйста, напишите немного о себе')
            bot.register_next_step_handler(bug, novphotos2)
    else:
        bot.send_message(message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())

# сохранение фото на сервере
def novphotoss2(message):  
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'member' or 'administrator' or 'creator':
        if message.photo:     # ПРОВЕРКА, ЧТО ОТПРАВИЛИ ИМЕННО ФОТО
            file_info = bot.get_file(message.photo[-1].file_id)
            if file_info is not None:
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS photo_id(
                    id INTEGER, photo BLOB
                )""")
                connect.commit()
                # проверка записи по айди
                cursor.execute(f"SELECT id FROM photo_id WHERE id = {message.chat.id}")
                data = cursor.fetchone()
                if data is not None:
                    # сохранение в бд фото и айди
                    downloaded_file = bot.download_file(file_info.file_path)
                    cursor.execute("UPDATE photo_id SET photo = ? WHERE id = ?", (downloaded_file, message.chat.id))
                    connect.commit()
                connect.close()
                bot.send_message(message.chat.id, 'Фото сохранено!\nВыбери дальнейшее действие!', reply_markup=start_anketa())
        else:
            bug = bot.send_message(message.chat.id, 'Необходимо отправить именно фото!')
            bot.register_next_step_handler(bug, novphotoss2)
    else:
        bot.send_message(message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())
        
#ЗАРЕГИСТРИРУЮСЬ ЗАНОВО!

def interes1(call):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=call.message.chat.id).status == 'member' or 'administrator' or 'creator':
        bot.send_message(call.message.chat.id, 'Кто тебе интересен?', reply_markup=start_markup7())
    else:
        bot.send_message(call.message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())


def kurs_update(call):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=call.message.chat.id).status == 'member' or 'administrator' or 'creator':
        novmsg = bot.send_message(call.message.chat.id, 'Как тебя зовут?')
        bot.register_next_step_handler(novmsg, novage)
    else:
        bot.send_message(call.message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())


def novage(message):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'member' or 'administrator' or 'creator':
        if message.text:
            if (message.text.isalpha()) and (len(message.text)<15):
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS name_id(
                id INTEGER, name TEXT
                )""")
                connect.commit()
                cursor.execute(f"SELECT id FROM name_id WHERE id = {message.chat.id}")
                data = cursor.fetchone()
                if data is not None:
                    # Изменение в таблице
                    cursor.execute("UPDATE name_id SET name = ? WHERE id = ?", (message.text, message.chat.id)) #я апдейт
                    connect.commit()
                else:
                    cursor.execute("INSERT INTO name_id VALUES(?, ?);", (message.chat.id, message.text)) #запись
                    connect.commit()
                connect.close()
                novmsg4 = bot.send_message(message.chat.id, 'Сколько тебе лет?')
                bot.register_next_step_handler(novmsg4, novcourse)

            else:
                bug11 = bot.send_message(message.chat.id, 'В имени не должны присутствовать цифры.\n'
                                                        'Напишите ваше имя без цифр')
                bot.register_next_step_handler(bug11, novage)
        else:
            bug = bot.send_message(message.chat.id, 'Сообщение должно быть в текстовом формате!\n'
                                                    'Пожалуйста, напишите как вас зовут')
            bot.register_next_step_handler(bug, novage)
    else:
        bot.send_message(message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())
        
def novcourse(message):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'member' or 'administrator' or 'creator':
        if message.text:
            if (message.text.isdigit()) and (len(message.text)<3):
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS years_id(
                id INTEGER, years TEXT
                )""")
                connect.commit()
                cursor.execute(f"SELECT id FROM years_id WHERE id = {message.chat.id}")
                data = cursor.fetchone()
                if data is not None:
                    # Изменение в таблице
                    cursor.execute("UPDATE years_id SET years = ? WHERE id = ?", (message.text, message.chat.id)) #я апдейт
                    connect.commit()
                else:
                    cursor.execute("INSERT INTO years_id VALUES(?, ?);", (message.chat.id, message.text)) #запись
                    connect.commit()
                novmsg5 = bot.send_message(message.chat.id, 'С какого ты курса?')
                bot.register_next_step_handler(novmsg5, novbio)
            else:
                bug3 = bot.send_message(message.chat.id, 'В сообщении присутствуют не только числа, либо ваш возраст слишком большой!\n'
                                                        'Отправь только число либо верный возраст')
                bot.register_next_step_handler(bug3, novcourse)
        else:
            bug = bot.send_message(message.chat.id, 'Сообщение должно быть в текстовом формате!\n'
                                                    'Пожалуйста, напишите сколько вам лет')
            bot.register_next_step_handler(bug, novcourse)
        connect.close()
    else:
        bot.send_message(message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())

def novbio(message):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'member' or 'administrator' or 'creator':
        if message.text:
            if (message.text.isdigit()) and (len(message.text) < 2):
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS kurs_id(
                id INTEGER, kurs TEXT
                )""")
                connect.commit()
                cursor.execute(f"SELECT id FROM kurs_id WHERE id = {message.chat.id}")
                data = cursor.fetchone()
                if data is not None:
                    # Изменение в таблице
                    cursor.execute("UPDATE kurs_id SET kurs = ? WHERE id = ?", (message.text, message.chat.id)) #я апдейт
                    connect.commit()
                else:
                    cursor.execute("INSERT INTO kurs_id VALUES(?, ?);", (message.chat.id, message.text)) #запись
                    connect.commit()
                novmsg6 = bot.send_message(message.chat.id, 'Расскажи немного о себе!\nЭто поможет лучше подобрать тебе компанию.')
                bot.register_next_step_handler(novmsg6, novphotos)
            else:
                bug4 = bot.send_message(message.chat.id, 'В сообщении присутствуют не только числа, либо такого курса не существует!\n'
                                                        'Отправь только число или верный курс')
                bot.register_next_step_handler(bug4, novbio)
        else:
            bug = bot.send_message(message.chat.id, 'Сообщение должно быть в текстовом формате!\n'
                                                    'Пожалуйста, напишите с какого вы курса')
            bot.register_next_step_handler(bug, novbio)
        connect.close()
    else:
        bot.send_message(message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())
        
def novphotos(message):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'member' or 'administrator' or 'creator':
        if message.text:
            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS description_id(
            id INTEGER, description TEXT
            )""")
            connect.commit()
            cursor.execute(f"SELECT id FROM description_id WHERE id = {message.chat.id}")
            data = cursor.fetchone()
            if data is not None:
                # Изменение в таблице
                cursor.execute("UPDATE description_id SET description = ? WHERE id = ?", (message.text, message.chat.id)) #я апдейт
                connect.commit()
            else:
                cursor.execute("INSERT INTO description_id VALUES(?, ?);", (message.chat.id, message.text)) #запись
                connect.commit()
            novmsg7 = bot.send_message(message.chat.id, 'Пришли свою фотографию!')
            bot.register_next_step_handler(novmsg7, novphotoss)
        else:
            bug = bot.send_message(message.chat.id, 'Сообщение должно быть в текстовом формате!\n'
                                                    'Пожалуйста, напишите немного о себе')
            bot.register_next_step_handler(bug, novphotos)
        connect.close()
    else:
        bot.send_message(message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())

# сохранение фото на сервере
def novphotoss(message):
    if bot.get_chat_member(chat_id='-1001720626187', user_id=message.chat.id).status == 'member' or 'administrator' or 'creator':
        if message.photo:     # ПРОВЕРКА, ЧТО ОТПРАВИЛИ ИМЕННО ФОТО
            file_info = bot.get_file(message.photo[-1].file_id)
            if file_info is not None:
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS photo_id(
                    id INTEGER, photo BLOB
                )""")
                connect.commit()
                # проверка записи по айди
                cursor.execute(f"SELECT id FROM photo_id WHERE id = {message.chat.id}")
                data = cursor.fetchone()
                if data is not None:
                    # сохранение в бд фото и айди
                    downloaded_file = bot.download_file(file_info.file_path)
                    cursor.execute("UPDATE photo_id SET photo = ? WHERE id = ?", (downloaded_file, message.chat.id))
                    connect.commit()
                else:
                    downloaded_file = bot.download_file(file_info.file_path)
                    cursor.execute("INSERT INTO photo_id (id, photo) VALUES (?, ?);", (message.chat.id, downloaded_file))
                    connect.commit() #запись
                bot.send_message(message.chat.id, 'Фото сохранено!\nВыбери дальнейшее действие!', reply_markup=start_anketa())
        else:
            bug = bot.send_message(message.chat.id, 'Необходимо отправить именно фото!')
            bot.register_next_step_handler(bug, novphotoss)
        connect.close()
    else:
        bot.send_message(message.chat.id, "Подпишитесь на канал!", reply_markup=proverka_markup())
            
bot.polling(none_stop=True)
