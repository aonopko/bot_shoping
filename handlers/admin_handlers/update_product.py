from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from loguru import logger

from filters.bot_filter import CheckAdmin
from states.admin_state import UpdateProduct
from keyboards.default.admin_keyboard import update_product
from db.db_commands import UpdateData
from keyboards.default.admin_keyboard import admin_menu


async def update_products(m: Message):
    await m.answer(text="Ваше меню для оновлення",
                   reply_markup=update_product)


async def back(m: Message):
    await m.answer(text="Панель адміна",
                   reply_markup=admin_menu)


async def add_id(m: Message):
    await UpdateProduct.id_product.set()
    await m.answer("Додайте id")


async def update_id(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["id_product"] = int(m.text)
        except ValueError:
            await m.reply("\U0000203C Потрібно ввести число")
        else:
            await m.answer("Додайте дані товару які бажаєте змінити \U0001F44D")
            await state.reset_state()


async def add_foto(m: Message, state: FSMContext):
    async with state.proxy() as data:
        if data:
            await m.answer("Додайте фото")
            await UpdateProduct.photo.set()
        else:
            await m.answer("\U0000203C З початку треба додати id")


async def update_photo(m: Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = m.photo[0].file_id
        id_product = data.get("id_product")
        photo = data.get("photo")
        update = UpdateData(id_product, photo)
        try:
            await update.update_db_photo()
            await m.answer("Фото змінено \U0001F44D")
        except AttributeError:
            await m.answer("\U0000203C Нажаль такого товару не існує")
            data.clear()
        await state.finish()


async def add_price(m: Message, state: FSMContext):
    async with state.proxy() as data:
        if data:
            await m.answer("Додайте ціну")

            await UpdateProduct.price.set()
        else:
            await m.answer("\U0000203C З початку треба додати id")


async def update_price(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["price"] = int(m.text)
        except ValueError:
            await m.reply("\U0000203C Потрібно ввести число")
        else:
            id_product = data.get("id_product")
            price = data.get("price")
            update = UpdateData(id_product, price)
            try:
                await update.update_db_price(id_product, price)
            except AttributeError:
                await m.reply("\U0000203C Нажаль такого товару не існує")
                data.clear()
            else:
                await m.answer("Ціну змінено \U0001F44D")
        await state.finish()


async def add_quantity(m: Message, state: FSMContext):
    async with state.proxy() as data:
        if data:
            await m.answer("Додайте кількість")
            await UpdateProduct.quantity.set()
        else:
            await m.answer("\U0000203C З початку треба додати id")


async def update_quantity(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["quantity"] = int(m.text)
        except ValueError:
            await m.reply("\U0000203C Потрібно ввести число")
        else:
            id_product = data.get("id_product")
            quantity = data.get("quantity")
            update = UpdateData(id_product, quantity)
            try:
                await update.update_db_quantity(id_product, quantity)
            except AttributeError:
                await m.reply("\U0000203C Нажаль такого товару не існує")
                data.clear()
            else:
                await m.answer("Кількість змінено \U0001F44D")
            await state.finish()


async def add_promotion(m: Message, state: FSMContext):
    async with state.proxy() as data:
        if data:
            await m.answer("Додати акцію")
            await UpdateProduct.promotion.set()
            logger.info(data)
        else:
            await m.answer("\U0000203C З початку треба додати id")


async def update_promotion(m: Message, state: FSMContext):
    async with state.proxy() as data:
        logger.info(data)
        data["promotion"] = True
        id_product = data.get("id_product")
        promotion = data.get("promotion")
        logger.info(data)
        update = UpdateData(id_product, promotion)
        try:
            await update.update_db_quantity(id_product, promotion)
        except AttributeError:
            await m.reply("\U0000203C Нажаль такого товару не існує")
            data.clear()
        else:
            await m.answer("Акцію додано \U0001F44D")
        await state.finish()


def register_update_product_hendlers(dp: Dispatcher):
    dp.register_message_handler(back, CheckAdmin(),
                                text=["\U000025C0 Назад"])
    dp.register_message_handler(update_products, CheckAdmin(),
                                text=["\U0001f504 Оновити товар"])
    dp.register_message_handler(add_id, CheckAdmin(),
                                text=["\U0001F194 Додати id"])
    dp.register_message_handler(update_id,
                                state=UpdateProduct.id_product)
    dp.register_message_handler(add_foto, CheckAdmin(),
                                text=["\U0001F4F7 Фото"])
    dp.register_message_handler(update_photo,
                                state=UpdateProduct.photo,
                                content_types=["photo"])
    dp.register_message_handler(add_price, CheckAdmin(),
                                text=["\U0001F4C8 Ціну"])
    dp.register_message_handler(update_price,
                                state=UpdateProduct.price)
    dp.register_message_handler(add_quantity, CheckAdmin(),
                                text=["\U0001F4CA Кількість"])
    dp.register_message_handler(update_quantity,
                                state=UpdateProduct.quantity)
    dp.register_message_handler(add_promotion, CheckAdmin(),
                                text=["Додати акцію"])
    dp.register_message_handler(update_promotion,
                                state=UpdateProduct.promotion)
