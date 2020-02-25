import telebot
import random
from telebot import types

bot = telebot.TeleBot('1025191995:AAHqQJzP_WllwR_S6WiEkv3f4ic8yXoCFxw')




markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
markup = types.InlineKeyboardMarkup(row_width=2)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('ДЗ по природе 🗣')
    item2 = types.KeyboardButton('ЗНО 🧠')



    markup.add(item1,item2)

    bot.send_message(message.chat.id, 'Я Силан, нажми на кнопку'.format(message.from_user, bot.get_me()),parse_mode = 'html', reply_markup=markup)


@bot.message_handler(commands=['homework'])
def wtf(message):
    bot.send_message(message.chat.id, "Напиши ДЗ".format(message.from_user, bot.get_me()),parse_mode = 'html')
    bot.register_next_step_handler(message, get_homework)

def get_homework(message): #получаем фамилию
    global homework
    homework = message.text
    bot.send_message(message.chat.id, "Сохранено")


@bot.message_handler(content_types=['text'])
def keyboard(message):
        if message.text == 'ЗНО 🧠':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item3 = types.InlineKeyboardButton("Украинский язык", callback_data='1')
            item4 = types.InlineKeyboardButton("Математика", callback_data='2')
            item5 = types.InlineKeyboardButton("История Украины", callback_data='3')
            item6 = types.InlineKeyboardButton("Английский язык", callback_data='4')
            item7 = types.InlineKeyboardButton("География", callback_data='5')
            item8 = types.InlineKeyboardButton("Биология", callback_data='6')
            item9 = types.InlineKeyboardButton("Физика", callback_data='7')
            item10 = types.InlineKeyboardButton("Химия", callback_data='8')
            item11 = types.InlineKeyboardButton("Немецкий язык", callback_data='9')
            item12 = types.InlineKeyboardButton("Испанский язык", callback_data='10')


            markup.add(item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
            bot.send_message(message.chat.id, 'Какой возьмём предмет 🤔?', reply_markup=markup)

        elif message.text == 'ДЗ по природе 🗣':
            bot.send_message(message.chat.id, 'ДЗ: ' + str(homework))



        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            try:
                if call.message:
                    if call.data == '1':
                        bot.send_message(call.message.chat.id, '('+message.from_user.first_name+')'+' Украинский язык - ' + str(str(random.randint(100,200)) + ' баллов'))
                    elif call.data == '2':
                        bot.send_message(call.message.chat.id,  '('+message.from_user.first_name+')'+' Математика - ' + str(str(random.randint(100,200)) + ' баллов'))
                    elif call.data == '3':
                        bot.send_message(call.message.chat.id, '('+message.from_user.first_name+')'+' История Украины - ' + str(str(random.randint(100,200)) + ' баллов'))
                    elif call.data == '4':
                        bot.send_message(call.message.chat.id, '('+message.from_user.first_name+')'+' Английский язык - ' + str(str(random.randint(100,200)) + ' баллов'))
                    elif call.data == '5':
                        bot.send_message(call.message.chat.id, '('+message.from_user.first_name+')'+' География - ' + str(str(random.randint(100,200)) + ' баллов'))
                    elif call.data == '6':
                        bot.send_message(call.message.chat.id, '('+message.from_user.first_name+')'+' Биология - ' + str(str(random.randint(100,200)) + ' баллов'))
                    elif call.data == '7':
                        bot.send_message(call.message.chat.id, '('+message.from_user.first_name+')'+' Физика - ' + str(str(random.randint(100,200)) + ' баллов'))
                    elif call.data == '8':
                        bot.send_message(call.message.chat.id, '('+message.from_user.first_name+')'+' Химия - ' + str(str(random.randint(100,200)) + ' баллов'))
                    elif call.data == '9':
                        bot.send_message(call.message.chat.id, '('+message.from_user.first_name+')'+' Немецкий язык - ' + str(str(random.randint(100,200)) + ' баллов'))
                    elif call.data == '10':
                        bot.send_message(call.message.chat.id, '('+message.from_user.first_name+')'+' Испанский язык - ' + str(str(random.randint(100,200)) + ' баллов'))










            except Exception as e:
                print(repr(e))










bot.polling(none_stop = True)
