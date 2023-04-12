from aiogram.dispatcher import FSMContext
from loguru import logger
from aiogram.types import CallbackQuery
from aiogram.types import Message, InputMediaPhoto
from aiogram import Dispatcher


from keyboards.default.costumer_keyboard import cart
from db.db_commands import CustomerCart
from keyboards.inline.customer_kb import not_paid_kb, delete_product


async def basket(m: Message):
    await m.answer("Ваши замовлення",
                   reply_markup=cart)


async def change_order(m: Message):
    id_customer = m.from_user.id
    get_not_paid = await CustomerCart.not_paid_cart(id_customer=id_customer)
    for i in get_not_paid:
        logger.info(i.photo)
        logger.info(i.product_id)
        await m.answer_photo(i.photo, f"Артикул: {i.product_id}\n"
                                      f"Кількість: {i.quantity}шт.\n"
                                      f"Ціна: {i.price} грн.\n",
                             reply_markup=await not_paid_kb(i.product_id))
        logger.info(i.price)


async def your_order(m: Message):
    id_customer = m.from_user.id
    order = await CustomerCart.not_paid_cart(id_customer)
    album = []
    logger.info(order)
    my_sum = 0
    for i in order:
        my_sum += i.price * i.quantity
        album.append(InputMediaPhoto(i.photo, f"Артикул: {i.product_id}\n"
                                              f"Кількість: {i.quantity}\n"
                                              f"Ціна: {i.price}\n"
                                              f"Загальна вартість: {i.price * i.quantity} грн."))
        logger.info(album)
    await m.answer_media_group(media=album)
    await m.answer(f"Загальна сума замовлення: {my_sum}")


async def del_item_cart(call: CallbackQuery, callback_data: dict,
                        state: FSMContext):
    async with state.proxy() as data:
        id_customer = call.from_user.id
        id_item = data["id_product"] = int(callback_data.get("id_product"))
        logger.info(id_item)
        logger.info(id_customer)
        await CustomerCart.del_cart_item(product_id=id_item,
                                         customer_id=id_customer)
        await call.message.answer("OK")


def register_basket_hendlers(dp: Dispatcher):
    dp.register_message_handler(basket, text=["Кошик"],
                                state="*")
    dp.register_message_handler(change_order,
                                text="Змінити замовлення")
    dp.register_message_handler(your_order,
                                text="Ваше замовлення")
    dp.register_callback_query_handler(del_item_cart, delete_product.filter())
