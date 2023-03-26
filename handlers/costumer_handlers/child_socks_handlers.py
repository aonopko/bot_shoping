from aiogram.types import CallbackQuery
from aiogram import Dispatcher


from db.db_commands import get_socks


async def child_hot_socks(call: CallbackQuery):
    hot_socks = await get_socks(category_code="H",
                                sub_category_code="CH")
    if hot_socks:
        for i in hot_socks:
            await call.message.answer_photo(i.photo, f"  id: {i.id_product}\n"
                                                     f"- {i.category}\n"
                                                     f"- {i.sub_category}\n"
                                                     f"- Ціна {i.price} грн.")
    else:
        await call.message.answer("Зараз такого товару не існує")
    await call.answer()


async def child_summer_socks(call: CallbackQuery):
    hot_socks = await get_socks(category_code="S",
                                sub_category_code="CH")
    if hot_socks:
        for i in hot_socks:
            await call.message.answer_photo(i.photo, f"  id: {i.id_product}\n"
                                                     f"- {i.category}\n"
                                                     f"- {i.sub_category}\n"
                                                     f"- Ціна {i.price} грн.")
    else:
        await call.message.answer("Зараз такого товару не існує")
    await call.answer()


async def child_new_year_socks(call: CallbackQuery):
    hot_socks = await get_socks(category_code="NY",
                                sub_category_code="CH")
    if hot_socks:
        for i in hot_socks:
            await call.message.answer_photo(i.photo, f"  id: {i.id_product}\n"
                                                     f"- {i.category}\n"
                                                     f"- {i.sub_category}\n"
                                                     f"- Ціна {i.price} грн.")
    else:
        await call.message.answer("Зараз такого товару не існує")
    await call.answer()


def register_child_socks(dp: Dispatcher):
    dp.register_callback_query_handler(child_hot_socks,
                                       text="hot_child")
    dp.register_callback_query_handler(child_summer_socks,
                                       text="summer_child")
    dp.register_callback_query_handler(child_new_year_socks,
                                       text="new_year_child")
