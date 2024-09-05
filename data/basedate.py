from aiogram.fsm.state import StatesGroup, State


user = {'in_game': False,
        'secret_number': None,
        'attempts': None,
        'total_games': 0,
        'wins': 0}


class Reg_sneak(StatesGroup):
        price = State()
class Reg_blouse(StatesGroup):
        price = State()
class Reg_shirt(StatesGroup):
        price = State()
class Reg_jacket(StatesGroup):
        price = State()
class Reg_bag(StatesGroup):
        price = State()
class Reg_backpack(StatesGroup):
        price = State()

