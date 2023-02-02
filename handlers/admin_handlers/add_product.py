from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from states.admin_state import AddProduct


async def add_id(m: Message, state: FSMContext):
    await AddProduct.id_product.set()
    await m.answer("Додайте id товару", m.from_user.id)
