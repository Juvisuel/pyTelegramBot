import random
import time
import classes
import telebot
from telebot import types
import json

temp = open('bb', 'r')
name = temp.read()
# print(name)

vision = 1

session_dict = {}  #будем потом переписывать дикты и подчитывать
session_dict[0] = 'temp'

# while session_dict:
#     for session_all in session_dict.items():
#         # print(1)
#         session = session_all[1]

tb = telebot.TeleBot(str(name))


    ## асинхронный
    # tb = telebot.AsyncTeleBot(str(name))
    # @tb.message_handler(commands=['start'])
    # async def start_message(message):
    # 	await tb.send_message(message.chat.id, 'Hello!')


# Using the ReplyKeyboardMarkup class
# It's constructor can take the following optional arguments:
# - resize_keyboard: True/False (default False)
# - one_time_keyboard: True/False (default False)
# - selective: True/False (default False)
# - row_width: integer (default 3)
# row_width is used in combination with the add() function.
# It defines how many buttons are fit on each row before continuing on the next row.

# todo решить проблему с сессиями в цикле

# for session_all in session_dict.items():
#     session = session_all[1]

@tb.message_handler(commands =['start'])
def start(message):
    time.sleep(2)
    if not message.from_user == 'is_bot':

        session_dict[f'{message.from_user.id}'] = classes.OneExit()
        session = session_dict[f'{message.from_user.id}']

        markup = types.ReplyKeyboardMarkup(row_width=2)
        session.user_id = message.from_user.id
        session.username = message.from_user.first_name
        session.chat_id = message.chat.id
        session.datetime = message.date

        # itembtn1 = types.KeyboardButton('Чувствую тревогу или страх')
        # itembtn2 = types.KeyboardButton('Злюсь и обижаюсь')
        # itembtn3 = types.KeyboardButton('Мне неспокойно')
        # itembtn4 = types.KeyboardButton('Как-то грустно')
        # itembtn5 = types.KeyboardButton('Ничего не хочется делать')
        # itembtn6 = types.KeyboardButton('Вроде нормально, но что-то не так')
        #
        # markup.add(itembtn1, itembtn2, itembtn3,itembtn4,itembtn5,itembtn6)
        markup = types.ReplyKeyboardRemove()

        tb.send_message(session.chat_id, "Доброго!",reply_markup=markup )
        return

    else:
        tb.send_message(message.chat.id, "Привет ботам")
        session = 0
        return

print(session_dict)

