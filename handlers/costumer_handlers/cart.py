from aiogram.dispatcher import FSMContext
from loguru import logger
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup,\
    CallbackQuery
from aiogram import Dispatcher
from asyncpg.exceptions import UniqueViolationError

from keyboards.default.admin_keyboard import update_product
from keyboards.default.costumer_keyboard import cart
from db.db_commands import get_promotion, get_new_product,\
    add_user, get_item, add_cart, not_paid_cart
from keyboards.inline.customer_kb import buy_button, buy_product, not_paid_kb
from states.customers_state import ProductQuantity


async def basket(m: Message):
    await m.answer("Ваши замовлення",
                   reply_markup=cart)


async def not_paid(m: Message):
    id_customer = m.from_user.id
    logger.info(id_customer)
    get_not_paid = await not_paid_cart(id_customer=id_customer)
    logger.info(get_not_paid)
    for i in get_not_paid:
        logger.info(i.photo)
        await m.answer_photo(i.photo, f"Артикул {i.product_id},\n"
                                      f"Кількість {i.quantity}",
                             reply_markup=await not_paid_kb())


def register_basket_hendlers(dp: Dispatcher):
    dp.register_message_handler(basket, text=["Кошик"],
                                state="*")
    dp.register_message_handler(not_paid,
                                text="Неоплочені замовлення")
