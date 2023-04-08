from aiogram.types import Message, InputMediaPhoto
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from keyboards.inline.customer_kb import not_paid_kb
from filters.bot_filter import CheckAdmin
from db.db_commands import get_item, get_all_photo
from states.admin_state import GetProduct


async def id_item(m: Message):
    await GetProduct.id_product.set()
    await m.answer("\U0000231B Додайте id товару")


async def find_item_id(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["id_product"] = int(m.text)
            id_product = data.get("id_product")
        except ValueError:
            await m.answer("\U0000203C Потрібно ввести число")
        else:
            try:
                photo = await get_item(id_product)
            except AttributeError:
                await m.answer("\U0000203C Такого товару не існує")
            else:
                await m.answer_photo(photo.photo, f"id {photo.id_product},\n"
                                                  f"{photo.name}\n"
                                                  f"ціна {photo.price} грн")
            await state.finish()


async def find_all_photo(m: Message):
    find_photo = await get_all_photo()
    album = []
    for i in find_photo:

        album.append(InputMediaPhoto(i.photo, f"id: {i.id_product}"))
    await m.answer_media_group(media=album)


def register_get_all_items(dp: Dispatcher):
    dp.register_message_handler(id_item, CheckAdmin(),
                                Text(equals=["Знайти товар по id"],
                                     ignore_case="/"))
    dp.register_message_handler(find_item_id, CheckAdmin(),
                                state=GetProduct.id_product)
    dp.register_message_handler(find_all_photo, CheckAdmin(),
                                Text(equals=["Знайти товар по фото"],
                                     ignore_case="/"))
