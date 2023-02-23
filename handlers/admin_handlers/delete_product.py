from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from filters.bot_filter import CheckAdmin
from states.admin_state import DelProduct
from db.db_commands import del_item


async def delete_item(m: Message):
    await DelProduct.id_product.set()
    await m.answer("\U0000231B Додайте id товару")


async def del_id(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["id_product"] = int(m.text)
            id_product = data.get("id_product")
        except ValueError:
            await m.answer("\U0000203C Потрібно ввести число")
        else:
            try:
                await del_item(id_product)
            except AttributeError:
                await m.reply("\U0000203C Такого товару не існує")
            else:
                await m.answer("Товар видалено")
        await state.finish()


def register_del_product_hendlers(dp: Dispatcher):
    dp.register_message_handler(delete_item, CheckAdmin(),
                                Text(equals=["\U0000274C Видалити товар"],
                                     ignore_case="/"))
    dp.register_message_handler(del_id, state=DelProduct.id_product)
