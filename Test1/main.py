import sqlite3
import telebot
import config
import random
from telebot import types

conn = sqlite3.connect('db.db', check_same_thread=False)
cursor = conn.cursor()
def db_table_val(user_id: int, user_name: str, user_surname: str, email: str, city: str, school: str, phone: str):
	cursor.execute('INSERT INTO test (user_id, user_name, user_surname, email, city, school, phone) VALUES (?, ?, ?, ?, ?, ?, ?)', (user_id, user_name, user_surname, email, city, school, phone))
	conn.commit()
        
def update_db_table(faculty: str, direction: str, user_id: int):
	cursor.execute('UPDATE test SET faculty = ?, direction = ? WHERE user_id = ?', (faculty, direction, user_id))
	conn.commit()

class InlineKeyboard:
    def __init__(self, bot):
        self.bot=bot

    def create_keybord(self, button_list):
        keyboard_markup=types.InlineKeyboardMarkup(row_width=5)

        buttons=[]
        for button_text, callback_data in button_list:
            button=types.InlineKeyboardButton(button_text, callback_data=callback_data)
            buttons.append(button)

        keyboard_markup.add(*buttons)
        return keyboard_markup

bot = telebot.TeleBot(config.TOKEN)
inline_keybord = InlineKeyboard(bot)

technozhr = [0, 0, 0, 0, 0, 0]
technomag = [0, 0, 0, 0, 0, 0]
keep_soul = [0, 0, 0, 0, 0, 0]
alchemist = [0, 0, 0, 0, 0, 0]
keep_civil = [0, 0, 0, 0, 0, 0]
keep_world = [0, 0, 0, 0, 0, 0]
oracle = [0, 0, 0, 0, 0, 0]

global name 
global surname 
global email  
global city
global phone 
global school 
global us_id

global msg


arr = ["Осуществлять монтаж или сборку машин и приборов",
"Обслужиать и ремонтировать различные механизмы",
"Выяснять проблемы людей, проводить диагностику, искать причины проблем и объяснять их людям", "Изобретать и производить новые химические соединения (лаки, краски, бытововую химию и др.)",
"Создавать эффективную систему документооборота, перемещения товаров для работы предприятия", "Организовывать и управлять производством новой техники и технологий",
"Создавать одежду, обувь, предметы мебели и др. предметы быта", "Обеспечивать людей комфортным и безопасным жильем, поддерживать в рабочем состоянии городскую инфраструктуру",
"Обучать людей, преподавать в учебных заведениях, сообщать, разъяснять людям нужные им сведения", "Защищать природу от негативного воздействия человеческой цивилизации, обеспечивать жизнеспособность планеты",
"Держать людей в курсе событий, сообщать им важную информацию", "Создавать произведения фото- и видеоискусства",
"Анализировать статистические данные, составлять прогнозы и планы развития", "Руководить работой других людей и организовать людей для выполнения рабочих задач и мероприятий",
"Придумывать способы улучшить производство", "Составлять точные описания, отчеты о наблюдениях, явлениях, событиях, измеряемых объектах и др., открывать фундаментальные законы природы", "Делать изделия с уникальными свойствами из новых материалов",
"Исследовать свойства и природу веществ, придумывать и производить новые материалы", "Создавать, модернизировать и следить за безопасностью компьютерных сетей и программного обеспечения",
"Развивать у людей различные способности", "Обслуживать приборы, следить за их работой, регулировать и настраивать придумывать, изобретать новую технику и технологии (корабли, автомобили, космические корабли, энергостанции, компьютерную технику и программное обеспечение и др.)",
"Производить и продавать новую технику и технологии", "Следить за развитием науки и выбирать, какие технологии будут помогать человечеству эффективно развиваться",
"Выводить новые сорта растений, новые породы животных", "Добывать ресурсы для существования человеческой цивилизации (продукты питания, энергию, воду и пр.) и доставлять их людям",
"Помогать людям поддерживать физическое и психологическое здоровье, лечить, поддерживать в тяжелой ситуации, продвигать здоровый образ жизни", "Управлять персоналом в организации: осуществлять отбор, помогать адаптироваться, обучать, мотивировать на эффективную работу",
"Анализировать рынок товаров и выбирать направления развития предприятия", "Обеспечивать мирную коммуникацию людей друг с другом, помогать договариваться, разрешать споры, защищать юридические интересы людей и организаций",
"Придумывать, изобретать новую технику и технологии (корабли, автомобили, космические корабли, энергостанции, компьютерную технику и программное обеспечение и др.)", "Доводить информацию о товарах до потребителя", "Защищать интересы людей находящихся в трудных жизненных ситуациях",
"Улучшать существующие технику и технологии", "Работать на сложном химическом оборудовании, проводить опыты с химическими веществами", "Изготовлять по чертежам (проектам) детали, изделия, здания и сооружения"]

directs = ["Электроэнергетика и электротехника ⚡", "Авиастроение ✈️", "Конструирование и технология электронных средств ⚙️", "Автоматизация технологических процессов и производств 🤖", "Информационные системы и технологии 💻", "Системный анализ и управление 📊", "Лингвистика 💬", "Психология 🧠", "Клиническая психология 🧠", 
           "Юриспруденция 💼", "Химия 🧪", "Ядерная физика и технологии ☢️", "Химия, физика и механика материалов 🔬", "Физика ⚛️", "Химия 🧪", "Юриспруденция 💼", "Социология", "Государственное и муниципальное управление 🏛️", "Фундаментальная информатика и информационные технологии 📡", 
           "Бизнес-информатика 📊", "Автоматизация технологических процессов и производств 🤖", "Информатика и вычислительная техника 👨‍💻", "Программная инженерия 👨‍💻", "Авиастроение ✈️", "Прикладная математика и информатика 👨‍💻", "Химия, физика и механика материалов 🔬", "Электроэнергетика и электротехника ⚡", 
           "Экология и природопользование 🌍", "Химия 🧪", "Технология геологической разведки 🗺️", "Государственное и муниципальное управление 🏛️", "Прикладная информатика 👨‍💻", "Государственное и муниципальное управление 🏛️", "Юриспруденция 💼", "Экономика 📈"]


@bot.message_handler(commands = ['start'])
def welcome(message):
    welcomebtn = [('Представиться 👋', 'in'), ('Промолчать 😶', 'nah')]
    welcomemrk = inline_keybord.create_keybord(welcomebtn)

    yy = types.ReplyKeyboardRemove()

    bot.send_message(message.chat.id, f"Здравствуй, добрый путник! 🖖", reply_markup=yy)
    bot.send_message(message.chat.id, f"Перед тобой открыта ГУД Вселенная! 🌌\n" + "Эта Вселенная зародилась давным-давно, ещё в прошлом столетии. В этой Вселенной есть место каждому: здесь дружно живут представители разных гильдий, которые вместе строят и развивают ее. Чтобы всем в ней жилось хорошо предлагаем тебе найти и занять место в этой уникальной Вселенной! Готов рассказать немного о себе?", reply_markup= welcomemrk)

@bot.message_handler(commands=['stop'])
def stop(message):
    bot.stop_polling()

@bot.message_handler(commands = ['restart'])
def restart_test(message):
    res = [('Да', 'ye'), ('Нет','n')] 
    markpp = inline_keybord.create_keybord(res)

    value_to_check = message.chat.id
    info = cursor.execute('SELECT * FROM test WHERE user_id=?', (value_to_check, )).fetchone()
    if info is not None:
        bot.send_message(message.chat.id, 'При перехождении теста, предыдущие результаты сменятся новыми.\n' + 'Продолжить?', reply_markup=markpp)
    else:
        stt = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bss = types.KeyboardButton('/start')
        stt.add(bss)
        bot.send_message(message.chat.id, 'У вас нет аккаунта в нашей системе. 😯 \n' + 'Для регистрации выберете команду <b>start</b>', parse_mode='html', reply_markup=stt)
          

@bot.message_handler(commands=['deleteaccount'])
def delete_account(message):
    user_id = message.from_user.id
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM test WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()

    bot.send_message(message.chat.id, 'Ваш аккаунт удален из базы данных. 🗑️')
    bot.send_message(message.chat.id, message.from_user.id)


