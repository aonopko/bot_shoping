from aiogram.types import CallbackQuery
from aiogram import Dispatcher


from db.db_commands import get_socks


async def woman_hot_socks(call: CallbackQuery):
    hot_socks = await get_socks(category_code="H",
                                sub_category_code="W")
    if hot_socks:
        for i in hot_socks:
            await call.message.answer_photo(i.photo, f"  id: {i.id_product}\n"
                                                     f"- {i.category}\n"
                                                     f"- {i.sub_category}\n"
                                                     f"- Ціна {i.price} грн.",
                                            reply_markup=await buy_button())
    else:
        await call.message.answer("Зараз такого товару не існує")
    await call.answer()


async def woman_summer_socks(call: CallbackQuery):
    hot_socks = await get_socks(category_code="S",
                                sub_category_code="W")
    if hot_socks:
        for i in hot_socks:
            await call.message.answer_photo(i.photo, f"  id: {i.id_product}\n"
                                                     f"- {i.category}\n"
                                                     f"- {i.sub_category}\n"
                                                     f"- Ціна {i.price} грн.",
                                            reply_markup=await buy_button())
    else:
        await call.message.answer("Зараз такого товару не існує")
    await call.answer()


async def woman_new_year_socks(call: CallbackQuery):
    hot_socks = await get_socks(category_code="NY",
                                sub_category_code="W")
    if hot_socks:
        for i in hot_socks:
            await call.message.answer_photo(i.photo, f"  id: {i.id_product}\n"
                                                     f"- {i.category}\n"
                                                     f"- {i.sub_category}\n"
                                                     f"- Ціна {i.price} грн.",
                                            reply_markup=await buy_button())
    else:
        await call.message.answer("Зараз такого товару не існує")
    await call.answer()


def register_woman_socks(dp: Dispatcher):
    dp.register_callback_query_handler(woman_hot_socks,
                                       text="hot_woman")
    dp.register_callback_query_handler(woman_summer_socks,
                                       text="summer_woman")
    dp.register_callback_query_handler(woman_new_year_socks,
                                       text="new_year_woman")
