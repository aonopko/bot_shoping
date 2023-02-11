from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from filters.bot_filter import CheckAdmin
from states.admin_state import UpdateProduct
from keyboards.default.admin_keyboard import update_product
from db.db_commands import update_item


async def update_products(m: Message):
    await m.answer(text="Ваше меню для оновлення",
                   reply_markup=update_product)


async def add_foto(m: Message):
    await m.answer("Додайте фото")
    await UpdateProduct.photo.set()


async def update_photo(m: Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = m.photo[0].file_id
        await m.answer("Фото додано \U0001F44D")
        await state.reset_state()


async def add_price(m: Message):
    await m.answer("Додайте ціну")
    await UpdateProduct.price.set()


async def update_price(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["price"] = int(m.text)
        except ValueError:
            await m.answer("\U0000203C Потрібно ввести число")
        else:
            await m.answer("Ціну додано \U0001F44D")
        await state.reset_state()


async def add_quantity(m: Message):
    await m.answer("Додайте кількість")
    await UpdateProduct.quantity.set()


async def update_quantity(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["quantity"] = int(m.text)
        except ValueError:
            await m.answer("\U0000203C Потрібно ввести число")
        else:
            await m.answer("Кількість додано \U0001F44D")
        await state.reset_state()


async def add_update(m: Message):
    await m.answer("\U0000231B Додайте id товару")
    await UpdateProduct.id_product.set()


async def update_id(m: Message, state: FSMContext):
    async with state.proxy() as data:
        if not data:
            await state.reset_state()
            await m.answer("\U0000203C Потрібно ввести данні")
        else:
            try:
                data["id_product"] = int(m.text)
            except ValueError:
                await m.answer("\U0000203C Потрібно ввести число")
            else:
                await state.reset_state()
                get_args = data.get("id_product")
                get_photo = data.get("photo")
                get_quantity = data.get("quantity")
                get_price = data.get("price")
                try:
                    await update_item(get_args,
                                      photo=get_photo,
                                      price=get_price,
                                      quantity=get_quantity)
                except AttributeError:
                    await m.answer("\U0000203C Такого id не існує")


def register_update_product_hendlers(dp: Dispatcher):
    dp.register_message_handler(update_products, CheckAdmin(),
                                text=["\U0001f504 Оновити товар"])
    dp.register_message_handler(add_update, CheckAdmin(),
                                text=["Додати"])
    dp.register_message_handler(update_id,
                                state=UpdateProduct.id_product)
    dp.register_message_handler(add_foto, CheckAdmin(),
                                text=["Фото"])
    dp.register_message_handler(update_photo,
                                state=UpdateProduct.photo,
                                content_types=["photo"])
    dp.register_message_handler(add_price, CheckAdmin(),
                                text=["Ціну"])
    dp.register_message_handler(update_price,
                                state=UpdateProduct.price)
    dp.register_message_handler(add_quantity, CheckAdmin(),
                                text=["Кількість"])
    dp.register_message_handler(update_quantity,
                                state=UpdateProduct.quantity)
