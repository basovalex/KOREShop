from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardRemove, WebAppInfo)
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='💴 Расчет стоимости заказа'),
    KeyboardButton(text='📦 Оформить заказ')], [KeyboardButton(text='🔎 Часто задаваемые вопросы'), KeyboardButton(text='📝 Отзывы')], [KeyboardButton(text='❗️ Важные моменты перед заказом')]], resize_keyboard=True)

questions = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='🛍 Как сделать заказ?')], [KeyboardButton(text='🔍 Товар оригинальный?')],
                                          [KeyboardButton(text='🚚 Как отследить заказ?')], [KeyboardButton(text='🕐 Сроки доставки')],
                                          [KeyboardButton(text='🏠 Главное меню')]], resize_keyboard=True)

pon = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Понятно 👍')]], resize_keyboard=True)
ok = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Готово, далее ✅')]], resize_keyboard=True)
nextt = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='📦 Оформить заказ')], [KeyboardButton(text='🔎 Часто задаваемые вопросы')]], resize_keyboard=True)

tovar = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '👟 Кроссовки/Кеды', callback_data='sneaker')],
    [InlineKeyboardButton(text = '🥷 Худи/Толстовки/Спорт. штаны', callback_data='blouse')],
    [InlineKeyboardButton(text = '👕 Футболки/Шорты/Аксессуары', callback_data='t-short')],
    [InlineKeyboardButton(text = '🧥 Пуховики', callback_data='jacket')],
    [InlineKeyboardButton(text = '👜 Сумки/Рюкзаки (небольшие)', callback_data='bag')],
    [InlineKeyboardButton(text = '🎒 Сумки/Рюкзаки (большие)', callback_data='backpack')]])

home = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = '⚙️ Инструкция по получению ссылки'),
    KeyboardButton(text = '🏠 Главное меню')]
    ], resize_keyboard=True, input_field_placeholder='Отправьте ссылку на товар...')

back = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = '↩️ Назад'),
     KeyboardButton(text = '🏠 Главное меню')]
    ], resize_keyboard=True)

size = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='У товара нет размера 🎒')]
    ], resize_keyboard=True)
remove_kb = ReplyKeyboardRemove()