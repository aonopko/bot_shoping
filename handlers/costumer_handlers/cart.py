
from loguru import logger
from aiogram.types import Message, InputMediaPhoto
from aiogram import Dispatcher


from keyboards.default.costumer_keyboard import cart
from db.db_commands import CustomerCart
from keyboards.inline.customer_kb import not_paid_kb


async def basket(m: Message):
    await m.answer("Ваши замовлення",
                   reply_markup=cart)


async def change_order(m: Message):
    id_customer = m.from_user.id
    get_not_paid = await CustomerCart.not_paid_cart(id_customer=id_customer)
    for i in get_not_paid:
        logger.info(i.photo)
        await m.answer_photo(i.photo, f"Артикул {i.product_id},\n"
                                      f"Кількість {i.quantity}",
                             reply_markup=await not_paid_kb())


async def your_order(m: Message):
    id_customer = m.from_user.id
    order = await CustomerCart.not_paid_cart(id_customer)
    album = []
    logger.info(order)
    for i in order:
        album.append(InputMediaPhoto(i.photo, f"Артикул: {i.product_id}\n"
                                              f"Кількість: {i.quantity}\n"
                                              f": "))
        logger.info(i.photo)
    await m.answer_media_group(media=album)
def register_basket_hendlers(dp: Dispatcher):
    dp.register_message_handler(basket, text=["Кошик"],
                                state="*")
    dp.register_message_handler(change_order,
                                text="Неоплочені замовлення")
    dp.register_message_handler(your_order,
                                text="Ваше замовлення")
