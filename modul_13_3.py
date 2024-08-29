from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

start = False

@dp.message_handler(text=["Urban"])
async def urban_message(message):
    print('Urban всех научит!')


@dp.message_handler(commands=['start'])
async def all_message(message):

    global start
    start = True
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    print(start)
    #print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_message(message):
    globals()
    print(start)
    if start:
        if message.text == 'Привет':
            await message.answer('Как Ваше настроение ?')
        else:
            await message.answer(message.text)

    else:
        await message.answer('Введите команду /start, чтобы начать общение напишите "Привет".')


    #print('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
