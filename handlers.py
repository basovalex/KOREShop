import types

from aiogram.enums import InputMediaType, ParseMode
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, FSInputFile, InputMedia
from aiogram.filters import CommandStart
from aiogram import F, Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from data.basedate import Reg_sneak, Reg_blouse, Reg_shirt, Reg_jacket, Reg_backpack, Reg_bag
from data.commands import condition_comis
from data.config import id_photo1, id_photo2, id_photo3, id_photo4, id_photo5, id_photo6, chat_id_admin1
from data.price import kurs_ya, sneak_delivery, blouse_delivery, shirt_delivery, jacket_delivery, backpack_delivery, \
    bag_delivery
from keyboards import menu, tovar, home, size, remove_kb, questions, pon, ok, nextt

router = Router()

class Tovar(StatesGroup):
    url = State()
    size = State()

@router.message(CommandStart())
async def get_start(message: Message):
    await message.answer(f"Здраствуй, *{message.from_user.first_name}*!\n"
                         "С помощью этого бота Вы можете заказать любую вещь с маркетплейса *Poizon*, за 14-17 дней с момента оформления заказа. ✈️\n\n"
                         "Этот бот может рассчитать стоимость вашего заказа с учетом доставки 💵\n"
                         "После этого, можете написать заявку для оформления заказа 📦\n\n"
                         "Тут вы можете найти ответы на все интересующие Вас вопросы 🧐\n"
                         "*Связаться - @shop_poizon1*", reply_markup=menu, parse_mode='Markdown')

@router.message(F.text == '💴 Расчет стоимости заказа')
async def category(message: Message):
    await message.answer('Выбери категорию товара, чтобы рассчитать цену доставки 💸',  reply_markup=tovar)

@router.message(F.text == '📦 Оформить заказ')
async def get_zakaz(message: Message, state: FSMContext):
    await message.answer('Для оформления товара от вас мне потребуется:\n\n'
                                     '1. Ссылка на товар 🔗 (Для получения ссылки следуйте инструкции)\n'
                                     '2. Размер 👟👕(Если присутствует)\n\n\nОтправьте нам вашу ссылку на товар: 🔗',
                                    reply_markup=home)
    await state.set_state(Tovar.url)
    await state.update_data(id=message.message_id)

@router.message(F.text == '🔎 Часто задаваемые вопросы')
async def qeust(message: Message):
    await message.answer('Выберите ваш вопрос: 🧐', reply_markup=questions)

@router.message(F.text == '🛍 Как сделать заказ?')
async def zakaz(message: Message):
    await message.answer_photo('https://telegra.ph/file/b7716b6c78606511e4829.jpg', '🏄 Сейчас мы поможем Вам разобраться!\n\n'
                         'Сначала скачайте приложение\n'
                         'Ссылки для скачивания:\n\n'
                         '➖ [IOS](https://apps.apple.com/ru/app/%E5%BE%97%E7%89%A9-%E5%BE%97%E5%88%B0%E8%BF%90%E5%8A%A8x%E6%BD%AE%E6%B5%81x%E5%A5%BD%E7%89%A9/id1012871328)\n'
                         '➖ [Android](https://www.anxinapk.com/rj/12201303.html)\n\n'
                         'Если всё понятно, нажмите 👇', reply_markup=pon, parse_mode='Markdown')


@router.message(F.text == 'Понятно 👍')
async def okey(message: Message):
    await message.answer_photo(photo=id_photo4, caption='*1. Внизу приложения выберите «значок сумки» \n\n'
                                                '2. В поисковую строку впишите на английском языке название товара\n\n'
                                                '3. Выберете подходящий товар\n\n Как это сделать? Смотрите фото!*', reply_markup=ok, parse_mode='Markdown')

