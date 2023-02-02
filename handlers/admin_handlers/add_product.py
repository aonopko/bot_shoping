from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from states.admin_state import AddProduct


async def add_id(m: Message):
    await AddProduct.id_product.set()
    await m.answer("Додайте id товару", m.from_user.id)

async def load_id(m: Message, state: FSMContext):
    async with state.proxy() as data:
        pass