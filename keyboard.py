from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

# добавляем разметку наших кнопок
start = types.ReplyKeyboardMarkup(row_width=3)
# создаем кнопки записаться
sign_up = types.KeyboardButton('Записаться на занятие')
# и расписание
schedule = types.KeyboardButton('Расписание тренеровок')
# и контакты
contacts = types.KeyboardButton('Контакты')
# и покажи пользователя
user = types.KeyboardButton('Покажи пользователя')
# и покажи отправить фото
picture = types.KeyboardButton('Отправить фото')
# добавляем кнопки в нашу разметку
start.add(sign_up, schedule, contacts, user, picture)

"""------------------------------------------Добавление inline-кнопок-----------------------------------------------"""
contacts_or_map = InlineKeyboardMarkup(row_width=2)
contacts_or_map.add(InlineKeyboardButton('Написать тренеру', callback_data='trener'))

url_list = 'https://yandex.by/maps/-/CCUV6ZcsTC'
contacts_or_map.add(InlineKeyboardButton('Где находится клуб', callback_data='list', url=url_list))

"""------------------------Добавление inline-кнопок для "Покажи полльзователя"---------------------------------------"""
user_id = InlineKeyboardMarkup(row_width=2)
button_id = InlineKeyboardButton('Хочу увидеть ID', callback_data="button_id")
back_again = InlineKeyboardButton('Вернуться обратно', callback_data="back_again")
user_id.add(button_id, back_again)
