
from aiogram.dispatcher.filters.state import StatesGroup, State


class ProductQuantity(StatesGroup):
    quantity = State()