@bot.callback_query_handler(func = lambda callback: True)
def callback_name(callback):
    global name  
    global technozhr
    global technomag
    global keep_soul
    global alchemist
    global keep_civil
    global keep_world
    global oracle 
    global phone
    global faculty
    global school
    global surname
    global name
    global email
    global city

    wlcmmm = [('Да', 'yes'), ('Нет', 'no')]
    markupp = inline_keybord.create_keybord(wlcmmm)

    againbtns = [('Да', 'ye'), ('Нет', 'nah')]
    againmrk = inline_keybord.create_keybord(againbtns)

    buttons=[('1','one'),('2','two'),('3','three'),('4','four'),('5','five')]
    markup=inline_keybord.create_keybord(buttons)

    buttons1=[('1','one1'),('2','two1'),('3','three1'),('4','four1'),('5','five1')]
    markup1=inline_keybord.create_keybord(buttons1)

    buttons2=[('1','one2'),('2','two2'),('3','three2'),('4','four2'),('5','five2')]
    markup2=inline_keybord.create_keybord(buttons2)

    buttons3=[('1','one3'),('2','two3'),('3','three3'),('4','four3'),('5','five3')]
    markup3=inline_keybord.create_keybord(buttons3)

    buttons4=[('1','one4'),('2','two4'),('3','three4'),('4','four4'),('5','five4')]
    markup4=inline_keybord.create_keybord(buttons4)

    buttons5=[('1','one5'),('2','two5'),('3','three5'),('4','four5'),('5','five5')]
    markup5=inline_keybord.create_keybord(buttons5)

    buttons6=[('1','one6'),('2','two6'),('3','three6'),('4','four6'),('5','five6')]
    markup6=inline_keybord.create_keybord(buttons6)

    buttons7=[('1','one7'),('2','two7'),('3','three7'),('4','four7'),('5','five7')]
    markup7=inline_keybord.create_keybord(buttons7) 

    buttons8=[('1','one8'),('2','two8'),('3','three8'),('4','four8'),('5','five8')]
    markup8=inline_keybord.create_keybord(buttons8)

    buttons9=[('1','one9'),('2','two9'),('3','three9'),('4','four9'),('5','five9')]
    markup9=inline_keybord.create_keybord(buttons9)

    buttons10=[('1','one10'),('2','two10'),('3','three10'),('4','four10'),('5','five10')]
    markup10=inline_keybord.create_keybord(buttons10)
    
    buttons11=[('1','one11'),('2','two11'),('3','three11'),('4','four11'),('5','five11')]
    markup11=inline_keybord.create_keybord(buttons11)

    buttons12=[('1','one12'),('2','two12'),('3','three12'),('4','four12'),('5','five12')]
    markup12=inline_keybord.create_keybord(buttons12)

    buttons13=[('1','one13'),('2','two13'),('3','three13'),('4','four13'),('5','five13')]
    markup13=inline_keybord.create_keybord(buttons13)

    buttons14=[('1','one14'),('2','two14'),('3','three14'),('4','four14'),('5','five14')]
    markup14=inline_keybord.create_keybord(buttons14)

    buttons15=[('1','one15'),('2','two15'),('3','three15'),('4','four15'),('5','five15')]
    markup15=inline_keybord.create_keybord(buttons15)

    buttons16=[('1','one16'),('2','two16'),('3','three16'),('4','four16'),('5','five16')]
    markup16=inline_keybord.create_keybord(buttons16)

    buttons17=[('1','one17'),('2','two17'),('3','three17'),('4','four17'),('5','five17')]
    markup17=inline_keybord.create_keybord(buttons17)

    buttons18=[('1','one18'),('2','two18'),('3','three18'),('4','four18'),('5','five18')]
    markup18=inline_keybord.create_keybord(buttons18)

    buttons19=[('1','one19'),('2','two19'),('3','three19'),('4','four19'),('5','five19')]
    markup19=inline_keybord.create_keybord(buttons19)

    buttons20=[('1','one20'),('2','two20'),('3','three20'),('4','four20'),('5','five20')]
    markup20=inline_keybord.create_keybord(buttons20)

    buttons21=[('1','one21'),('2','two21'),('3','three21'),('4','four21'),('5','five21')]
    markup21=inline_keybord.create_keybord(buttons21)

    buttons22=[('1','one22'),('2','two22'),('3','three22'),('4','four22'),('5','five22')]
    markup22=inline_keybord.create_keybord(buttons22)

    buttons23=[('1','one23'),('2','two23'),('3','three23'),('4','four23'),('5','five23')]
    markup23=inline_keybord.create_keybord(buttons23)

    buttons24=[('1','one24'),('2','two24'),('3','three24'),('4','four24'),('5','five24')]
    markup24=inline_keybord.create_keybord(buttons24)

    buttons25=[('1','one25'),('2','two25'),('3','three25'),('4','four25'),('5','five25')]
    markup25=inline_keybord.create_keybord(buttons25)

    buttons26=[('1','one26'),('2','two26'),('3','three26'),('4','four26'),('5','five26')]
    markup26=inline_keybord.create_keybord(buttons26)

    buttons27=[('1','one27'),('2','two27'),('3','three27'),('4','four27'),('5','five27')]
    markup27=inline_keybord.create_keybord(buttons27)

    buttons28=[('1','one28'),('2','two28'),('3','three28'),('4','four28'),('5','five28')]
    markup28=inline_keybord.create_keybord(buttons28)

    buttons29=[('1','one29'),('2','two29'),('3','three29'),('4','four29'),('5','five29')]
    markup29=inline_keybord.create_keybord(buttons29)

    buttons30=[('1','one30'),('2','two30'),('3','three30'),('4','four30'),('5','five30')]
    markup30=inline_keybord.create_keybord(buttons30)

    buttons31=[('1','one31'),('2','two31'),('3','three31'),('4','four31'),('5','five31')]
    markup31=inline_keybord.create_keybord(buttons31)

    buttons32=[('1','one32'),('2','two32'),('3','three32'),('4','four32'),('5','five32')]
    markup32=inline_keybord.create_keybord(buttons32)

    buttons33=[('1','one33'),('2','two33'),('3','three33'),('4','four33'),('5','five33')]
    markup33=inline_keybord.create_keybord(buttons33)

    buttons34=[('1','one34'),('2','two34'),('3','three34'),('4','four34'),('5','five34')]
    markup34=inline_keybord.create_keybord(buttons34)

    if(callback.data == 'yes'):
        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup="")
        bot.edit_message_text(f"Отлично!\n Напиши свою фамилию", callback.message.chat.id, callback.message.message_id)
        #bot.send_message(callback.message.chat.id, f"Отлично!\n Напиши свою фамилию")
        name = callback.from_user.first_name
        bot.register_next_step_handler(callback.message, get_user_surname)
    elif (callback.data == 'no'):
        bot.edit_message_text(f"Напиши свое имя", callback.message.chat.id, callback.message.message_id)
        #bot.send_message(callback.message.chat.id, f"Напиши свое имя")
        bot.register_next_step_handler(callback.message, get_user_name)
    elif callback.data=="ye":
        #bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup="")
        bot.edit_message_text(arr[0], callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    elif callback.data=="one" or callback.data=="two" or callback.data=="three" or callback.data=="four" or callback.data=="five":
                if callback.data=="one":
                    technozhr[0] += 1
                    technozhr[1] += 1
                elif callback.data=="two": 
                    technozhr[0] += 2
                    technozhr[1] += 2
                elif callback.data=="three": 
                    technozhr[0] += 3
                    technozhr[1] += 3
                elif callback.data=="four": 
                    technozhr[0] += 4
                    technozhr[1] += 4
                elif callback.data=="five": 
                    technozhr[0] += 5
                    technozhr[1] += 5
                bot.edit_message_text(arr[1], callback.message.chat.id, callback.message.message_id, reply_markup=markup1)             
    elif callback.data=="one1" or callback.data=="two1" or callback.data=="three1" or callback.data=="four1" or callback.data=="five1":
                if callback.data=="one1":
                    technozhr[0] += 1
                    technozhr[2] += 1
                elif callback.data=="two1": 
                    technozhr[0] += 2
                    technozhr[2] += 2    
                elif callback.data=="three1":
                    technozhr[0] += 3
                    technozhr[2] += 3    
                elif callback.data=="four1":
                    technozhr[0] += 4
                    technozhr[2] += 4    
                elif callback.data=="five1": 
                    technozhr[0] += 5
                    technozhr[2] += 5    
                bot.edit_message_text(arr[2], callback.message.chat.id, callback.message.message_id, reply_markup=markup2)   
    elif callback.data=="one2" or callback.data=="two2" or callback.data=="three2" or callback.data=="four2" or callback.data=="five2":
                if callback.data=="one2":
                    keep_soul[0] += 1
                    keep_soul[1] += 1
                elif callback.data=="two2": 
                    keep_soul[0] += 2
                    keep_soul[1] += 2  
                elif callback.data=="three2":
                    keep_soul[0] += 3
                    keep_soul[1] += 3    
                elif callback.data=="four2":
                    keep_soul[0] += 4
                    keep_soul[1] += 4   
                elif callback.data=="five2": 
                    keep_soul[0] += 5
                    keep_soul[1] += 5    
                bot.edit_message_text(arr[3], callback.message.chat.id, callback.message.message_id, reply_markup=markup3)
    elif callback.data=="one3" or callback.data=="two3" or callback.data=="three3" or callback.data=="four3" or callback.data=="five3":
                if callback.data=="one3":
                    alchemist[0] += 1
                    alchemist[1] += 1
                elif callback.data=="two3": 
                    alchemist[0] += 2
                    alchemist[1] += 2   
                elif callback.data=="three3":
                    alchemist[0] += 3
                    alchemist[1] += 3    
                elif callback.data=="four3":
                    alchemist[0] += 4
                    alchemist[1] += 4   
                elif callback.data=="five3": 
                    alchemist[0] += 5
                    alchemist[1] += 5    
                bot.edit_message_text(arr[4], callback.message.chat.id, callback.message.message_id, reply_markup=markup4)
    elif callback.data=="one4" or callback.data=="two4" or callback.data=="three4" or callback.data=="four4" or callback.data=="five4":
                if callback.data=="one4":
                    oracle[0] += 1
                    oracle[1] += 1
                elif callback.data=="two4": 
                    oracle[0] += 2
                    oracle[1] += 2
                elif callback.data=="three4":
                    oracle[0] += 3
                    oracle[1] += 3
                elif callback.data=="four4":
                    oracle[0] += 4
                    oracle[1] += 4   
                elif callback.data=="five4": 
                    oracle[0] += 5
                    oracle[1] += 5   
                bot.edit_message_text(arr[5], callback.message.chat.id, callback.message.message_id, reply_markup=markup5)
    elif callback.data=="one5" or callback.data=="two5" or callback.data=="three5" or callback.data=="four5" or callback.data=="five5":
                if callback.data=="one5":
                    technomag[0] += 1
                    technomag[1] += 1
                elif callback.data=="two5": 
                    technomag[0] += 2
                    technomag[1] += 2  
                elif callback.data=="three5":
                    technomag[0] += 3
                    technomag[1] += 3   
                elif callback.data=="four5":
                    technomag[0] += 4
                    technomag[1] += 4    
                elif callback.data=="five5": 
                    technomag[0] += 5
                    technomag[1] += 5  
                bot.edit_message_text(arr[6], callback.message.chat.id, callback.message.message_id, reply_markup=markup6)  
    elif callback.data=="one6" or callback.data=="two6" or callback.data=="three6" or callback.data=="four6" or callback.data=="five6":
                if callback.data=="one6":
                    keep_civil[0] += 1
                    keep_civil[1] += 1
                elif callback.data=="two6": 
                    keep_civil[0] += 2
                    keep_civil[1] += 2   
                elif callback.data=="three6":
                    keep_civil[0] += 3
                    keep_civil[1] += 3    
                elif callback.data=="four6":
                    keep_civil[0] += 4
                    keep_civil[1] += 4    
                elif callback.data=="five6": 
                    keep_civil[0] += 5
                    keep_civil[1] += 5    
                bot.edit_message_text(arr[7], callback.message.chat.id, callback.message.message_id, reply_markup=markup7)
    elif callback.data=="one7" or callback.data=="two7" or callback.data=="three7" or callback.data=="four7" or callback.data=="five7":
                if callback.data=="one7":
                    keep_civil[0] += 1
                    keep_civil[2] += 1
                elif callback.data=="two7": 
                    keep_civil[0] += 2
                    keep_civil[2] += 2   
                elif callback.data=="three7":
                    keep_civil[0] += 3
                    keep_civil[2] += 3    
                elif callback.data=="four7":
                    keep_civil[0] += 4
                    keep_civil[2] += 4    
                elif callback.data=="five7": 
                    keep_civil[0] += 5
                    keep_civil[2] += 5  
                bot.edit_message_text(arr[8], callback.message.chat.id, callback.message.message_id, reply_markup=markup8)  
    elif callback.data=="one8" or callback.data=="two8" or callback.data=="three8" or callback.data=="four8" or callback.data=="five8":
                if callback.data=="one8":
                    keep_soul[0] += 1
                    keep_soul[1] += 1
                elif callback.data=="two8": 
                    keep_soul[0] += 2
                    keep_soul[1] += 2   
                elif callback.data=="three8":
                    keep_soul[0] += 3
                    keep_soul[1] += 3    
                elif callback.data=="four8":
                    keep_soul[0] += 4
                    keep_soul[1] += 4    
                elif callback.data=="five8": 
                    keep_soul[0] += 5
                    keep_soul[1] += 5    
                bot.edit_message_text(arr[9], callback.message.chat.id, callback.message.message_id, reply_markup=markup9)
    elif callback.data=="one9" or callback.data=="two9" or callback.data=="three9" or callback.data=="four9" or callback.data=="five9":
                if callback.data=="one9":
                    keep_civil[0] += 1
                    keep_civil[3] += 1 
                elif callback.data=="two9": 
                    keep_civil[0] += 2
                    keep_civil[3] += 2 
                elif callback.data=="three9":
                    keep_civil[0] += 3
                    keep_civil[3] += 3    
                elif callback.data=="four9":
                    keep_civil[0] += 4
                    keep_civil[3] += 4     
                elif callback.data=="five9": 
                    keep_civil[0] += 5
                    keep_civil[3] += 5    
                bot.edit_message_text(arr[10], callback.message.chat.id, callback.message.message_id, reply_markup=markup10)
    elif callback.data=="one10" or callback.data=="two10" or callback.data=="three10" or callback.data=="four10" or callback.data=="five10":
                if callback.data=="one10":
                    keep_world[0] += 1
                    keep_world[1] += 1
                elif callback.data=="two10": 
                    keep_world[0] += 2
                    keep_world[1] += 2    
                elif callback.data=="three10":
                    keep_world[0] += 3
                    keep_world[1] += 3    
                elif callback.data=="four10":
                    keep_world[0] += 4
                    keep_world[1] += 4    
                elif callback.data=="five10": 
                    keep_world[0] += 5
                    keep_world[1] += 5   
                bot.edit_message_text(arr[11], callback.message.chat.id, callback.message.message_id, reply_markup=markup11)
    elif callback.data=="one11" or callback.data=="two11" or callback.data=="three11" or callback.data=="four11" or callback.data=="five11":
                if callback.data=="one11":
                    keep_world[0] += 1
                    keep_world[2] += 1
                elif callback.data=="two11": 
                    keep_world[0] += 2
                    keep_world[2] += 2  
                elif callback.data=="three11":
                    keep_world[0] += 3
                    keep_world[2] += 3   
                elif callback.data=="four11":
                    keep_world[0] += 4
                    keep_world[2] += 4    
                elif callback.data=="five11": 
                    keep_world[0] += 5
                    keep_world[2] += 5    
                bot.edit_message_text(arr[12], callback.message.chat.id, callback.message.message_id, reply_markup=markup12)
    elif callback.data=="one12" or callback.data=="two12" or callback.data=="three12" or callback.data=="four12" or callback.data=="five12":
                if callback.data=="one12":
                    oracle[0] += 1
                    oracle[2] += 1
                elif callback.data=="two12": 
                    oracle[0] += 2
                    oracle[2] += 2    
                elif callback.data=="three12":
                    oracle[0] += 3
                    oracle[2] += 3    
                elif callback.data=="four12":
                    oracle[0] += 4
                    oracle[2] += 4   
                elif callback.data=="five12": 
                    oracle[0] += 5
                    oracle[2] += 5
                bot.edit_message_text(arr[13], callback.message.chat.id, callback.message.message_id, reply_markup=markup13)
    elif callback.data=="one13" or callback.data=="two13" or callback.data=="three13" or callback.data=="four13" or callback.data=="five13":
                if callback.data=="one13":
                    oracle[0] += 1
                    oracle[3] += 1
                elif callback.data=="two13": 
                    oracle[0] += 2
                    oracle[3] += 2   
                elif callback.data=="three13":
                    oracle[0] += 3
                    oracle[3] += 3    
                elif callback.data=="four13":
                    oracle[0] += 4
                    oracle[3] += 4    
                elif callback.data=="five13": 
                    oracle[0] += 5
                    oracle[3] += 5    
                bot.edit_message_text(arr[14], callback.message.chat.id, callback.message.message_id, reply_markup=markup14)

    elif callback.data=="one14" or callback.data=="two14" or callback.data=="three14" or callback.data=="four14" or callback.data=="five14":
                if callback.data=="one14":
                    technozhr[0] += 1
                    technozhr[3] += 1
                elif callback.data=="two14": 
                    technozhr[0] += 2
                    technozhr[3] += 2   
                elif callback.data=="three14":
                    technozhr[0] += 3
                    technozhr[3] += 3    
                elif callback.data=="four14":
                    technozhr[0] += 4
                    technozhr[3] += 4    
                elif callback.data=="five14": 
                    technozhr[0] += 5
                    technozhr[3] += 5    
                bot.edit_message_text(arr[15], callback.message.chat.id, callback.message.message_id, reply_markup=markup15)

    elif callback.data=="one15" or callback.data=="two15" or callback.data=="three15" or callback.data=="four15" or callback.data=="five15":
                if callback.data=="one15":
                    alchemist[0] += 1
                    alchemist[2] += 1
                elif callback.data=="two15": 
                    alchemist[0] += 2
                    alchemist[2] += 2    
                elif callback.data=="three15":
                    alchemist[0] += 3
                    alchemist[2] += 3
                elif callback.data=="four15":
                    alchemist[0] += 4
                    alchemist[2] += 4
                elif callback.data=="five15": 
                    alchemist[0] += 5
                    alchemist[2] += 5
                bot.edit_message_text(arr[16], callback.message.chat.id, callback.message.message_id, reply_markup=markup16)

    elif callback.data=="one16" or callback.data=="two16" or callback.data=="three16" or callback.data=="four16" or callback.data=="five16":
                if callback.data=="one16":
                    alchemist[0] += 1
                    alchemist[3] += 1
                elif callback.data=="two16": 
                    alchemist[0] += 2
                    alchemist[3] += 2
                elif callback.data=="three16":
                    alchemist[0] += 3
                    alchemist[3] += 3
                elif callback.data=="four16":
                    alchemist[0] += 4
                    alchemist[3] += 4
                elif callback.data=="five16": 
                    alchemist[0] += 5
                    alchemist[3] += 5
                bot.edit_message_text(arr[17], callback.message.chat.id, callback.message.message_id, reply_markup=markup17)

    elif callback.data=="one17" or callback.data=="two17" or callback.data=="three17" or callback.data=="four17" or callback.data=="five17":
                if callback.data=="one17":
                    alchemist[0] += 1
                    alchemist[4] += 1
                elif callback.data=="two17": 
                    alchemist[0] += 2
                    alchemist[4] += 2   
                elif callback.data=="three17":
                    alchemist[0] += 3
                    alchemist[4] += 3   
                elif callback.data=="four17":
                    alchemist[0] += 4
                    alchemist[4] += 4    
                elif callback.data=="five17": 
                    alchemist[0] += 5
                    alchemist[4] += 5   
                bot.edit_message_text(arr[18], callback.message.chat.id, callback.message.message_id, reply_markup=markup18)

    elif callback.data=="one18" or callback.data=="two18" or callback.data=="three18" or callback.data=="four18" or callback.data=="five18":
                if callback.data=="one18":
                    technozhr[0] += 1
                    technozhr[4] += 1
                elif callback.data=="two18": 
                    technozhr[0] += 2
                    technozhr[4] += 2   
                elif callback.data=="three18":
                    technozhr[0] += 3
                    technozhr[4] += 3    
                elif callback.data=="four18":
                    technozhr[0] += 4
                    technozhr[4] += 4   
                elif callback.data=="five18": 
                    technozhr[0] += 5
                    technozhr[4] += 5    
                bot.edit_message_text(arr[19], callback.message.chat.id, callback.message.message_id, reply_markup=markup19)

    elif callback.data=="one19" or callback.data=="two19" or callback.data=="three19" or callback.data=="four19" or callback.data=="five19":
                if callback.data=="one19":
                    keep_soul[0] += 1
                    keep_soul[3] += 1
                elif callback.data=="two19": 
                    keep_soul[0] += 2
                    keep_soul[3] += 2    
                elif callback.data=="three19":
                    keep_soul[0] += 3
                    keep_soul[3] += 3    
                elif callback.data=="four19":
                    keep_soul[0] += 4
                    keep_soul[3] += 4   
                elif callback.data=="five19": 
                    keep_soul[0] += 5
                    keep_soul[3] += 5    
                bot.edit_message_text(arr[20], callback.message.chat.id, callback.message.message_id, reply_markup=markup20)

    elif callback.data=="one20" or callback.data=="two20" or callback.data=="three20" or callback.data=="four20" or callback.data=="five20":
                if callback.data=="one20":
                    technomag[0] += 1
                    technomag[2] += 1
                elif callback.data=="two20": 
                    technomag[0] += 2
                    technomag[2] += 2   
                elif callback.data=="three20":
                    technomag[0] += 3
                    technomag[2] += 3    
                elif callback.data=="four20":
                    technomag[0] += 4
                    technomag[2] += 4    
                elif callback.data=="five20": 
                    technomag[0] += 5
                    technomag[2] += 5    
                bot.edit_message_text(arr[21], callback.message.chat.id, callback.message.message_id, reply_markup=markup21)

    elif callback.data=="one21" or callback.data=="two21" or callback.data=="three21" or callback.data=="four21" or callback.data=="five21":
                if callback.data=="one21":
                    technomag[0] += 1
                    technomag[3] += 1
                elif callback.data=="two21": 
                    technomag[0] += 2
                    technomag[3] += 2    
                elif callback.data=="three21":
                    technomag[0] += 3
                    technomag[3] += 3    
                elif callback.data=="four21":
                    technomag[0] += 4
                    technomag[3] += 4    
                elif callback.data=="five21": 
                    technomag[0] += 5
                    technomag[3] += 5    
                bot.edit_message_text(arr[22], callback.message.chat.id, callback.message.message_id, reply_markup=markup22)

    elif callback.data=="one22" or callback.data=="two22" or callback.data=="three22" or callback.data=="four22" or callback.data=="five22":
                if callback.data=="one22":
                    oracle[0] += 1
                    oracle[4] += 1
                elif callback.data=="two22": 
                    oracle[0] += 2
                    oracle[4] += 2
                elif callback.data=="three22":
                    oracle[0] += 3
                    oracle[4] += 3    
                elif callback.data=="four22":
                    oracle[0] += 4
                    oracle[4] += 4    
                elif callback.data=="five22": 
                    oracle[0] += 5
                    oracle[4] += 5    
                bot.edit_message_text(arr[23], callback.message.chat.id, callback.message.message_id, reply_markup=markup23) 

    elif callback.data=="one23" or callback.data=="two23" or callback.data=="three23" or callback.data=="four23" or callback.data=="five23":
                if callback.data=="one23":
                    keep_civil[0] += 1
                    keep_civil[4] += 1
                elif callback.data=="two23": 
                    keep_civil[0] += 2
                    keep_civil[4] += 2    
                elif callback.data=="three23":
                    keep_civil[0] += 3
                    keep_civil[4] += 3    
                elif callback.data=="four23":
                    keep_civil[0] += 4
                    keep_civil[4] += 4    
                elif callback.data=="five23": 
                    keep_civil[0] += 5
                    keep_civil[4] += 5    
                bot.edit_message_text(arr[24], callback.message.chat.id, callback.message.message_id, reply_markup=markup24)

    elif callback.data=="one24" or callback.data=="two24" or callback.data=="three24" or callback.data=="four24" or callback.data=="five24":
                if callback.data=="one24":
                    keep_civil[0] += 1
                    keep_civil[5] += 1
                elif callback.data=="two24": 
                    keep_civil[0] += 2
                    keep_civil[5] += 2    
                elif callback.data=="three24":
                    keep_civil[0] += 3
                    keep_civil[5] += 3    
                elif callback.data=="four24":
                    keep_civil[0] += 4
                    keep_civil[5] += 4    
                elif callback.data=="five24": 
                    keep_civil[0] += 5
                    keep_civil[5] += 5    
                bot.edit_message_text(arr[25], callback.message.chat.id, callback.message.message_id, reply_markup=markup25)

    elif callback.data=="one25" or callback.data=="two25" or callback.data=="three25" or callback.data=="four25" or callback.data=="five25":
                if callback.data=="one25":
                    keep_soul[0] += 1
                    keep_soul[4] += 1
                elif callback.data=="two25": 
                    keep_soul[0] += 2
                    keep_soul[4] += 2    
                elif callback.data=="three25":
                    keep_soul[0] += 3
                    keep_soul[4] += 3    
                elif callback.data=="four25":
                    keep_soul[0] += 4
                    keep_soul[4] += 4    
                elif callback.data=="five25": 
                    keep_soul[0] += 5
                    keep_soul[4] += 5    
                bot.edit_message_text(arr[26], callback.message.chat.id, callback.message.message_id, reply_markup=markup26)

    elif callback.data=="one26" or callback.data=="two26" or callback.data=="three26" or callback.data=="four26" or callback.data=="five26":
                if callback.data=="one26":
                    keep_world[0] += 1
                    keep_world[3] += 1
                elif callback.data=="two26": 
                    keep_world[0] += 2
                    keep_world[3] += 2    
                elif callback.data=="three26":
                    keep_world[0] += 3
                    keep_world[3] += 3    
                elif callback.data=="four26":
                    keep_world[0] += 4
                    keep_world[3] += 4    
                elif callback.data=="five26": 
                    keep_world[0] += 5
                    keep_world[3] += 5    
                bot.edit_message_text(arr[27], callback.message.chat.id, callback.message.message_id, reply_markup=markup27)

    elif callback.data=="one27" or callback.data=="two27" or callback.data=="three27" or callback.data=="four27" or callback.data=="five27":
                if callback.data=="one27":
                    oracle[0] += 1
                    oracle[5] += 1
                elif callback.data=="two27": 
                    oracle[0] += 2
                    oracle[5] += 2    
                elif callback.data=="three27":
                    oracle[0] += 3
                    oracle[5] += 3    
                elif callback.data=="four27":
                    oracle[0] += 4
                    oracle[5] += 4    
                elif callback.data=="five27": 
                    oracle[0] += 5
                    oracle[5] += 5   
                bot.edit_message_text(arr[28], callback.message.chat.id, callback.message.message_id, reply_markup=markup28) 

    elif callback.data=="one28" or callback.data=="two28" or callback.data=="three28" or callback.data=="four28" or callback.data=="five28":
                if callback.data=="one28":
                    keep_world[0] += 1
                    keep_world[4] += 1
                elif callback.data=="two28": 
                    keep_world[0] += 2
                    keep_world[4] += 2    
                elif callback.data=="three28":
                    keep_world[0] += 3
                    keep_world[4] += 3       
                elif callback.data=="four28":
                    keep_world[0] += 4
                    keep_world[4] += 4       
                elif callback.data=="five28": 
                    keep_world[0] += 5
                    keep_world[4] += 5    
                bot.edit_message_text(arr[29], callback.message.chat.id, callback.message.message_id, reply_markup=markup29)   

    elif callback.data=="one29" or callback.data=="two29" or callback.data=="three29" or callback.data=="four29" or callback.data=="five29":
                if callback.data=="one29":
                    technomag[0] += 1
                    technomag[4] += 1
                elif callback.data=="two29": 
                    technomag[0] += 2
                    technomag[4] += 2    
                elif callback.data=="three29":
                    technomag[0] += 3
                    technomag[4] += 3    
                elif callback.data=="four29":
                    technomag[0] += 4
                    technomag[4] += 4    
                elif callback.data=="five29": 
                    technomag[0] += 5
                    technomag[4] += 5   
                bot.edit_message_text(arr[30], callback.message.chat.id, callback.message.message_id, reply_markup=markup30) 

    elif callback.data=="one30" or callback.data=="two30" or callback.data=="three30" or callback.data=="four30" or callback.data=="five30":
                if callback.data=="one30":
                    keep_world[0] += 1
                    keep_world[5] += 1
                elif callback.data=="two30": 
                    keep_world[0] += 2
                    keep_world[5] += 2    
                elif callback.data=="three30":
                    keep_world[0] += 3
                    keep_world[5] += 3    
                elif callback.data=="four30":
                    keep_world[0] += 4
                    keep_world[5] += 4    
                elif callback.data=="five30": 
                    keep_world[0] += 5
                    keep_world[5] += 5   
                bot.edit_message_text(arr[31], callback.message.chat.id, callback.message.message_id, reply_markup=markup31)  

    elif callback.data=="one31" or callback.data=="two31" or callback.data=="three31" or callback.data=="four31" or callback.data=="five31":
                if callback.data=="one31":
                    keep_soul[0] += 1
                    keep_soul[5] += 1
                elif callback.data=="two31": 
                    keep_soul[0] += 2
                    keep_soul[5] += 2    
                elif callback.data=="three31":
                    keep_soul[0] += 3
                    keep_soul[5] += 3    
                elif callback.data=="four31":
                    keep_soul[0] += 4
                    keep_soul[5] += 4    
                elif callback.data=="five31": 
                    keep_soul[0] += 5
                    keep_soul[5] += 5    
                bot.edit_message_text(arr[32], callback.message.chat.id, callback.message.message_id, reply_markup=markup32)

    elif callback.data=="one32" or callback.data=="two32" or callback.data=="three32" or callback.data=="four32" or callback.data=="five32":
                if callback.data=="one32":
                    technomag[0] += 1
                    technomag[5] += 1
                elif callback.data=="two32": 
                    technomag[0] += 2
                    technomag[5] += 2    
                elif callback.data=="three32":
                    technomag[0] += 3
                    technomag[5] += 3    
                elif callback.data=="four32":
                    technomag[0] += 4
                    technomag[5] += 4    
                elif callback.data=="five32": 
                    technomag[0] += 5
                    technomag[5] += 5    
                bot.edit_message_text(arr[33], callback.message.chat.id, callback.message.message_id, reply_markup=markup33)
        
    elif callback.data=="one33" or callback.data=="two33" or callback.data=="three33" or callback.data=="four33" or callback.data=="five33":
                if callback.data=="one33":
                    alchemist[0] += 1
                    alchemist[5] += 1
                elif callback.data=="two33": 
                    alchemist[0] += 2
                    alchemist[5] += 2   
                elif callback.data=="three33":
                    alchemist[0] += 3
                    alchemist[5] += 3    
                elif callback.data=="four33":
                    alchemist[0] += 4
                    alchemist[5] += 4    
                elif callback.data=="five33": 
                    alchemist[0] += 5
                    alchemist[5] += 5  
                bot.edit_message_text(arr[34], callback.message.chat.id, callback.message.message_id, reply_markup=markup34)

    elif callback.data=="one34" or callback.data=="two34" or callback.data=="three34" or callback.data=="four34" or callback.data=="five34":
                if callback.data=="one34":
                    technozhr[0] += 1
                    technozhr[5] += 1
                elif callback.data=="two34": 
                    technozhr[0] += 2
                    technozhr[5] += 2    
                elif callback.data=="three34":
                    technozhr[0] += 3
                    technozhr[5] += 3    
                elif callback.data=="four34":
                    technozhr[0] += 4
                    technozhr[5] += 4    
                elif callback.data=="five34": 
                    technozhr[0] += 5
                    technozhr[5] += 5    

                result = ["", "", ""]
                arr2 = [technozhr[0], keep_soul[0], alchemist[0], oracle[0], technomag[0], keep_civil[0], keep_world[0]]
                f = arr2.index(max(arr2)) 
                
                technozhr[0] = -1
                keep_soul[0] = -1
                alchemist[0] = -1
                oracle[0] = -1
                technomag[0] = -1
                keep_civil[0] = -1
                keep_world[0] = -1
                
                direct = 0
                     
                if f == 0:
                    result[0] = "Техножрец ⚙️"
                    direct = technozhr.index(max(technozhr))
                    result[1] = directs[5 * f + direct]
                    result[2] = "Техномаги и техножрецы живут среди машин. Они создают внутри Вселенной отдельный мир машин и механизмов. Техножрецы - настоящие заклинатели и хранители машин. Они делают реальным то, что техномаги придумали и нарисовали, но только техножрецы знают, на какие кнопки нажать, чтобы машина заработала как надо. Техножрецы живут в кузницах и мастерских, в которых собирают машины и механизмы, чинят их, совершенствуют и управляют ими. Машины для них как дети, они заботятся о них, учат их говорить, общаться друг с другом и с жителями Вселенной. Техножрецы могут говорить с машинами на одном языке и создавать заклинания, которые позволяют жителям Вселенной отдавать им команды."
                elif f == 1:
                    result[0] = "Хранитель души 📚" 
                    direct = keep_soul.index(max(keep_soul))
                    result[1] = directs[5 * f + direct]
                    result[2] = "Хранители души и тела живут в уютных домиках на окраинах селений. К ним приходят жители Вселенной, когда им нужна помощь в излечении или укреплении их духа и тела. Только они знают, как устроен человек и его внутренний мир, могут помочь разобраться в себе и других, сохранить любовь и взаимопонимание в семьях, гармонично развить личность ребенка. Иногда хранители души выходят из своих домиков, идут на ярмарочную площадь, где рассказывают и обучают жителей Вселенной тому, как и детям, и взрослым быть здоровыми, активными и счастливыми."
                elif f == 2:
                    result[0] = "Алхимик ⚗️" 
                    direct = alchemist.index(max(alchemist))
                    result[1] = directs[5 * f + direct]
                    result[2] = "Алхимики живут в лабораториях на окраине Вселенной, наполненных аккуратно расставленными пробирками, колбами, реактивами и измерительными приборами (которые иногда представляют собой целое здание). Их влечет к познанию основ мироздания. Они исследуют, как и из чего создан этот мир от самых маленьких частиц до звезд и устройства Вселенной, по каким законам он работает, а потом разбирают его “по кирпичикам”, чтобы сделать из найденных веществ разные интересные материалы, которые пригодятся жителям Вселенной."
                elif f == 3:
                    result[0] = "Оракул 🔮" 
                    direct = oracle.index(max(oracle))
                    result[1] = directs[5 * f + direct]
                    result[2] = "Оракулы - повелители чисел, они живут в небесных башнях на пересечении потоков информации, порождаемой жителями Вселенной, где черпают данные для своих предсказаний, которые очень нужны жителям Вселенной."
                elif f == 4:
                    result[0] = "Техномаг 👨‍💻" 
                    direct = technomag.index(max(technomag))
                    result[1] = directs[5 * f + direct]
                    result[2] = "Техномаги и техножрецы живут среди машин. Они создают внутри Вселенной отдельный мир машин и механизмов. Техномаги находят себе тихий уголок, где можно день и ночь в одиночестве мечтать о новых машинах и механизмах, придумывать и рисовать их "
                elif f == 5:
                    result[0] = "Хранитель цивилизации 🗺️" 
                    direct = keep_civil.index(max(keep_civil))
                    result[1] = directs[5 * f + direct]
                    result[2] = "Хранители цивилизации живут среди людей, наблюдают за тем, чего им не хватает, а потом идут в далекие земли, где живут в палатках и добывают ресурсы для развития цивилизации. Они возводят города, охраняют и оберегают природу, следят за разумным использованием добытых ресурсов для того, чтобы всем жителям Вселенной хватило тепла, энергии, еды и чистой воды, миру машин - топлива, а человеческая цивилизация продолжала существовать и не погибла из-за того, что во Вселенной закончились ресурсы и её переполнило отходами."
                elif f == 6:
                    result[0] = "Хранитель мира 🌐"
                    direct = keep_world.index(max(keep_world))
                    result[1] = directs[5 * f + direct]
                    result[2] = "Жители Вселенной, представители разных гильдий живут бок о бок, обмениваются полезной информацией и произведенными товарами, а иногда конкурируют и спорят друг с другом из-за территории и ресурсов. Часто им бывает сложно договориться между собой, потому что у них противоположные интересы или говорят они на разных языках. Жители Вселенной для того, чтобы сохранить мир и понять друг друга, зовут на помощь хранителей мира, которые живут среди людей и стараются быть как можно ближе к ним. Только они могут найти общий язык с любым человеком, понять его, помочь людям договориться, обойти острые углы, совершить выгодные сделки и защитить интересы каждого."
                
                faculty = result[0]
                direction = result[1]
                global resd
 
                match direction:
                    case 'Электроэнергетика и электротехника ⚡':
                        resd = 'Цивилизация жителей Вселенной постоянно развивается, потребности в энергии постоянно растут, а запасы ископаемого топлива не безграничны. Мастера электроэнергетики  и электротехники смотрят на Вселенную и видят бесконечные запасы энергии, которые есть в каждой земной стихии, и задаются вопросом: зачем копать глубокие шахты в поисках остатка угля, если можно делать энергию прямо из воздуха? Как правило, жители Вселенной не задумываются о том, откуда в их уютных жилищах чудесным образом появляются свет и тепло, а тем временем мастера электроэнергетики и электротехники постоянно придумывают все новые и новые способы и магические преобразователи, которые превращают энергию Вселенной в электричество и доставляют его жителям Вселенной прямо в дом. Кроме того, жители Вселенной привыкли к тому, что электричество в розетке не заканчивается, и тратят его сверх меры, включая одновременно вентилятор и обогреватель, но мастера электроэнергетики и электротехники знают, что невозможно добыть энергию без вреда для планеты, поэтому ее надо беречь. Они неустанно работают над тем, чтобы найти способ получения энергии, который будет максимально экономичным, безопасным и безвредным для человека и природы.'
                    case 'Авиастроение ✈️':
                        resd = 'Давным-давно люди мечтали научиться летать. Они думали о том, как подняться в небо, и с завистью смотрели на птиц, парящих высоко над ними. Осуществить эту мечту им помогли мастера авиастроения. Они знают, как вознестись к Солнцу и не сгореть, поднять в воздух тяжелые грузы и доставить их в нужную точку Вселенной, присматривают новые материалы, чтобы сделать летающие суда легкими и прочными и придумывают как летать еще выше, быстрее и безопаснее. Благодаря мастерам авиастроения для жителей Вселенной началась захватывающая эра воздухоплавания. Поднимая в воздух шары, дирижабли, цеппелины и этажерки, люди смогли увидеть Вселенную с высоты птичьего полета.Сейчас авиационный транспорт самый удобный, комфортный, высокоскоростной и безопасный. Никто уже не удивляется тому, что самолеты переносят их в любую точку мира легко и быстро. Кроме того, мастера авиастроения придумали беспилотные летательные аппараты, которые стали незаменимыми помощниками для жителей Вселенной не только в мирное время, но и охранниками порядка и мира в неспокойные времена. Эти летающие автоматические роботы помогут запечатлеть праздник, красивые виды, осуществить поиск потерявшихся людей, доставить грузы, следить за порядком в городе, обеспечить безопасность и спокойствие жителей Вселенной и много другое. Мастера авиастроения сделали реальным то, что казалось невозможным – парить рядом с птицами и даже выше них. Теперь жители Вселенной могут почувствовать себя как рыба в воде не только в воздухе, но и в космическом пространстве. Однажды мастерам авиастроения удастся построить и запустить такой летательный аппарат, который позволит осуществлять регулярные космические полеты жителей Вселенной на другие планеты.'
                    case 'Конструирование и технология электронных средств ⚙️':
                        resd = 'Жители Вселенной на протяжении тысячелетий делали все собственными руками, а потом мастера конструирования и технологии электронных средств начали создавать машины, которые делали бы за них нудную  рутинную работу. Они смогли создать мозги для умных машин, и так увлеклись, что стали демиургами кремниевой эволюции. Раньше умные машины были медленными, неповоротливыми тугодумами, размером с целую комнату, теперь они легко помещаются в кармане и решают сложнейшие задачи в мгновение ока. Благодаря мастерам конструирования и технологии электронных средств машины стали такими умными, что могут не только выполнять сложные команды, но и самостоятельно принимать решения, взяв на себя заботу о безопасности и комфорте жителей Вселенной через системы умного дома, умного производства и умного города. '
                    case 'Автоматизация технологических процессов и производств 🤖':
                        resd = 'Когда-то давным-давно абсолютно все вещи во Вселенной делались руками ее жителей, и это был тяжелый и монотонный труд. И тогда мастера автоматизации технологических процессов и производств создали роботов для помощи жителям Вселенной, которые теперь могут почти все: и испечь хлеб, и собрать автомобиль, и заменить человека в опасных условиях труда. Но роботы – просто послушные и верные помощники, они не могут придумать сами, чем бы им заняться, и мастера автоматизации технологических процессов и производств объясняют им, что и как нужно делать, придумывают как изменить конструкцию робота, чтобы он лучшим образом справлялся с конкретной работой. Благодаря им многие вещи, которыми пользуются жители Вселенной, стали качественнее, безопаснее, дешевле и доступнее. Мастера автоматизации технологических процессов и производств мечтают о том, что когда-нибудь человек будет работать только ради удовольствия, а не из-за необходимости.'
                    case 'Информационные системы и технологии 💻':
                        resd = 'Информационные технологии во Вселенной стремительно развиваются, создавая отдельный виртуальный мир, полностью состоящий из информации. Кто владеет информацией, тот управляет миром. Так информация становится таким же ценным ресурсом, как и природные. Информационные моря Вселенной бороздят опасные цифровые пираты и разбойники, которые могут внезапно атаковать любую умную машину, подкладывая логические бомбы, заражая опасными вирусами, запуская хитрых червей и троянских коней, грабить трюмы с информацией, взять в плен файлы, вымогая за них деньги, украсть ваш аккаунт в социальной сети и деньги в цифровом банке, или взять умную машину на абордаж, и даже зомбировать ее, подчиняя своей темной воле. Каждый житель Вселенной хочет быть уверенным, что встреча с разбойником не грозит ему, когда он подключается к всемирной паутине. Мастера информационных систем и технологий стоят на страже порядка виртуального мира, защищая жителей Вселенной от посягательств злобных пиратов. Они знают тайный язык криптографии, создают надежные защищенные информационные системы, которые вмещают в себя всю информацию Вселенной от фото сегодняшнего завтрака до карты урановых месторождений. И чтобы жители Вселенной не потерялись в море информации, мастера информационных систем и технологий наводят в них порядок, раскладывая по полочкам и давая названия, для того, чтобы ее было легко найти. А чтобы ни один пират не догадался, что вы ели на завтрак, они кодируют ее хитрым шифром.'
                    case 'Системный анализ и управление 📊':
                        resd = ' '
                    case 'Лингвистика 💬':
                        resd = 'Вселенная подобна котлу, в котором варятся разные народы со своей культурой и языком. Общение народов позволяет каждому обогатиться новыми знаниями, но порой этому мешают языковые барьеры и недопонимания. Мастерам лингвистики не страшно Вавилонское многоголосье языков, так как они могут понять каждого, изложить любую диковинную речь и текст другому человеку на его языке и даже помочь освоить всем желающим языки чужеземцев. Мастера лингвистики могут познавать мир, общаясь с интересными людьми из других стран, чувствовать себя как дома в любой стране, будто бы  границ между странами для них не существует. В языковой стихии они чувствуют себя как рыба в воде, но язык для них не просто способ общения, а целый мир, полный очарования и волшебства. Они раскрывают секреты речи, рассматривают каждое слово как драгоценный бриллиант, изучают, откуда оно взялось и как развивалось, постигая его истинную суть и смысл. Когда-нибудь благодаря мастерам лингвистики все жители Вселенной смогут понимать речь и культурные традиции друг друга. '
                    case 'Психология 🧠':
                        resd = 'Человеческая психика таит в себе не меньше загадок, чем космическое пространство. Мастера психологии наблюдают за поведением людей и ставят эксперименты, погружаясь в тайны психики, чтобы понять, как устроен разум человека. Зная секреты устройства человеческой души, мастера психологии могут подсказать жителям Вселенной как сделать их жизнь лучше. Жители Вселенной всегда могут обратиться к мастерам психологии за помощью в тяжелые моменты своей жизни, чтобы лучше понять себя и свои желания, выйти из кризиса, разрешить конфликт, улучшить свой эмоциональный интеллект, справиться со стрессом, проблемами в семье, на работе или в учебе или с другими сложностями человеческого бытия. Мастера психологии однажды найдут способ, чтобы каждый житель Вселенной смог жить осознанной, гармоничной и счастливой жизнью.'
                    case 'Клиническая психология 🧠':
                        resd = 'Как не бывает одинаковых снежинок, так не бывает и одинаковых душ. Иногда во Вселенной появляются страдающие души, которые сильно отличаются от других, и им бывает сложно найти свое место во Вселенной, а мастера клинической психологии стремятся их понять и помочь им. Причинами таких отличий могут быть болезни тела и души.Мастеров клинической психологии интересует откуда берутся такие аномалии души и тела, как они устроены. Они способны определить эти болезни, отследить их развитие и совместно с врачевателями тел и душ исправить то, что возможно. Не каждую душу можно исправить, но ее можно научить жить в гармонии с собой и окружающими. Когда-нибудь благодаря мастерам клинической психологии у каждого жителя Вселенной будет шанс жить полной жизнью и реализовывать свои таланты несмотря на болезнь.'
                    case 'Юриспруденция 💼':
                        resd = 'Основой развития Вселенной является мир и согласие между ее жителями, но договориться им между собой порой бывает очень сложно, так как каждый имеет свое представление о правде и справедливости. Мастера юриспруденции призваны урегулировать взаимоотношения, возникающие среди жителей Вселенной, разрешить конфликты и сгладить недовольства. И тогда во Вселенной появляются соглашения, договоры, своды правил и законов, которые помогают удерживать хрупкое равновесие мира. Каждый  хочет, чтобы соблюдались его интересы, но иногда они могут противоречить интересам других людей, и тогда они обращаются к мастерам юриспруденции, рыцарям закона и справедливости. Мастера юриспруденции виртуозно разбираются в законах и умеют применять их, выполняя благородную миссию защиты прав, чести и достоинства  людей, так как  не каждый житель Вселенной может сделать это самостоятельно. Их пытливый ум позволяет находить и наказывать правонарушителей, восстанавливая порядок в обществе. Когда-нибудь мастера юриспруденции придумают такие законы и правила поведения в обществе, с которыми все будут согласны и станут их соблюдать.'
                    case 'Химия 🧪':
                        resd = 'Мастера химии интересуются тем, из чего состоит мир вокруг, и познают его через тончайшие связи атомов и молекул. Они постигают природу веществ и реакций между ними, умеют раскладывать вещества на более простые компоненты, изучают взаимопревращение веществ и их новые свойства. Дни напролет тщательно анализируют и систематизируют свойства элементов, а по ночам спят и видят как новый открытый элемент будет занесен в таблицу. В недрах своих лабораторий мастера химии соединяют вещества для получения причудливых реакций. Из череды взрывов и осколков колб от неудавшихся экспериментов, однажды рождается новое вещество. Сотворенные ими соединения  помогают жителям Вселенной поддерживать здоровье и красоту, из прочных и легких материалов создавать разные нужные вещи, строить здания и машины.'
                    case 'Ядерная физика и технологии ☢️':
                        resd = 'Мастеров ядерной физики и технологий интересуют атомы, из которых состоит Вселенная. В своих затейливых экспериментах они сталкивали эти мельчайшие частички между собой и смотрели, что из этого получается. В результате своих игр с материей Вселенной они обнаружили, что при столкновении может высвободиться колоссальное количество энергии, которая может привести к ужасающему взрыву и стать разрушительным оружием. И тогда мастера ядерной физики и технологий осознали, что атом не солдат, а рабочий, и должен служить мирным нуждам жителей Вселенной, давая тепло, свет и горячую воду в дома и излечивая от страшных заболеваний. Изучая свойства атома, они установили, что излучение в больших количествах может быть смертельно опасным для жителей Вселенной, поэтому они несут постоянный дозор, отслеживая радиационный фон планеты, и придумывают способы как защитить отважных астронавтов от космической радиации. Нельзя переоценить то, что делают мастера ядерной физики и технологий, ведь от их действий зависит существование всей Вселенной. Они мечтают о том, что когда-то смогут поймать “божественную” частицу.'
                    case 'Химия, физика и механика материалов 🔬':
                        resd = 'Мастера химии, физики и механики материалов поглощены происходящим на стыке макро- и микромиров. Их интересуют свойства различных материалов, они исследуют их на молекулярном и атомарном уровнях. Но не все материалы, которые встречаются в природе, совершенны и способны удовлетворить нужды жителей Вселенной, и тогда мастера химии, физики и механики материалов на молекулярном уровне преобразуют Вселенную, изобретают технологии, неотличимые от магии, придумывая способы создания новых материалов с волшебными свойствами и изготавливают их. С помощью этих материалов жители Вселенной могут делать удивительные вещи, даже невообразимо маленьких размеров, которые не видны человеческому глазу. Однажды в лабораториях мастеров химии, физики и механики материалов родятся новые существа - графеновые кентавры и наноботы, которые преодолеют грань между искусственным и живым мирами.'
                    case 'Физика ⚛️':
                        resd = 'Мастера физики способны мыслить о том, что не укладывается в голове у других жителей Вселенной. Их интересует как устройство видимого мира, который можно потрогать, так и мир невидимый, который можно только вообразить. Они изучают и далекие огромные объекты, которые можно увидеть только в телескоп, и самые маленькие частички, которые не разглядеть даже в микроскоп. Мастера физики способны описать красоту Вселенной с помощью формул и уравнений, а чтобы другие мастера смогли в них разобраться, они создают понятные иллюстрации. Мастера физики уже научились управлять потоком частиц, скоро придумают как покорять далекие планеты и однажды смогут найти ответы на вопросы как устроена Вселенная, кто ее придумал и существуют ли параллельные миры.'
                    case 'Социология':
                        resd = 'Мастера социологии владеют тайным искусством вопрошания. Собранные ответы они обрабатывают и анализируют с помощью умных машин, и способны не только разобраться в происходящем, но и могут почувствовать настроение жителей Вселенной и предсказать развитие событий в обществе. Мастера социологии исследуют, что необходимо и интересно жителям Вселенной, что помогает организациям и предприятиям исполнять их желания. Другие мастера обращаются за помощью к ним, чтобы подобрать себе хороших помощников. Мастера социологии знают секреты того, как создать привлекательный образ не только какого-либо товара или услуги, но и умеют сотворить волшебную ауру любому жителю Вселенной.'
                    case 'Государственное и муниципальное управление 🏛️':
                        resd = 'Мастера государственного и муниципального управления умеют создавать условия для слаженной работы жителей Вселенной в больших и маленьких организациях или управлять работой целого города. Управляя работой города, они призваны защищать права и прислушиваться к просьбам и пожеланиям жителей Вселенной о том, что где-то что-то нужно починить, исправить, наладить. С помощью умных машин мастера государственного и муниципального управления анализируют эти просьбы и пожелания, быстро и эффективно решают возникающие у жителей Вселенной проблемы, и даже могут предсказать и не допустить их возникновения, делая город умным.'
                    case 'Фундаментальная информатика и информационные технологии 📡':
                        resd = 'Информация бывает такой сложной, или ее бывает так много, что одна умная машина не способна справиться с ее обработкой. Тогда мастера фундаментальной информатики и информационных технологий  объединяют машины в большие, сложные и защищенные от чужого вторжения сети, чтобы они сообща решали эту трудную задачу. Кроме того, мастера фундаментальной информатики и информационных технологий знают языки машин, помогают жителям Вселенной найти с машинами общий язык и даже могут терпеливо объяснить, на какую кнопку для этого надо нажать. Умные машины под руководством мастеров фундаментальной информатики и информационных технологий постепенно становятся все умнее, и быть может, когда-то обретут собственный разум. '
                    case 'Бизнес-информатика 📊':
                        resd = 'Торговля - двигатель развития Вселенной, и она порождает огромный поток информации, из  которого  мастера бизнес-информатики умеют выделить сведения, важные для эффективной работы предприятия.\n' + 'Они создают программы для умных машин, которые помогают спрогнозировать, как будет развиваться рынок, сколько потребуется людей и материалов, как преобразовать рабочие процессы в четкие алгоритмы, чтобы организации и предприятия стали более успешными в производстве и торговле.'
                    case 'Информатика и вычислительная техника 👨‍💻':
                        resd = 'Умные машины стали важной частью жизни жителей Вселенной.\n' + ' Они умеют общаться между собой и даже собираться во всемирную сеть, которая окутывает всю Вселенную. И пока мастера физики ищут параллельные миры, мастера информатики и вычислительной техники создают свой собственный  виртуальный мир безграничных возможностей, открытый для каждого жителя Вселенной, в котором можно общаться, учиться, работать и развлекаться, не выходя при этом из дома. Они придумывают программы для умных машин, которые помогают им понимать то, что от них хотят жители Вселенной, делают эти программы удобными для использования, превращая безликие нули и единицы в красивые и понятные кнопки. Благодаря мастерам информатики и вычислительной техники сейчас у каждого жителя Вселенной в кармане лежит маленькая умная машина, при помощи которой они могут в любой момент обратиться к великой всемирной паутине и узнать ответ на главный вопрос жизни, Вселенной и всего такого, или просто быть рядом друг с другом прямо сейчас, даже если на самом деле находятся на разных концах света. Виртуальная жизнь жителей Вселенной создает огромный массив данных, которым мастера информатики и вычислительной техники умеют ловко управлять. Они, как бойцы невидимого фронта, сохраняют его и защищают от злоумышленников. Мастера информатики и вычислительной техники мечтают о том, что когда-нибудь они смогут создать метавселенную, которая окончательно сотрет границы между реальным и виртуальным мирами, и станет общим, комфортным пространством для всех.'
                    case 'Программная инженерия 👨‍💻':
                        resd = 'Еще с древних времен жители Вселенной не перестают исследовать мироздание и узнают о нем все больше удивительных вещей и фактов, которые невозможно осмыслить одним только человеческим интеллектом. И тогда на помощь жителям Вселенной приходят умные машины, которые помогают им провести точные и сложные расчеты.\n' + 'Мастера программной инженерии учат умные машины решать сразу много сложных задач и не сходить с ума от перегрева. Только они понимают внутренний мир машины, знают магические слова, с помощью которых могут объяснить ей что необходимо делать, даруют ей ее истинное предназначение. Перед мастерами программной инженерии постоянно встает все больше и больше запросов от жителей Вселенной, которые сподвигают их придумывать и изобретать новые волшебные заклятия для умных машин как больших, так и маленьких, с помощью которых они заставляют их выполнять все новые и новые задания. Мастера программной инженерии мечтают когда-нибудь изобрести такие волшебные заклинания, которые помогут умным машинам будущего, работающим на энергии света и тьмы, за секунды решать поставленные перед ними задачи, на которые ушли бы миллионы лет у миллионов мудрецов.  '
                    case 'Прикладная математика и информатика 👨‍💻':
                        resd = 'Жизнь жителей Вселенной порождает много информации, которую нужно собирать, хранить и искать в ней закономерности.\n' + ' Мастера прикладной математики и информатики понимают, что любой процесс можно представить в виде формул и чисел, и знают как это сделать. Они изучают языки умных машин, чтобы отдавать им приказы. Под их управлением умные машины собирают и обрабатывают информацию, хранят ее в надежном месте, а когда необходимо, достают оттуда именно те сведения, которые требуются жителям Вселенной. '
                    case 'Экология и природопользование 🌍':
                        resd = 'Вселенная - общий дом для всех живых существ.\n' + 'Она огромна и прекрасна. В ней есть просторные поля, бескрайние океаны и недры, полные сокровищ. Человек считает себя вершиной эволюции, властителем природы и даже может повернуть реки вспять. И вслед за большой силой приходит большая ответственность: защищать других существ, оберегать Вселенную от катастроф, истощения, разрушения, загрязнения, вымирания. Но, к сожалению, не все жители Вселенной ведут себя разумно, нанося ей непоправимый вред. Некоторые из них думают, что ничего ужасного не случится, если они, например, выбросят разлагаться на свалку устаревшую умную машину или бутылку в море. Но Вселенная лишь кажется бескрайней, а на самом деле она маленькая и хрупкая, и все выброшенное когда-то возвращается обратно: через воду, воздух и почву. Мастера экологии и природопользования пристально следят за тем, чтобы техногенного мусора в море не стало больше чем воды. Спасая планету, они пройдутся по лесам, полям и болотам, залезут в самую зловонную сточную канаву и очистят природу от мусора. Когда мастера других гильдий слишком увлекаются созданием разных интересных штуковин, напоминают им о необходимости сокращать вредные выбросы, занимаясь экопросвещением. Они анализируют, из чего на самом деле состоят воздух, вода и земля, чтобы защитить здоровье человека. Однажды мастера экологии и природопользования при колонизации других планет встанут на острие экспансии и терраформирования и смогут сделать их цветущим садом для себя и своих потомков.'
                    case 'Технология геологической разведки 🗺️':
                        resd = 'Вселенная изобилует природными богатствами.\n' + 'Большинство жителей Вселенной и не  догадываются, что ходят по сокровищам, скрытым от глаз под толщей земли, но только мастера технологии геологической разведки будто способны видеть сквозь землю, могут найти и поднять на поверхность любые ценные ресурсы. Они самые настоящие разведчики недр и залежей полезных ископаемых, их влекут тайны и секреты подземного мира, интересует строение планеты и свойства пород, из которых она состоит. Некоторые мастера технологии геологической разведки большую часть своего времени проводят в путешествиях за тридевять земель по заполярью, пустыням, тайге и высоким горам, собирая и накапливая знания о подземном мире, другие с помощью умных машин на основе собранной информации делают сложные расчеты и составляют карты и модели подземных сокровищниц, в которых спрятаны природные богатства. Они мечтают, чтобы всем жителям Вселенной всегда хватало ресурсов, но не все жители Вселенной бережно относятся к добытым ими полезным ископаемым, бездумно и бездарно расходуя их. Мастера технологии геологической разведки изучили все подземные сокровищницы как свои пять пальцев и знают, что они не бездонны и ресурсы в них не бесконечны. Теперь они обращают свой взор в небо и с нетерпением ждут, когда будет осваиваться космическое пространство, и можно будет спускать с небес на землю новые сокровища, найденные на Луне, астероидах и других планетах.'
                    case 'Прикладная информатика 👨‍💻':
                        resd = 'Когда-то давным-давно жители Вселенной вручную рассчитывали, сколько нужно будет ресурсов для производства, рисовали плакаты, двигали мебель, чтобы посмотреть, как будет смотреться столик у дивана, а сейчас эти задачи может решить умная машина.\n' + 'Многие жители Вселенной до сих пор продолжают все делать по-старинке, зря растрачивая время и силы, совершая ошибки в сложных расчетах с большим количеством данных и переменных. Мастера прикладной информатики могут подсказать жителям Вселенной к какой задаче стоит применить умную машину, чтобы все это сделать проще, быстрее, надежнее и красивее - сверстать газету, создать дизайн сайта, приложения или компьютерной игры, помочь организации оптимизировать работу производства, навести порядок в расчетах. Современные умные машины под руководством мастеров прикладной информатики все больше совершенствуются в решении сложных задач, распознавая предметы, лица, ситуации на дорогах, предсказывая погоду. И теперь каждый житель Вселенной может спросить у личного виртуального помощника, живущего в карманной умной машине, о сегодняшних новостях, погоде и пробках на дорогах, попросить подобрать музыку под настроение.'
                    case 'Экономика 📈':
                        resd = 'Мастера экономики - настоящие повелители финансовых потоков.\n' + 'Там, где другие жители Вселенной видят просто цифры, мастера экономики видят закономерности работы рынка. У них все посчитано. Они не уснут спокойно, пока цифры не сойдутся или не поймут, куда пропали деньги. Вместе с умными машинами мастера экономики строят предсказания о том, будет ли выгодна та или иная сделка, сколько денег получится заработать, куда будет выгодно их вложить. Они понимают, кто что кому продал и сколько еще нужно будет произвести товаров жителям Вселенной для благополучной жизни. '
                
                bot.send_message(callback.message.chat.id, f"Ты {result[0]}! \n\n" + f"{result[2]} \n\n" + f"Твоё направление:\n" + f"{result[1]}\n\n" + f"{resd}")
                
                update_db_table(faculty=faculty, direction=direction, user_id=callback.message.chat.id)
                
                bot.send_message(callback.message.chat.id, 'Хочешь попробывать снова?',  reply_markup = againmrk)
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
    
    elif callback.data=="n":
        for i in range(random.randint(0, 4)):
            match i : 
                case 0: msg = 'Как хочешь.\n' + 'Не мне же поступать в университет. 😒'
                case 1: msg = 'Окей 👌'
                case 2: msg = 'Пока ✌'
                case 3: msg = 'Может всё таки да? 😉'
                case 4: msg = '🤓🤓🤓' 
                case 5: msg = '🤓🤓🤓' 
        bot.send_message(callback.message.chat.id, msg)
    elif callback.data == "nah":
        bot.edit_message_text('Хорошо, твои данные были звписанны! 📝\n\n' + 'Счастливого пути в мир знаний и открытий! 👋📚', callback.message.chat.id, callback.message.message_id)
    
    elif callback.data == 'in':
        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup="")
        bot.send_message(callback.message.chat.id, f"Твое имя {callback.from_user.first_name}?", reply_markup= markupp)
    
    elif callback.data == 'nf':
         bot.edit_message_reply_markup('Окей 👌', callback.message.chat.id, callback.message.message_id, reply_markup="")
         

