from botConfig import dp, bot
from aiogram import types
import random

total = 150 
ocher = 0

@dp.message_handler(commands=['start'])
async def startBot(message: types.Message):
    await bot.send_message(message.from_user.id, text = f'{message.from_user.first_name}'
    f', Привет бро! ты написал мне "{message.text}" напиши /game мне и да начнется мировая игра )хех')


@dp.message_handler(commands=['game'])
async def anysing(message: types.Message):
    global ocher
    ocher = random.randint(0,2) # ставим рандомную очередность 
    if ocher:
        await bot.send_message(message.from_user.id,  f'{message.from_user.first_name}'
    f',  бро ты первый ходишь! введи количество конфет')
    else:
        await bot.send_message(message.from_user.id,  f'{message.from_user.first_name}'
    f', первый ходит компьютер напиши мне любой символ для продолжения игры ')


@dp.message_handler()
async def games(message: types.Message):
    global ocher
    global total
    if total > 28:
        if ocher:
            if int(message.text) >= 28:
                await message.reply(f'{message.from_user.first_name} ты взял больше чем нужно бро ( Попробуй еще раз ')
                return message.reply(f'')
            total -= int(message.text)
            await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
            f' взял со стола{message.text} конфет.'
            f'на столе осталось {total} конфет'
            ' (введи любой символ)')
            ocher = False 
            if total < 28:
                await bot.send_message(message.from_user.id,  f'{message.from_user.first_name}'
                f', Твой проигрышь бро ((( Бот тебя дёрнул))) ')        
        else:
            k = random.randint(0, 28)
            total -= k
            await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
            f' бот взял со стола{k} конфет.'
            f'на столе осталось {total} конфет'
            '(Введите количество конфет)') 
            ocher = True  
            if total < 28:
                await bot.send_message(message.from_user.id,  f'{message.from_user.first_name}'
                f', Бро твоя победа Бот проиграл ') 

































