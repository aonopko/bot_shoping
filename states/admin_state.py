
from aiogram.dispatcher.filters.state import StatesGroup, State


class AddProduct(StatesGroup):
    name = State()
    category = State()
    category_code = State()
    sub_category = State()
    sub_category_code = State()
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
    promotion = State()
    new_product = State()
