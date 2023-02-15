from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from filters.bot_filter import CheckAdmin
from states.admin_state import UpdateProduct
from keyboards.default.admin_keyboard import update_product
from db.db_commands import UpdateData


async def update_products(m: Message):
    await m.answer(text="Ваше меню для оновлення",
                   reply_markup=update_product)


async def add_id(m: Message):
    await UpdateProduct.id_product.set()
    await m.answer("Додайте id")


async def update_id(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["id_product"] = int(m.text)
        except ValueError:
            await m.answer("\U0000203C Потрібно ввести число")
        else:
            await m.answer("Додайте дані товару які бажаєте змінити \U0001F44D")
            await state.reset_state()


async def add_foto(m: Message):
    await m.answer("Додайте фото")
    await UpdateProduct.photo.set()


async def update_photo(m: Message, state: FSMContext):
    async with state.proxy() as data:
        if not data:
            await m.answer("\U0000203C Треба додати id товару")
        else:
            data["photo"] = m.photo[0].file_id
            id_product = data.get("id_product")
            photo = data.get("photo")
            update = UpdateData(id_product, photo)
            try:
                await update.update_db_photo()
                await m.answer("Фото змінено \U0001F44D")
            except AttributeError:
                await m.answer("\U0000203C Нажаль такого товару не існує")
    await state.finish()


async def add_price(m: Message):
    await m.answer("Додайте ціну")
    await UpdateProduct.price.set()


async def update_price(m: Message, state: FSMContext):
    async with state.proxy() as data:
        if data:
            try:
                data["price"] = int(m.text)
            except ValueError:
                await m.answer("\U0000203C Потрібно ввести число")
            else:
                id_product = data.get("id_product")
                price = data.get("price")
                update = UpdateData(id_product, price)
                try:
                    await update.update_db_price(id_product, price)
                except AttributeError:
                    await m.answer("\U0000203C Нажаль такого товару не існує")
                    await state.finish()
                else:
                    await m.answer("Ціну змінено \U0001F44D")
        else:
            await m.answer("\U0000203C id треба додати")
        await state.finish()


async def add_quantity(m: Message):
    await m.answer("Додайте кількість")
    await UpdateProduct.quantity.set()


async def update_quantity(m: Message, state: FSMContext):
    async with state.proxy() as data:
        if data:
            try:
                data["quantity"] = int(m.text)
            except ValueError:
                await m.answer("\U0000203C Потрібно ввести число")
            else:
                id_product = data.get("id_product")
                quantity = data.get("quantity")
                u = UpdateData(id_product, quantity)
                try:
                    await u.update_db_quantity(id_product, quantity)
                except AttributeError:
                    await m.answer("\U0000203C Нажаль такого товару не існує")
                    await state.finish()
                else:
                    await m.answer("Кількість змінено \U0001F44D")
        else:
            await m.answer("\U0000203C id треба додати")
        await state.finish()


def register_update_product_hendlers(dp: Dispatcher):
    dp.register_message_handler(update_products, CheckAdmin(),
                                text=["\U0001f504 Оновити товар"])
    dp.register_message_handler(add_id, CheckAdmin(),
                                text=["Додати id"])
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
