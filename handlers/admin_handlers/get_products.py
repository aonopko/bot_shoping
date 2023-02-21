import types
from loguru import logger
from aiogram.types import Message, MediaGroup, InputMediaPhoto
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

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
                logger.info(f"{photo.photo}")
                await m.answer_photo(photo.photo, f"id {photo.id_product},\n"
                                                  f" name {photo.name}\n"
                                                  f"photo {photo.price}")
                await state.finish()


async def find_all_photo(m: Message):
    find_photo = await get_all_photo()
    logger.info(find_photo)
    v = 0
    while len(find_photo):
        for i in find_photo:
            album = [
                InputMediaPhoto(i.photo[v])
        ]
            v += 1
            logger.info(album)
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