@bot.message_handler(content_types=['text'])
def get_user_name(message):
    global name 
    name = message.text
    bot.send_message(message.chat.id, "Пожалуйста, введи свою фамилию", parse_mode = 'html')
    bot.register_next_step_handler(message, get_user_surname)

def get_user_surname(message):
    bot.send_message(message.chat.id, "Пожалуйста, введи свою почту 📧", parse_mode = 'html')
    global surname
    surname = message.text
    surname = surname
    
    bot.register_next_step_handler(message, get_email)

def get_email(message):
    bot.send_message(message.chat.id, "Пожалуйста, напиши название твоего населённого пункта 🏠", parse_mode = 'html')    
    global email  
    email = message.text
    email=email
    bot.register_next_step_handler(message, get_city)

def get_city(message):
    bot.send_message(message.chat.id, "Пожалуйста, введи номер твоей школы 🏫", parse_mode = 'html')
    global city
    city = message.text
    city=city
    bot.register_next_step_handler(message, get_school)

def get_school(message):
    bot.send_message(message.chat.id, "И напоследок, напиши номер своего телефона 📞", parse_mode = 'html')
    global school 
    school = message.text
    school=school
    bot.register_next_step_handler(message, get_number)
    
def get_number(message):
    global phone
    global us_id
    global name
    global school
    global email
    global city
    us_id = message.from_user.id
    us_id = us_id
    phone = message.text
    phone = phone

    markup0=types.InlineKeyboardMarkup(row_width=2)
    item1=types.InlineKeyboardButton("Да", callback_data="ye")
    item2=types.InlineKeyboardButton("Нет", callback_data="n")
    markup0.add(item1, item2)

    markupoщ=types.InlineKeyboardMarkup(row_width=2)
    iteme=types.InlineKeyboardButton("Да", callback_data="ye")
    iteme2=types.InlineKeyboardButton("Нет", callback_data="nf")
    markupoщ.add(iteme, iteme2)

    value_to_check = message.chat.id
    info1 = cursor.execute('SELECT * FROM test WHERE user_id=? AND user_name=? AND user_surname=? AND email=? AND city=? AND school=? AND phone=?', (value_to_check, name, surname, email, city, school, phone, )).fetchone()
    if info1 is not None:
        bot.send_message(message.chat.id, 'У вас уже есть аккаунт\n' + 'Желаете начать тест?', reply_markup=markupoщ)
        
    else:
        db_table_val(user_id= message.chat.id, user_name=name, user_surname=surname, email=email, city=city, school=school, phone=phone)
        bot.send_message(message.chat.id, "Ты готов ответить на несколько вопросов? 🤔".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup0)

    

bot.polling(non_stop=True)

#Если проходил тест команда на прохождение снова (проверка на наличе аккаунта)