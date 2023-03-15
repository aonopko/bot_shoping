from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram import Dispatcher
from loguru import logger

from keyboards.default.costumer_keyboard import main_menu, categories
from db.db_commands import get_promotion


async def costumer_start(m: Message):
    await m.answer("Ваше меню", reply_markup=main_menu)


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
    button = InlineKeyboardButton(text="Купити", callback_data="cust_prom")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button)
    promotion = await get_promotion()
    for i in promotion:
        await m.answer_photo(i.photo, f"{i.name},\n"
                                      f"{i.category},\n"
                                      f"{i.sub_category},\n"
                                      f"{i.price},\n", reply_markup=keyboard)


def register_costumer_handlers(dp: Dispatcher):
    dp.register_message_handler(costumer_start, commands=["start"],
                                state="*")
    dp.register_message_handler(catalog_button, text=["Каталог"],
                                state="*")
    dp.register_message_handler(hot_socks, text=["\U000026C4 Теплі"],
                                state="*")
    dp.register_message_handler(summer_socks, text=["Літні"],
                                state="*")
    dp.register_message_handler(new_year_socks, text=["Новорічні"],
                                state="*")
    dp.register_message_handler(customer_promotion, text=["Акція"],
                                state="*")