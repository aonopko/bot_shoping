
from aiogram.dispatcher.filters.state import StatesGroup, State


class AddProduct(StatesGroup):
    id_product = State()
    name = State()
    category = State()
    sub_category = State()
    price = State()
    quantity = State()
    photo = State()


class DelProduct(StatesGroup):
    id_product = State()


class GetProduct(StatesGroup):
    id_product = State()


class UpdateProduct(StatesGroup):
    id_product = State()
    photo = State()
    price = State()
    quantity = State()
