
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


class AddProduct(StatesGroup):
    id_product = State()
    name = State()
    category = State()
    sub_category = State()
    price = State()
    quantity = State()
    photo = State()
    add_prod = State()
    del_prod = State()
