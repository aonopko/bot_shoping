import types

from aiogram.types import Message, ContentType
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from filters.bot_filter import CheckAdmin
from db.db_commands import get_item
from states.admin_state import GetProduct


async def id_item(m: Message):
    await GetProduct.id_product.set()
    await m.answer("\U0000231B Додайте id товару")


async def get_id(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["id_product"] = int(m.text)
            id_product = data.get("id_product")
        except ValueError:
            await m.answer("\U0000203C Потрібно ввести число")
        else:
            try:
                a = await get_item(id_product)
            except AttributeError:
                await m.answer("\U0000203C Такого товару не існує")
            else:
                await m.answer_photo(m.from_user.id)
                await state.finish()


def register_get_all_items(dp: Dispatcher):
    dp.register_message_handler(id_item, CheckAdmin(),
                                Text(equals=["Переглянути товар"],
                                     ignore_case="/"))
    dp.register_message_handler(get_id, CheckAdmin(),
                                state=GetProduct.id_product, content_types=ContentType.PHOTO)
