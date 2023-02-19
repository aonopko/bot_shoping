from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
#
from filters.bot_filter import CheckAdmin
from db.db_commands import get_all_items


async def get_items(m: Message):
    get_items = await get_all_items()
    await m.answer(f"Привіт {str(get_items)}")


def register_get_all_items(dp: Dispatcher):
    dp.register_message_handler(get_items, CheckAdmin(),
                                Text(equals=["Переглянути товар"],
                                     ignore_case="/"))