@router.message(F.text == 'Готово, далее ✅')
async def ready(message: Message):
    await message.answer_media_group(media=[InputMediaPhoto(type=InputMediaType.PHOTO, media=id_photo5), InputMediaPhoto(type=InputMediaType.PHOTO, media=id_photo6)])
    await message.answer(text='*Посмотрите, есть ли Ваш размер в наличии🔎\n\n'
                                                'Регистрация 📝*\n\n'
                                                '1. Регистрация очень простая, если у Вас нет аккаунта на Poizon, то при нажатии на синюю кнопку попросят ввести номер телефона.\n'
                                                '2. Выбираете из списка +7, вводите свой номер телефона и ожидайте, когда Вам прийдет СМС. После регистрации Вы можете смотреть размер товара.\n\n'
                                                '*Если все понятно можете перейти к оформлению заказа ⬇️*', reply_markup=nextt, parse_mode='Markdown')


@router.message(F.text == '🔍 Товар оригинальный?')
async def original(message: Message):
    await message.answer_video(video='https://cs14.pikabu.ru/video/2023/01/16/167388679822433384_512x288.mp4', caption='*Мы доставляем только оригинальные товары!\n\n'
                              '🥇Перед отправкой они проходят проверку качества.\n\n'
                              'В проверку входит:\n\n'
                              '1) Визуальный осмотр и регистрация вещи в системе\n'
                              '2) Фотофиксация каждой детали\n'
                              '3) Идентификация\n'
                              '4) Перепроверка и выдача сертификата подлинности\n*', parse_mode='Markdown')

@router.message(F.text == '🕐 Сроки доставки')
async def time_delivery(message: Message):
    await message.answer(text="*Доставка занимает в среднем от 14 до 17 дней 🕘\n\n"
                              "Доставка проходит через надежного китайского посредника, который отправляет товар из Китая в Москву 👨‍💼\n"
                              "Далее доставкой через CDEK мы отправляем Вам в ближайший пункт выдачи заказов.\n\n"
                              "В день, когда приходит товар Вам остается только забрать его 🤝*", parse_mode='Markdown')

@router.message(F.text == '📝 Отзывы')
async def reviews(message: Message):
    await message.answer('Оставить или посмотреть отзывы Вы можете тут 🤗\n\n'
                         '⬇️⬇️⬇️⬇️'
                         '\n\n'
                         'https://t.me/Reviews_KOREShop')

@router.message(F.text == '❗️ Важные моменты перед заказом')
async def moment(message: Message):
    await message.answer(text="*Важно! Оформляя заказ, учитывайте следующие моменты*: ❗️\n\n\n"
                              "— У нас нет возвратов. Poizon дает на возврат 1 неделю, а доставка до Москвы занимает больше времени, к тому же возврат стоит значительных денег. \n\n"
                              "— У нас нет примерки. Мы не являемся продавцом, и если Вам вдруг не подойдет размер, вернуть его не получится (как сказали выше). Но мы с радостью поможем Вам перепродать товар.\n\n"
                              "— Если Вы оформили заказ, значит Вы доверяете Poizon и Вам подходит тот легит-чек, который предлагает площадка.\n\n"
                              "Если у Вас есть особые пожелания к заказу (комплектация, дополнительная проверка на оригинальность и тд), напишите нам и мы постараемся их учесть.", parse_mode='Markdown')

@router.message(F.text == '🚚 Как отследить заказ?')
async def check_tovar(message: Message):
    await message.answer(text="*Мы обязательно вам сообщим об измении статуса Вашего заказа в личные сообщения! 🚚\n\n"
                              "Так же Вы получите фотоотчет, когда товар попадет на склад в Китае и пройдет проверку на оригинальность* ✅", parse_mode='Markdown')

