import telebot
import Obj
from Info import setting
from telebot import types
#from keyboa import Keyboa # кнопки на клаве
#fruits = [
#  "banana", "coconut", "orange",
#  "peach", "apricot", "apple",
#  "pineapple", "avocado", "melon"
#] список кнопок
#kb_fruits = keyboa_maker(items=fruits, copy_text_to_callback=True) создание их
#bot.send_message(
#  chat_id=uid, reply_markup=kb_fruits,
#  text="Please select one of the fruit:") прикрепление


# Инициализация бота и основные обработчики комманд,основная логика в Obj

keys_board = {
'start' : ['/help', '/info', 'tutor'],
'info' : ['/help', '/start', '/tutor', '/play'],
'play' : ['/help'],
'tutor' : ['/help', '/start', '/play'],
}


client = Obj.client()
bot = telebot.TeleBot(setting["token"]);
 
HELP = """
***********************HELP****************************
*/start - создаём ваш аккаунт <3
*/help - команда выводит информацию о возможностях бота
*/play - запускаю режим игры с выбором уровня
*/info - небольшая информация
*******************************************************
"""
information = """
Этот бот предназначен для помощи с составлением примеров
и их решения не/используя сарабан. Приложение делится на 2
вида: подсчёт с использованием сарабана, подсчёт без сарабана на цифрах в голове.
Информация по тому, как правильно использовать сарабан здесь /tutor (в разработке)

на 1 уровне цифры прописываются словами (возможно голосовыми сообщениями,
теоретическая идея), а так же есть визуальный ответ по примеру на сарабане, к каждой
задаче
на 2 уровне сложные примеры на сарабане
на 3 уровне числа такие же прописные (или голосовые сообщения), но без деталей сарабана
на 4 уровне простые цифровые примеры
на 5 уровне сложные цифровые
"""

tutor = """
Счеты представляют собой прямоугольную рамку с вертикальными спицами.
Рамка поделена поперечной перекладиной на две неравные части. На спицах
нанизаны костяшки – снизу по четыре штуки, а сверху по одной. Общее количество
спиц может отличаться в зависимости от модели счетной доски.
<правила особого счёта>
<далее техники передвижения костяшек в сарабане>
"""

"""
@bot.message_handler(commands=["start"])
def inline(message):
    answer = self.client.registration()
    if answer == "Added":
        bot.send_message(message.from_user.id, "Отлично, вы зарегестрированы! Посмотреть мои возможности /help")
        bot.send_message(message.from_user.id, )
        bot.send_message(message.from_user.id, input("Введи сообщение"))
    elif answer == "Been":
        bot.send_message(message.from_user.id, "Ошибка! Вы уже зарегестрированы. Посмотреть мои возможности /help")

    with open('1.jpg', 'rb') as img:
        bot.send_photo(message.chat.id, img)
"""

@bot.message_handler(commands=["help"])
def HELPs(message):
    print("work with help")
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("Start!", callback_data="cb_start"),
               types.InlineKeyboardButton("Info", callback_data="cb_info"),
               types.InlineKeyboardButton("Play!", callback_data="cb_play"),
               types.InlineKeyboardButton("Help again", callback_data="cb_help"))
    bot.send_message(message.from_user.id, HELP, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'cb_start')
def cb_button10(message: types.Message):
    print("work with start")
    bot.delete_message(message.from_user.id, message.message.message_id)
    answer = client.registration()
    if answer == "Added":
        bot.send_message(message.from_user.id, "Отлично, вы зарегестрированы! Посмотреть мои возможности /help", reply_markup=keyboards(keys_board['start']))

        bot.send_message(message.from_user.id, input("Введи сообщение"))
    elif answer == "Been":
        bot.send_message(message.from_user.id, "Ошибка! Вы уже зарегестрированы. Посмотреть мои возможности /help", reply_markup=keyboards(keys_board['start']))

@bot.callback_query_handler(func=lambda call: call.data == 'cb_info')
def cb_button1(message: types.Message):
    print("work with info")
    bot.delete_message(message.from_user.id, message.message.message_id)
    bot.send_message(message.from_user.id, information, reply_markup=keyboards(keys_board['info']))

@bot.callback_query_handler(func=lambda call: call.data == 'cb_play')
def cb_button1(message: types.Message):
    print("work with play")
    bot.delete_message(message.from_user.id, message.message.message_id)
    bot.send_message(message.from_user.id, "будущая функция игры", reply_markup=keyboards(keys_board['play']))

@bot.callback_query_handler(func=lambda call: call.data == 'cb_help')
def cb_button1(message: types.Message):
    print("work with help")
    bot.delete_message(message.from_user.id, message.message.message_id)
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("Start!", callback_data="cb_start"),
               types.InlineKeyboardButton("Info", callback_data="cb_info"),
               types.InlineKeyboardButton("Play!", callback_data="cb_play"),
               types.InlineKeyboardButton("Help again", callback_data="cb_help"))
    bot.send_message(message.from_user.id, HELP, reply_markup=markup)


def keyboards(spisok):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*spisok)
    return keyboard



@bot.message_handler(content_types=["text"])
def get_text_messages(message):

    client.add_id(message.chat.id)


    # класс с методами работы в базе данных

    #print(str(message.chat.id) + " " + message.from_user.username + ": " + message.text)
    print(message.text)
    if message.text in ["Привет", "привет", "сап", "s"]:
        bot.send_message(message.from_user.id, "Привет, введи /help для информации о моих возможностях", reply_markup=keyboards(['/help']))


    elif message.text == "/play":

        bot.send_message(message.from_user.id, "будущая функция игры", reply_markup=keyboards(keys_board['play']))
        # 2 режима игры - со счетами в ирл и без них

    elif message.text == "/info":

        bot.send_message(message.from_user.id, information, reply_markup=keyboards(keys_board['info']))
    elif message.text == "/tutor":
        bot.send_message(message.from_user.id, "сейчас идёт загрузка туториала пожалуйсто дождитесь окончания ...")
        with open('1.jpg', 'rb') as img:
            bot.send_photo(message.chat.id, img)
        bot.send_message(message.from_user.id, tutor, reply_markup=keyboards(keys_board['tutor']))
        with open('2.png', 'rb') as img:
            bot.send_photo(message.chat.id, img)
        with open('check.mp4', 'rb') as img:
            video = open('check.mp4', 'rb')
        bot.send_video(message.chat.id, video)
        bot.send_message(message.from_user.id, "загрузка закончена!")

    elif message.text == "/start":
        answer = client.registration()
        if answer == "Added":
            bot.send_message(message.from_user.id, "Отлично, вы зарегестрированы! Посмотреть мои возможности /help", reply_markup=keyboards(keys_board['start']))

            bot.send_message(message.from_user.id, input("Введи сообщение"))
        elif answer == "Been":
            bot.send_message(message.from_user.id, "Ошибка! Вы уже зарегестрированы. Посмотреть мои возможности /help", reply_markup=keyboards(keys_board['start']))





bot.polling(none_stop=True, interval=0)