@tb.message_handler(content_types ='text')
def ansver(message):
    time.sleep(1)
    print(session_dict)
    session = session_dict[f'{message.from_user.id}']

    if session.level == 0:
        if not message.from_user == 'is_bot':
            # session = update_one_exit(session, message)
            session.level = 1
            session.user_id = message.from_user.id
            session.username = message.from_user.first_name
            session.chat_id = message.chat.id
            session.datetime = message.date

            session.begin_score = 0
            session.zone = 0
            session.end_score = 0
            session.emotion = ''
            session.helper = ''
            session.location = ''
            session.resource = ''
            session.wish = ''
            session.error = ''
            session.change_plus = ''
            session.change_minus = ''

            markup = types.ReplyKeyboardMarkup(row_width=2)
            itembtn1 = types.KeyboardButton('Чувствую тревогу или страх')
            itembtn2 = types.KeyboardButton('Злюсь и обижаюсь')
            itembtn3 = types.KeyboardButton('Мне неспокойно')
            itembtn4 = types.KeyboardButton('Как-то грустно')
            itembtn5 = types.KeyboardButton('Ничего не хочется делать')
            itembtn6 = types.KeyboardButton('Вроде нормально, но что-то не так')

            markup.add(itembtn1, itembtn2, itembtn3,itembtn4,itembtn5,itembtn6)

            tb.send_message(session.chat_id, "Как себя чувствуете?", reply_markup=markup)


        else: tb.send_message(message.chat.id, "Привет ботам")


    if session.level == 1:  # начальный уровень вопросов
        text = message.text
        print(message)
        if text == 'Чувствую тревогу или страх':

            markup = types.ReplyKeyboardMarkup(row_width=2)
            itembtn1 = types.KeyboardButton('Могу ли заработать денег')
            itembtn2 = types.KeyboardButton('Тают накопления')
            itembtn3 = types.KeyboardButton('Что-то с отношениями')
            itembtn4 = types.KeyboardButton('Сомневаюсь в своей успешности в бизнесе/на работе')
            itembtn5 = types.KeyboardButton('Кажется, здоровье не в порядке')
            itembtn6 = types.KeyboardButton('Пугает мое будущее')
            markup.add(itembtn1, itembtn2, itembtn3,itembtn4,itembtn5,itembtn6)
            tb.send_message(session.chat_id, f"Что вас тревожит, {session.username}?", reply_markup=markup)
            session.level = 2
            session.begin_score = 1
            return

        elif text == 'Злюсь и обижаюсь':
            time.sleep(2)
            markup = types.ReplyKeyboardMarkup(row_width=2)
            itembtn1 = types.KeyboardButton('Недостаточно платят')
            itembtn2 = types.KeyboardButton('Кто-то тратит мои деньги')
            itembtn3 = types.KeyboardButton('Не чувствую уважения и любви')
            itembtn4 = types.KeyboardButton('Меня не ценят на работе')
            itembtn5 = types.KeyboardButton('Люди не берегут меня')
            itembtn6 = types.KeyboardButton('Мне не дают пробиться, мешают')
            markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
            tb.send_message(session.chat_id, f"Что вас злит или обижает, {session.username}?", reply_markup=markup)
            session.begin_score = 2
            session.level = 2
            return

        elif text == 'Мне неспокойно':
            time.sleep(2)
            markup = types.ReplyKeyboardMarkup(row_width=2)
            itembtn1 = types.KeyboardButton('Низкий заработок')
            itembtn2 = types.KeyboardButton('Мне не хватает денег')
            itembtn3 = types.KeyboardButton('Что-то не так в отношениях')
            itembtn4 = types.KeyboardButton('Некомфортно чувствую себя на работе')
            itembtn5 = types.KeyboardButton('Чувствую опасность для своего здоровья')
            itembtn6 = types.KeyboardButton('Переживаю за будущее')
            markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
            tb.send_message(session.chat_id, f"Что вас беспокоит, {session.username}?", reply_markup=markup)
            session.begin_score = 3
            session.level = 2
            return

        elif text == 'Как-то грустно':
            time.sleep(2)
            markup = types.ReplyKeyboardMarkup(row_width=2)
            itembtn1 = types.KeyboardButton('Не получается зарабатывать')
            itembtn2 = types.KeyboardButton('Куда-то уходят деньги и ничего не остается')
            itembtn3 = types.KeyboardButton('Мне одиноко')
            itembtn4 = types.KeyboardButton('Работа не приносит радости')
            itembtn5 = types.KeyboardButton('Мало жизненных сил')
            itembtn6 = types.KeyboardButton('Будущее видится в грустных тонах')
            markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
            tb.send_message(session.chat_id, f"Что вас печалит, {session.username}?", reply_markup=markup)
            session.begin_score = 4
            session.level = 2
            return

        elif text == 'Ничего не хочется делать':
            time.sleep(2)
            markup = types.ReplyKeyboardMarkup(row_width=2)
            itembtn1 = types.KeyboardButton('Нет желания зарабатывать')
            itembtn2 = types.KeyboardButton('Не хочу считать и планировать деньги')
            itembtn3 = types.KeyboardButton('Нет сил строить отношения')
            itembtn4 = types.KeyboardButton('Не хочу идти на работу')
            itembtn5 = types.KeyboardButton('Ничего активного в жизни не хочу')
            itembtn6 = types.KeyboardButton('Не хочу смотреть в будущее')
            markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
            tb.send_message(session.chat_id, f"Что самое нежелательное из всего, {session.username}?", reply_markup=markup)
            session.begin_score = 5
            session.level = 2
            return

        elif text == 'Вроде нормально, но что-то не так':
            time.sleep(2)
            markup = types.ReplyKeyboardMarkup(row_width=2)
            itembtn1 = types.KeyboardButton('Когда думаю о заработке')
            itembtn2 = types.KeyboardButton('Когда думаю о том, как свести концы с концами')
            itembtn3 = types.KeyboardButton('При мыслях о семье, близком человеке')
            itembtn4 = types.KeyboardButton('Похоже, что-то не так на работе')
            itembtn5 = types.KeyboardButton('Кажется, я заболеваю')
            itembtn6 = types.KeyboardButton('Когда думаю о будущем')
            markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
            tb.send_message(session.chat_id, f"В какой зоне жизни это ощущение сильнее, {session.username}?", reply_markup=markup)
            session.begin_score = 6
            session.level = 2
            return
        else:
            tb.send_message(session.chat_id, 'Пожалуйста, выберите один из вариантов.')
            return


        # else:
        #     tb.send_message(session.chat_id,  f'{text}?')
        #     tb.send_message(session.chat_id, 'Ей вей.. тут нет кода, вы нашли проблему, пожалуйста, сообщите о ней')


    if session.level == 2:
        if vision:
            session.print_session()
        time.sleep(1)
        text = message.text
        if text == 'Могу ли заработать денег' or text == 'Недостаточно платят' or text == \
                'Низкий заработок' or text == 'Не получается зарабатывать' or text == 'Нет желания зарабатывать' \
                or text == 'Когда думаю о заработке' :
            if session:
                session.zone = 'Финансы, заработок'
                session.level = 3

        elif text == 'Тают накопления' or text == 'Кто-то тратит мои деньги' or text == \
                'Мне не хватает денег' or text == 'Куда-то уходят деньги и ничего не остается' or text == 'Не хочу считать и планировать деньги' \
                or text == 'Когда думаю о том, как свести концы с концами' :
            if session:
                session.zone = 'Экономика, планирование финансов'
                session.level = 3

        elif text == 'Что-то с отношениями' or text == 'Не чувствую уважения и любви' or text == \
                'Что-то не так в отношениях' or text == 'Мне одиноко' or text == 'Нет сил строить отношения' \
                or text == 'При мыслях о семье, близком человеке' :
            if session:
                session.zone = 'Отношения, близкие люди, партнеры, дети'
                session.level = 3

        elif text == 'Сомневаюсь в своей успешности в бизнесе/на работе' or text == 'Меня не ценят на работе' or text == \
                'Некомфортно чувствую себя на работе' or text == 'Работа не приносит радости' or text == 'Не хочу идти на работу' \
                or text == 'Похоже, что-то не так на работе' :
            if session:
                session.zone = 'Работа, карьера, успешность бизнеса'
                session.level = 3

        elif text == 'Кажется, здоровье не в порядке' or text == 'Люди не берегут меня' or text == \
                'Чувствую опасность для своего здоровья' or text == 'Мало жизненных сил' or text == 'Ничего активного в жизни не хочу' \
                or text == 'Кажется, я заболеваю' :
            if session:
                session.zone = 'Здоровье'
                session.level = 3

        elif text == 'Пугает мое будущее' or text == 'Мне не дают пробиться, мешают' or text == \
                'Переживаю за будущее' or text == 'Будущее видится в грустных тонах' or text == 'Не хочу смотреть в будущее' \
                or text == 'Когда думаю о будущем' :
            if session:
                session.zone = 'Будущее, планы на будущее'
                session.level = 3
        else:
            tb.send_message(session.chat_id, 'Пожалуйста, выберите один из вариантов.')




        markup = types.ReplyKeyboardRemove()
        tb.send_message(session.chat_id, 'что вы чувствуете, о чем думаете в связи с этим?', reply_markup=markup)

        session.print_session()
        return


        # elif text == 'Тают накопления':
        # elif text == 'Что-то с отношениями':
        # elif text == 'Сомневаюсь в своей успешности в бизнесе/на работе':
        # elif text == 'Кажется, здоровье не в порядке':
        # elif text == 'Тревожит мое будущее':


    if session.level == 3:
        if vision:
            session.print_session()
        time.sleep(2)
        text = message.text
        if len(text) > 4:
            session.emotion = session.emotion + text
            tb.send_message(session.chat_id,
                            'Какой человек вспоминается в связи с вашими эмоциями и чувствами? Может быть, '
                            'он проявлял что-то похожее или хорошо относился к вам, когда вы так себя '
                            'чувствовали и поступали, как сейчас чувствуете себя?')
            session.level = 4
            session.print_session()
            return
        else:
            session.emotion = session.emotion + text
            tb.send_message(session.chat_id, 'Расскажите о своих чувствах и мыслях немного подробней')

            return


    if session.level == 4:
        if vision:
            session.print_session()
        time.sleep(1)
        text = message.text

        if 'не' in text or 'не могу' in text or 'никто' in text:
            tb.send_message(session.chat_id, f'прочитайте еще раз описание и попробуйте снова: {session.emotion} ')
            return
        if ' я' in text or 'Я ' in text or ' я сам' in text or 'я сама' in text:
            tb.send_message(session.chat_id, f'Представьте ситуацию еще раз, и теперь '
                                             f'попробуйте найти кого-то другого: {session.emotion} ')
            return

        else:
            session.helper = text
            session.level = 5
        tb.send_message(session.chat_id, 'когда вы думаете об этом человеке, какая в первую очередь вспоминается ситуация?')
        return

    if session.level == 5:
        if vision:
            session.print_session()
        time.sleep(1)
        text = message.text
        session.location = session.location + text
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Знание правил, как правильно делать')
        itembtn2 = types.KeyboardButton('Способность принимать непростые решения')
        itembtn3 = types.KeyboardButton('Обеспечение безопасности, можно не бояться угроз')
        itembtn4 = types.KeyboardButton('Дать право отдыхать')
        itembtn5 = types.KeyboardButton('Подтверждение моей ценности')
        itembtn6 = types.KeyboardButton('Освобождение моего времени от обязательных, но не важных дел')
        itembtn7 = types.KeyboardButton('Амбиции')
        itembtn8 = types.KeyboardButton('Знание, что лучше для о моего здоровья')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8)
        tb.send_message(session.chat_id, f'Что в этой ситуации этот человек делал хорошо, мог так, как вы не могли, но хотели бы так сами? Можно выбрать из вариантов, лучше написать самостоятельно', reply_markup=markup)

        session.level = 6
        return


    if session.level == 6:
        if vision:
            session.print_session()
        time.sleep(1)
        text = message.text
        session.resource = text
        markup = markup = types.ReplyKeyboardRemove()
        tb.send_message(session.chat_id,f'Представьте себе, что в зоне *{session.zone}* вы получили волшебную способность '
                                        f' *{session.resource}*.Что вы можете теперь делать? Кем можете быть?', reply_markup=markup)
        session.level = 7
        return

    if session.level == 7:
        if vision:
            session.print_session()
        time.sleep(1)
        text = message.text
        session.wish = text
        session.level = 8
        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn1 = types.KeyboardButton('Вижу')
        itembtn2 = types.KeyboardButton('Не вижу')
        markup.add(itembtn1, itembtn2)
        tb.send_message(session.chat_id, f'если без *{session.resource}* невозможно *{session.wish}*,'
                                         'видите ли вы какую-то ошибку в том, как сформулировано ваше желание/цель?', reply_markup=markup)

        return

    if session.level == 8:
        if vision:
            session.print_session()
        time.sleep(1)
        text = message.text
        if text == 'Вижу':

            tb.send_message(session.chat_id, 'Расскажите о том, в чем видите ошибку')
            session.level = 9
            return
        if text == 'Не вижу':
            list_errors = ['Ошибка в решении чаще всего связана с тем, что вы перепутали зоны контроля: пытаетесь '
                           'контролировать то, что не можете или наоборот',
                           f'например: ПОКА НЕ *{session.resource}* , ТЫ НЕ ИМЕЕШЬ ПРАВА *{session.wish}*',
                           f'например: ЗАПРЕЩЕНО *{session.wish}*',
                           f'например: ОПАСНО *{session.wish}* ДЛЯ ТОГО КТО НЕ  *{session.resource}*',
                           f'Посмотрите на свое желание  *{session.wish.upper()}* , возможно, оно так сформулировано, что его исполнение '
                           'зависит от фактора, который вы не контролируете',
                           f'например: ЕСЛИ НЕ *{session.resource}* , НЕВОЗМОЖНО *{session.wish}*'
                           ]
            choice = random.randint(0, len(list_errors)-1)

            tb.send_message(session.chat_id, list_errors[choice])
        else:
            tb.send_message(session.chat_id, 'Пожалуйста, выберите один из вариантов')


            return

    if session.level == 9:
        if vision:
            session.print_session()

        text = message.text
        session.error = text

        session.level = 10


    if session.level == 10:
        if vision:
            session.print_session()
        text = message.text

        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn1 = types.KeyboardButton('Давайте продолжим')
        itembtn2 = types.KeyboardButton('Мне достаточно')
        markup.add(itembtn1, itembtn2)
        tb.send_message(session.chat_id, 'Сейчас можно остановиться, а можно поработать с зонами контроля '
                                         'и принять верное решение взамен неверного.', reply_markup=markup)

        session.level = 101

        if vision:
            session.print_session()


    if session.level == 101:
        if vision:
            session.print_session()
        time.sleep(1)

        text = message.text

        if text == 'Давайте продолжим':
            session.level = 11
            tb.send_message(session.chat_id, f'отлично, {session.username}, начнем')

        if text == 'Мне достаточно':
            markup = types.ReplyKeyboardMarkup(row_width=3)
            itembtn1 = types.KeyboardButton('Чувствую тревогу или страх')
            itembtn2 = types.KeyboardButton('Злюсь и обижаюсь')
            itembtn3 = types.KeyboardButton('Мне неспокойно')
            itembtn4 = types.KeyboardButton('Как-то грустно')
            itembtn5 = types.KeyboardButton('Ничего не хочется делать')
            itembtn6 = types.KeyboardButton('Вроде нормально, но что-то не так')
            itembtn7 = types.KeyboardButton('Я чувствую себя спокойно, стабильно')
            itembtn8 = types.KeyboardButton('Включилось чувство юмора или прилив сил')

            markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8)

            tb.send_message(session.chat_id, "как сейчас себя чувствуете?", reply_markup=markup)
            session.level = 14
            if vision:
                session.print_session()
            return

    if session.level == 11:
        if vision:
            session.print_session()
        text = message.text
        if text == 'Дополнить зону "не могу"':
            tb.send_message(session.chat_id, 'дополняем зону НЕ МОГУ')


        markup = types.ReplyKeyboardRemove()
        if session.error:
            tb.send_message(session.chat_id, f'Что в ситуации *{session.error}* в *{session.zone}* в зоне "Я НЕ МОГУ"? '
                                             f'Например, чувства и мысли других людей вы не контролируете, '
                                             f'не влияете на политику, погоду, удачу и т д', reply_markup=markup)

            if session.change_plus:
                session.level = 111
            else:
                session.level = 12
            return
        else:
            tb.send_message(session.chat_id, f'Что в ситуации *{session.wish}* *{session.zone}* в зоне "Я НЕ МОГУ"?  '
                                             f'Например, чувства и мысли других людей вы не контролируете, '
                                             f'не влияете на политику, погоду, удачу и т д', reply_markup=markup)
            if session.change_plus:
                session.level = 111
            else:
                session.level = 12
            return

    if session.level == 111:
        if vision:
            session.print_session()
        text = message.text
        session.change_minus  = session.change_minus + ' ' + text

        if text == 'Готово':
            markup = types.ReplyKeyboardMarkup(row_width=3)
            itembtn1 = types.KeyboardButton('Чувствую тревогу или страх')
            itembtn2 = types.KeyboardButton('Злюсь и обижаюсь')
            itembtn3 = types.KeyboardButton('Мне неспокойно')
            itembtn4 = types.KeyboardButton('Как-то грустно')
            itembtn5 = types.KeyboardButton('Ничего не хочется делать')
            itembtn6 = types.KeyboardButton('Вроде нормально, но что-то не так')
            itembtn7 = types.KeyboardButton('Спокойно, стабильно')
            itembtn8 = types.KeyboardButton('Включилось чувство юмора или прилив сил')

            markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8)

            tb.send_message(session.chat_id, "как сейчас себя чувствуете?", reply_markup=markup)

            session.level = 14
            return

        else:
            session.change_minus = session.change_minus + text
            markup = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton('Дополнить зону "не могу"')
            itembtn2 = types.KeyboardButton('Дополнить зону "могу"')
            itembtn3 = types.KeyboardButton('Готово')
            markup.add(itembtn3)
            markup.add(itembtn3)
            tb.send_message(session.chat_id,'готово?', reply_markup=markup)

            session.level = 102

            return


    if session.level == 12:
        if vision:
            session.print_session()
        time.sleep(1)
        text = message.text
        if text != 'Дополнить зону "могу"':
            session.change_minus = session.change_minus + ' ' + text

        if session.error:

            tb.send_message(session.chat_id,
                            f'Что в ситуации *{session.error}* *{session.zone}* в зоне "Я МОГУ?"')
            tb.send_message(session.chat_id, 'Вы контролируете все, что можете сделать своими руками, купить или '
                                             'все, на что у вас есть договоренности с другими и полномочия')
            session.level = 121
            return
        else:

            tb.send_message(session.chat_id,
                            f'Что в ситуации *{session.wish}* *{session.zone}* "Я МОГУ?"')
            tb.send_message(session.chat_id, 'Вы контролируете все, что можете сделать своими руками, купить или '
                                             'все, на что у вас есть договоренности с другими и полномочия')
            session.level = 121
            return

    if session.level == 121:
        if vision:
            session.print_session()
        text = message.text

        if text == 'Готово':
            markup = types.ReplyKeyboardMarkup(row_width=3)
            itembtn1 = types.KeyboardButton('Чувствую тревогу или страх')
            itembtn2 = types.KeyboardButton('Злюсь и обижаюсь')
            itembtn3 = types.KeyboardButton('Мне неспокойно')
            itembtn4 = types.KeyboardButton('Как-то грустно')
            itembtn5 = types.KeyboardButton('Ничего не хочется делать')
            itembtn6 = types.KeyboardButton('Вроде нормально, но что-то не так')
            itembtn7 = types.KeyboardButton('Спокойно, стабильно')
            itembtn8 = types.KeyboardButton('Включилось чувство юмора или прилив сил')

            markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8)

            tb.send_message(session.chat_id, "как сейчас себя чувствуете?", reply_markup=markup)

            session.level = 14
            return

        else:
            session.change_plus = session.change_plus + text
            markup = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton('Дополнить зону "не могу"')
            itembtn2 = types.KeyboardButton('Дополнить зону "могу"')
            itembtn3 = types.KeyboardButton('Готово')
            markup.add(itembtn3)
            tb.send_message(session.chat_id, 'готово?', reply_markup=markup)

            session.level = 102
            return


    if session.level == 102:
        if vision:
            session.print_session()
        time.sleep(1)
        text = message.text
        if text == 'Дополнить зону "могу"':
            session.level = 12
            if vision:
                session.print_session()
            return

        if text == 'Дополнить зону "не могу"':
            session.level = 11
            if vision:
                session.print_session()
            return

        if text == 'Готово':

            markup = types.ReplyKeyboardMarkup(row_width=3)
            itembtn1 = types.KeyboardButton('Чувствую тревогу или страх')
            itembtn2 = types.KeyboardButton('Злюсь и обижаюсь')
            itembtn3 = types.KeyboardButton('Мне неспокойно')
            itembtn4 = types.KeyboardButton('Как-то грустно')
            itembtn5 = types.KeyboardButton('Ничего не хочется делать')
            itembtn6 = types.KeyboardButton('Вроде нормально, но что-то не так')
            itembtn7 = types.KeyboardButton('Спокойно, стабильно')
            itembtn8 = types.KeyboardButton('Включилось чувство юмора или прилив сил')

            markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8)

            tb.send_message(session.chat_id, "как сейчас себя чувствуете?", reply_markup=markup)

            session.level = 14
            if vision:
                session.print_session()
            return

    if session.level == 14:
        if vision:
            session.print_session()

        text = message.text
        if text == 'Чувствую тревогу или страх':
            session.end_score = 1
        elif text == 'Злюсь и обижаюсь':
            session.end_score = 2
        elif text == 'Мне неспокойно':
            session.end_score = 3
        elif text == 'Как-то грустно':
            session.end_score = 4
        elif text == 'Ничего не хочется делать':
            session.end_score = 5
        elif text == 'Вроде нормально, но что-то не так':
            session.end_score = 6
        elif text == 'Спокойно, стабильно':
            session.end_score = 7
        elif text == 'Включилось чувство юмора или прилив сил':
            session.end_score = 8
        scores = (session.end_score-session.begin_score)/((8-session.begin_score)/100)

        tb.send_message(session.chat_id, f'В начале сессии вы думали и чувствовали: {session.emotion.upper()}, но на самом деле хотели получить'
                                         f'{session.resource.upper()} чтобы {session.wish.upper()} в {session.zone.upper()}')
        if session.error:
            tb.send_message(session.chat_id, f'вы ошибочно считали, что {session.error.upper()}')

        tb.send_message(session.chat_id,
                        f'попадая в похожую ситуацию, вы будете терять время, деньги и другие ресурсы в пользу тех, кто'
                        f'похож для вас на {session.helper.upper()}')

        if session.change_plus:
            tb.send_message(session.chat_id, f'вы решили, что можете {session.change_plus.upper()}')
        if session.change_plus:
            tb.send_message(session.chat_id, f'вы приняли невозможность {session.change_minus.upper()}')
        tb.send_message(session.chat_id, f'Ваше состояние улучшилось примерно в {session.end_score/session.begin_score} раза'
                                         f'  или на {round(scores)}% от максимума')

        markup = types.ReplyKeyboardRemove()
        tb.send_message(session.chat_id, 'Удачи!', reply_markup=markup)

        session.level = 15

    if session.level == 15:
        file_for_w = session_dict[f'{message.from_user.id}'].to_json()
        with open(f'f:\learn_neuro\pyTelegramBotAPI - Copy\sessions/{message.from_user.id}.txt', 'w') as temp_file:
            json.dump(file_for_w , temp_file)
        session_dict.pop(f'{message.from_user.id}')


tb.polling()

# tb.infinity_polling(interval=1, timeout=20)
