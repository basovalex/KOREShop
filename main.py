import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers import router

async def main():
    bot = Bot(token='7291158423:AAFM0LfXcoiiDI4GmcQaUbCGNM53osu0pJQ')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')