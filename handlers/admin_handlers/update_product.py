from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from asyncpg.exceptions import UniqueViolationError

from filters.bot_filter import CheckAdmin
from states.admin_state import UpdateProduct
from db.db_commands import update_photo_item
from keyboards.default.admin_keyboard import update_product


async def update_products(m: Message):
    await m.answer(text="Ваше меню для оновлення",
                   reply_markup=update_product)
    await UpdateProduct.id_product.set()
    await m.answer("\U0000231B Додайте id товару")


async def update_id(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["id_product"] = int(m.text)
        except ValueError:
            await m.answer("\U0000203C  Потрібно ввести число")
        else:
            await state.reset_state()
            await m.answer("\U0000231B id Додано")
            await m.answer(f"{data}")


async def update_photo(m: Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = m.photo[0].file_id
        await UpdateProduct.photo.set()
        await m.answer("\U0001F44D Товар додано")
        await state.reset_state()
        await m.answer(f"{data}")


def register_update_product_hendlers(dp: Dispatcher):
    dp.register_message_handler(update_products, CheckAdmin(),
                                text=["\U0001f504 Оновити товар"])
    dp.register_message_handler(update_id, state=UpdateProduct.id_product)
    dp.register_message_handler(update_photo, CheckAdmin(),
                                text=["Фото"], content_types=["photo"])
