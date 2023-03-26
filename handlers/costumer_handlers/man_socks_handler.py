from aiogram.types import CallbackQuery
from aiogram import Dispatcher


from keyboards.inline.customer_kb import buy_button
from db.db_commands import get_socks


async def man_hot_socks(call: CallbackQuery):
    hot_socks = await get_socks(category_code="H",
                                sub_category_code="M")
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


async def man_summer_socks(call: CallbackQuery):
    hot_socks = await get_socks(category_code="S",
                                sub_category_code="M")
    if hot_socks:
        for i in hot_socks:
            await call.message.answer_photo(i.photo, f"{i.name}\n"
                                                     f"{i.category}\n"
                                                     f"{i.sub_category}")
    else:
        await call.message.answer("Зараз такого товару не існує")
    await call.answer()


async def man_new_year_socks(call: CallbackQuery):
    hot_socks = await get_socks(category_code="NY",
                                sub_category_code="M")
    if hot_socks:
        for i in hot_socks:
            await call.message.answer_photo(i.photo, f"{i.name}\n"
                                                     f"{i.category}\n"
                                                     f"{i.sub_category}")
    else:
        await call.message.answer("Зараз такого товару не існує")
    await call.answer()


def register_man_socks(dp: Dispatcher):
    dp.register_callback_query_handler(man_hot_socks,
                                       text="hot_man")
    dp.register_callback_query_handler(man_summer_socks,
                                       text="summer_man")
    dp.register_callback_query_handler(man_new_year_socks,
                                       text="new_year_man")
