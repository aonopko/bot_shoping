from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram import Dispatcher

from db.db_commands import get_admin


class CheckAdmin(BoundFilter):
    async def check(self, m: types.Message) -> bool:
        return await get_admin(m.from_user.id)


def register_filters(dp: Dispatcher):
    dp.filters_factory.bind(CheckAdmin)
