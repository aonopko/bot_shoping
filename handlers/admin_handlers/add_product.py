from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from states.admin_state import AddProduct


async def add_id(m: Message):
    await AddProduct.id_product.set()
    await m.answer("Додайте id товару", m.from_user.id)


async def load_id(m: Message, state: FSMContext):
    async with state.proxy() as data:
        data['id_product'] = int(m.text)
        await m.answer(f"{data}")
        await state.finish()


def register_add_product_handlers(dp: Dispatcher):
    dp.register_message_handler(add_id, Text(equals=["Додати товар"], ignore_case="/"))
    dp.register_message_handler(load_id, state=AddProduct.id_product)
