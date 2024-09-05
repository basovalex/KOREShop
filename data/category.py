from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from handlers import router
from keyboards import menu, tovar

price_sneaker = State()

@router.callback_query(F.data == 'sneaker')
async def get_price_sneaker(callback: CallbackQuery, state: FSMContext):
    await state.set_state(price_sneaker)
    await callback.answer('Введите стоимость кроссовок.')
    print(price_sneaker)