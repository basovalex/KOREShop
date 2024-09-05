import random

from aiogram.types import message

from data.price import kurs_ya


def get_random_number() -> int:
    return random.randint(1, 100)

def condition_comis(price) -> int:
    if price * kurs_ya < 3000:
        commis = 500
    elif price * kurs_ya >= 3000 and price * kurs_ya <= 7000:
        commis = 700
    elif price * kurs_ya >= 7000 and price * kurs_ya <= 12000:
        commis = 1000
    else:
        commis = 1300
    return commis