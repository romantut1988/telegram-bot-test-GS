from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mainMenu = InlineKeyboardMarkup(row_width=1)
btnUrl = InlineKeyboardButton(text="открыть веб-приложение", url="https://romantut1988.github.io/email-delivery")

mainMenu.insert(btnUrl)
