from aiogram.types import ReplyKeyboardMarkup, KeyboardButton           #, ReplyKeyboardRemove


b1 = KeyboardButton('start')
b2 = KeyboardButton('game')


cbClient = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

cbClient.add(b1).insert(b2)

# cbClient.row(b1,b2) Всё в строку пульнет 