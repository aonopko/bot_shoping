from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup,\
    CallbackQuery
from aiogram import Dispatcher
from asyncpg.exceptions import UniqueViolationError

from keyboards.inline.customer_kb import buy_button
from keyboards.default.costumer_keyboard import categories
from db.db_commands import get_promotion, get_new_product,\
    add_user, add_order
from keyboards.default.costumer_keyboard import main_menu


async def back(m: Message):
    await m.answer(text="Панель адміна",
                   reply_markup=main_menu)


async def costumer_start(m: Message):
    user = {'name': m.from_user.username,
            "id_telegram": m.from_user.id}
    try:
        await add_user(**user)
    except UniqueViolationError:
        await m.answer(f"Привіт {user.get('name')}!!!")
    await m.answer("Ваше меню:", reply_markup=main_menu)


async def catalog_button(m: Message):
    await m.answer("Меню", reply_markup=categories)


async def hot_socks(m: Message):
    button = InlineKeyboardButton(text="Чоловічі",
                                  callback_data="hot_man")
    button_1 = InlineKeyboardButton(text="Жіночі",
                                    callback_data="hot_woman")
    button_2 = InlineKeyboardButton(text="Дитячі",
                                    callback_data="hot_child")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button, button_1, button_2)
    await m.answer("Обери свої шкарпетки", reply_markup=keyboard)


async def summer_socks(m: Message):
    button = InlineKeyboardButton(text="Чоловічі",
                                  callback_data="summer_man")
    button_1 = InlineKeyboardButton(text="Жіночі",
                                    callback_data="summer_woman")
    button_2 = InlineKeyboardButton(text="Дитячі",
                                    callback_data="summer_child")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button, button_1, button_2)
    await m.answer("Обери свої шкарпетки", reply_markup=keyboard)


async def new_year_socks(m: Message):
    button = InlineKeyboardButton(text="Чоловічі",
                                  callback_data="new_year_man")
    button_1 = InlineKeyboardButton(text="Жіночі",
                                    callback_data="new_year_woman")
    button_2 = InlineKeyboardButton(text="Дитячі",
                                    callback_data="new_year_child")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button, button_1, button_2)
    await m.answer("Обери свої шкарпетки", reply_markup=keyboard)


async def customer_promotion(m: Message):
    promotion = await get_promotion()
    if promotion:
        for i in promotion:
            await m.answer_photo(i.photo, f"{i.name},\n"
                                          f"{i.category},\n"
                                          f"{i.sub_category},\n"
                                          f"{i.price},\n",
                                 reply_markup=await buy_button())
    else:
        await m.answer("Зараз акції не має")


async def customer_new_product(m: Message):
    promotion = await get_new_product()
    if promotion:
        for i in promotion:
            await m.answer_photo(i.photo, f"{i.name},\n"
                                          f"{i.category},\n"
                                          f"{i.sub_category},\n"
                                          f"{i.price},\n",
                                 reply_markup=await buy_button())
    else:
        await m.answer("Зараз новинок не має")


async def buy(call: CallbackQuery):
    order = {"customer_id": call.from_user.id}
    await add_order(**order)
    await call.message.answer("Товар додано у кошик")
    await call.answer()


def register_costumer_handlers(dp: Dispatcher):
    dp.register_message_handler(back, text=['\U000021A9 Назад'],
                                state="*")
    dp.register_message_handler(costumer_start, commands=["start"],
                                state="*")
    dp.register_message_handler(catalog_button, text=["Каталог"],
                                state="*")
    dp.register_message_handler(hot_socks, text=["\U000026C4 Теплі"],
                                state="*")
    dp.register_message_handler(summer_socks, text=["\U00002600 Літні"],
                                state="*")
    dp.register_message_handler(new_year_socks, text=["\U00002744 Новорічні"],
                                state="*")
    dp.register_message_handler(customer_promotion, text=["\U0001F48E Акція"],
                                state="*")
    dp.register_message_handler(customer_new_product, text=["\U0001f195 Новинки"],
                                state="*")
    dp.register_callback_query_handler(buy, text="cust_prom")

