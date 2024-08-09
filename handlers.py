from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import F, Router

from keyboards import kb

router = Router()

@router.message(CommandStart())
async def get_start(message: Message):
    await message.answer('Привет!')

@router.message(Command('url'))
async def open_url(message: Message):
    await message.answer('Открыть', reply_markup=kb)

@router.message(Command('VK'))
async def open_google(message: Message):
    await message.answer('')

@router.message()
async def echo(message: Message):
    await message.answer(message.text)

