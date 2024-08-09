from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardRemove, WebAppInfo)

kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Open', web_app=WebAppInfo(url=f'https://vk.com'))]
])