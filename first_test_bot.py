import telebot
from telebot import types

temp = open('bb', 'r')
name = temp.read()
print(name)

tb = telebot.TeleBot(str(name))

dict = {}
chat_id = 243825705

#
@tb.message_handler(content_types ='text')
def simple_ansver(message):
    text = message.text
    print(message)
    if text != 'покажи':
        dict[message.message_id] = text
        tb.reply_to(message, text)
    elif text == 'заново':
        tb.reset_data()
        tb.delete_message()
    else:
        print(dict)
        tb.reply_to(message, str(dict))
# Using the ReplyKeyboardMarkup class
# It's constructor can take the following optional arguments:
# - resize_keyboard: True/False (default False)
# - one_time_keyboard: True/False (default False)
# - selective: True/False (default False)
# - row_width: integer (default 3)
# row_width is used in combination with the add() function.
# It defines how many buttons are fit on each row before continuing on the next row.
markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('хочу спать')
itembtn2 = types.KeyboardButton('хочу есть')
itembtn3 = types.KeyboardButton('ничего не хочу')
markup.add(itembtn1, itembtn2, itembtn3)
tb.send_message(chat_id, "Choose one letter:", reply_markup=markup)







tb.infinity_polling(interval=1, timeout=20)
