import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav

TOKEN = '6036358670:AAHSpB4EhWnWOqJo6MUQl3ClSPLlRkG3Ic0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id,
                               "Привет это моё тестовое задание по направлению “Кибербезопасность и приложения на Python”",
                               reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