@router.message(Tovar.url)
async def waiting_url(message: Message, state: FSMContext):
    if message.text == '⚙️ Инструкция по получению ссылки':
        photos = [InputMediaPhoto(type=InputMediaType.PHOTO, media=id_photo1),
                  InputMediaPhoto(type=InputMediaType.PHOTO, media=id_photo2)]
        await message.answer_media_group(media=photos)
        await message.answer(text='Инструкция предствлена на фото 🖼')
    elif message.text == '🏠 Главное меню':
        await message.answer(f"Здраствуй, {message.from_user.first_name}!"
                             "\n Этот бот может рассчитать стоимость вашего заказа с учетом доставки 💵\n"
                             "После этого, можете написать заявку для оформления заказа 📦\n\n"
                             "Тут вы можете найти ответы на все интересующие Вас вопросы 🧐\n"
                             "Связаться - @shop_poizon1",
                             reply_markup=menu)
    else:
        try:
            await state.update_data(order_u=message.text.lower())
            await state.set_state(Tovar.size)
            await message.answer('Напишите размер обуви, одежды: 👟👕', reply_markup=size)
        except AttributeError:
            await message.answer('Отправьте нам вашу ссылку на товар: 🔗')

@router.message(Tovar.size)
async def waiting_size(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(order_s=message.text.lower())
    user_data = await state.get_data()
    message_text_for_admin = (f"✅ Новый заказ ✅\n"
                    f"Ссылка на товар - {user_data['order_u']}\n\n"
                    f"Размер товара - {user_data['order_s']}\n\n"
                    f"Покупатель - {message.from_user.first_name}, @{message.from_user.username}")
    await state.clear()
    await bot.send_message(chat_id_admin1, message_text_for_admin)
    await message.answer(f"Ваш заказ принят ✅\n\n"
                         f"🔗 URL на товар - {user_data['order_u']} \n\n"
                         f"📏 Размер товара - {user_data['order_s']} \n\n\n"
                         f"🕐 Вам напишут в ближайшее время!\n\n"
                         f"По всем вопросам обращайтесь сюда - @shop_poizon1", reply_markup=remove_kb)
    await bot.delete_message(chat_id=message.chat.id, message_id=user_data['id'])
    await message.answer(f"{message.from_user.first_name}, если еще захотите сделать заказ, мы всегда будем рады Вам помочь!"
                         "\n\n"
                         "Связаться - @shop_poizon1", reply_markup=menu)

@router.message(F.text == '🏠 Главное меню')
async def back_home(message: Message):
    await message.answer(f"Здраствуй, *{message.from_user.first_name}!*"
                         "\n С помощью этого бота ты можешь заказать любую вещь с Poizon, за 14-17 дней с момента оформления заказа. ✈️\n\n"
                         "Этот бот может рассчитать стоимость вашего заказа с учетом доставки 💵\n"
                         "После этого, можете написать заявку для оформления заказа 📦\n\n"
                         "Тут вы можете найти ответы на все интересующие Вас вопросы 🧐\n"
                         "*Связаться - @shop_poizon1*",
                                     reply_markup=menu, parse_mode='Markdown')

@router.callback_query(F.data == 'sneaker')
async def get_price_sneaker(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Reg_sneak.price)
    await callback.message.answer_photo(photo=id_photo3, caption='Введите цену товара в юанях 💴\n\n❗️Укажите целое число, без дробей, пробелов, букв и знаков валюты. Пример: 1250', reply_markup=remove_kb)
    await callback.answer()

@router.message(Reg_sneak.price)
async def final_price_sneaker(message: Message, state: FSMContext):
    try:
        commis = condition_comis(int(message.text))
        price = int(message.text)*kurs_ya + sneak_delivery + commis
        text = (f"Стоимость заказа будет: 🧮\n\n"
                f"<b>{int(message.text)} ¥ - {int(price)} ₽</b>\n\n"
                f" Стоимость рассчитана с учетом:\n\n"
                f"💵 Цена товара на пойзоне*Курс ¥\n"
                f"🇨🇳 Доставка по Китаю\n"
                f"✈️ Доставка из Китая в Россию\n"
                f"🛍 Комиссия сервиса\n\n"
                f"Обращаем Ваше внимание: расчет актуален в течение часа, т.к. на Poizon цены часто меняются\n\n"
                f"<b>Связаться - @shop_poizon1</b>")
        await message.answer(text, parse_mode=ParseMode.HTML, reply_markup=menu)
        await state.clear()
    except ValueError:
        await message.answer('Напишите целое число (стоимость товара в 🇨🇳). Попробуйте еще раз 🔄')

@router.callback_query(F.data == 'blouse')
async def get_price_blouse(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Reg_blouse.price)
    await callback.message.answer_photo(photo=id_photo3, caption='Введите цену товара в юанях 💴\n\n❗️Укажите целое число, без дробей, пробелов, букв и знаков валюты. Пример: 1250', reply_markup=remove_kb)
    await callback.answer()

@router.message(Reg_blouse.price)
async def final_price_blouse(message: Message, state: FSMContext):
    try:
        commis = condition_comis(int(message.text))
        price = int(message.text)*kurs_ya + blouse_delivery + commis
        text = (f"Стоимость заказа будет: 🧮\n\n"
                f"<b>{int(message.text)} ¥ - {int(price)} ₽</b>\n\n"
                f" Стоимость рассчитана с учетом:\n\n"
                f"💵 Цена товара на пойзоне*Курс ¥\n"
                f"🇨🇳 Доставка по Китаю\n"
                f"✈️ Доставка из Китая в Россию\n"
                f"🛍 Комиссия сервиса\n\n"
                f"Обращаем Ваше внимание: расчет актуален в течение часа, т.к. на Poizon цены часто меняются\n\n"
                f"<b>Связаться - @shop_poizon1</b>")
        await message.answer(text, parse_mode=ParseMode.HTML, reply_markup=menu)
        await state.clear()
    except ValueError:
        await message.answer('Напишите целое число (стоимость товара в 🇨🇳). Попробуйте еще раз 🔄')

@router.callback_query(F.data == 't-short')
async def get_price_shirt(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Reg_shirt.price)
    await callback.message.answer_photo(photo=id_photo3, caption='Введите цену товара в юанях 💴\n\n❗️Укажите целое число, без дробей, пробелов, букв и знаков валюты. Пример: 1250', reply_markup=remove_kb)
    await callback.answer()

@router.message(Reg_shirt.price)
async def final_price_shirt(message: Message, state: FSMContext):
    try:
        commis = condition_comis(int(message.text))
        price = int(message.text)*kurs_ya + shirt_delivery + commis
        text = (f"Стоимость заказа будет: 🧮\n\n"
                f"<b>{int(message.text)} ¥ - {int(price)} ₽</b>\n\n"
                f" Стоимость рассчитана с учетом:\n\n"
                f"💵 Цена товара на пойзоне*Курс ¥\n"
                f"🇨🇳 Доставка по Китаю\n"
                f"✈️ Доставка из Китая в Россию\n"
                f"🛍 Комиссия сервиса\n\n"
                f"Обращаем Ваше внимание: расчет актуален в течение часа, т.к. на Poizon цены часто меняются\n\n"
                f"<b>Связаться - @shop_poizon1</b>")
        await message.answer(text, parse_mode=ParseMode.HTML, reply_markup=menu)
        await state.clear()
    except ValueError:
        await message.answer('Напишите целое число (стоимость товара в 🇨🇳). Попробуйте еще раз 🔄')

@router.callback_query(F.data == 'jacket')
async def get_price_jacket(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Reg_jacket.price)
    await callback.message.answer_photo(photo=id_photo3, caption='Введите цену товара в юанях 💴\n\n❗️Укажите целое число, без дробей, пробелов, букв и знаков валюты. Пример: 1250', reply_markup=remove_kb)
    await callback.answer()

@router.message(Reg_jacket.price)
async def final_price_jacket(message: Message, state: FSMContext):
    try:
        commis = condition_comis(int(message.text))
        price = int(message.text)*kurs_ya + jacket_delivery + commis
        text = (f"Стоимость заказа будет: 🧮\n\n"
                f"<b>{int(message.text)} ¥ - {int(price)} ₽</b>\n\n"
                f" Стоимость рассчитана с учетом:\n\n"
                f"💵 Цена товара на пойзоне*Курс ¥\n"
                f"🇨🇳 Доставка по Китаю\n"
                f"✈️ Доставка из Китая в Россию\n"
                f"🛍 Комиссия сервиса\n\n"
                f"Обращаем Ваше внимание: расчет актуален в течение часа, т.к. на Poizon цены часто меняются\n\n"
                f"<b>Связаться - @shop_poizon1</b>")
        await message.answer(text, parse_mode=ParseMode.HTML, reply_markup=menu)
        await state.clear()
    except ValueError:
        await message.answer('Напишите целое число (стоимость товара в 🇨🇳). Попробуйте еще раз 🔄')

@router.callback_query(F.data == 'bag')
async def get_price_bag(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Reg_bag.price)
    await callback.message.answer_photo(photo=id_photo3, caption='Введите цену товара в юанях 💴\n\n❗️Укажите целое число, без дробей, пробелов, букв и знаков валюты. Пример: 1250', reply_markup=remove_kb)
    await callback.answer()

@router.message(Reg_bag.price)
async def final_price_bag(message: Message, state: FSMContext):
    try:
        commis = condition_comis(int(message.text))
        price = int(message.text)*kurs_ya + bag_delivery + commis
        text = (f"Стоимость заказа будет: 🧮\n\n"
                f"<b>{int(message.text)} ¥ - {int(price)} ₽</b>\n\n"
                f" Стоимость рассчитана с учетом:\n\n"
                f"💵 Цена товара на пойзоне*Курс ¥\n"
                f"🇨🇳 Доставка по Китаю\n"
                f"✈️ Доставка из Китая в Россию\n"
                f"🛍 Комиссия сервиса\n\n"
                f"Обращаем Ваше внимание: расчет актуален в течение часа, т.к. на Poizon цены часто меняются\n\n"
                f"<b>Связаться - @shop_poizon1</b>")
        await message.answer(text, parse_mode=ParseMode.HTML, reply_markup=menu)
        await state.clear()
    except ValueError:
        await message.answer('Напишите целое число (стоимость товара в 🇨🇳). Попробуйте еще раз 🔄')

@router.callback_query(F.data == 'backpack')
async def get_price_backpack(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Reg_backpack.price)
    await callback.message.answer_photo(photo=id_photo3, caption='Введите цену товара в юанях 💴\n\n❗️Укажите целое число, без дробей, пробелов, букв и знаков валюты. Пример: 1250', reply_markup=remove_kb)
    await callback.answer()

@router.message(Reg_backpack.price)
async def final_price_backpack(message: Message, state: FSMContext):
    try:
        commis = condition_comis(int(message.text))
        price = int(message.text)*kurs_ya + backpack_delivery + commis
        text = (f"Стоимость заказа будет: 🧮\n\n"
                f"<b>{int(message.text)} ¥ - {int(price)} ₽</b>\n\n"
                f" Стоимость рассчитана с учетом:\n\n"
                f"💵 Цена товара на пойзоне*Курс ¥\n"
                f"🇨🇳 Доставка по Китаю\n"
                f"✈️ Доставка из Китая в Россию\n"
                f"🛍 Комиссия сервиса\n\n"
                f"Обращаем Ваше внимание: расчет актуален в течение часа, т.к. на Poizon цены часто меняются\n\n"
                f"<b>Связаться - @shop_poizon1</b>")
        await message.answer(text, parse_mode=ParseMode.HTML, reply_markup=menu)
        await state.clear()
    except ValueError:
        await message.answer('Напишите целое число (стоимость товара в 🇨🇳). Попробуйте еще раз 🔄')

@router.message(F.text)
async def get_text(message: Message):
    await message.reply('Я вас не понимаю 🤔')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.reply('Классная картинка! 😉')
    print(message.photo[-1])





