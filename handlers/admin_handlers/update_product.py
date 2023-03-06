from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from loguru import logger


from filters.bot_filter import CheckAdmin
from states.admin_state import UpdateProduct
from keyboards.default.admin_keyboard import update_product
from db.db_commands import UpdateData, update_db_promotion, delete_promotion, update_db_new_item, delete_new_item
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
            button = InlineKeyboardButton(text="Додати акцію", callback_data="yes")
            button_1 = InlineKeyboardButton(text="ВІдмінити", callback_data="no")
            button_2 = InlineKeyboardButton(text="Видалити акцію", callback_data="delete")
            keyboard = InlineKeyboardMarkup()
            keyboard.add(button, button_2, button_1)
            await m.answer("Меню акції", reply_markup=keyboard)
            await UpdateProduct.promotion.set()
        else:
            await m.answer("\U0000203C З початку треба додати id")


async def yes_promotion(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["promotion"] = 1
        except ValueError:
            await call.message.answer("\U0000203C Потрібно ввести число")
        else:
            id_product = data.get("id_product")
            promotion = data.get("promotion")
        try:
            await update_db_promotion(id_product, promotion)
        except AttributeError:
            await call.message.answer("\U0000203C Нажаль такого товару не існує")
            data.clear()
        else:
            await call.message.answer("Акцію додано \U0001F44D")
            await call.answer()
        await state.finish()


async def no_promotion(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.message.answer("Відміна")
        await call.answer()
        data.clear()
        await state.finish()


async def del_promotion(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        id_product = data.get("id_product")
        try:
            await delete_promotion(id_product)
        except AttributeError:
            await call.message.answer("\U0000203C Нажаль такого товару не існує")
            data.clear()
        else:
            await call.message.answer("Акцію видалено \U0001F44D")
            await call.answer()
        await state.finish()


async def add_new_item(m: Message, state: FSMContext):
    async with state.proxy() as data:
        if data:
            button = InlineKeyboardButton(text="Додати новинку", callback_data="yes_item")
            button_1 = InlineKeyboardButton(text="ВІдмінити", callback_data="no_item")
            button_2 = InlineKeyboardButton(text="Видалити новинку", callback_data="delete_item")
            keyboard = InlineKeyboardMarkup()
            keyboard.add(button, button_2, button_1)
            await m.answer("Меню новинки", reply_markup=keyboard)
            await UpdateProduct.new_product.set()
        else:
            await m.answer("\U0000203C З початку треба додати id")


async def yes_new_item(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["new_product"] = 1
        except ValueError:
            await call.message.answer("\U0000203C Потрібно ввести число")
        else:
            id_product = data.get("id_product")
            new_product = data.get("new_product")
        try:
            await update_db_new_item(id_product, new_product)
        except AttributeError:
            await call.message.answer("\U0000203C Нажаль такого товару не існує")
            data.clear()
        else:
            await call.message.answer("Новинку додано \U0001F44D")
            await call.answer()
        await state.finish()


async def cancel_new_item(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.message.answer("Відміна")
        await call.answer()
        data.clear()
        await state.finish()


async def del_new_item(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        id_product = data.get("id_product")
        try:
            await delete_new_item(id_product)
        except AttributeError:
            await call.message.answer("\U0000203C Нажаль такого товару не існує")
            data.clear()
        else:
            await call.message.answer("Новинку видалено \U0001F44D")
            await call.answer()
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
                                text=["\U0001F525 Акція"])
    dp.register_callback_query_handler(yes_promotion,
                                       state=UpdateProduct.promotion,
                                       text="yes")
    dp.register_callback_query_handler(no_promotion,
                                       state=UpdateProduct.promotion,
                                       text="no")
    dp.register_callback_query_handler(del_promotion,
                                       state=UpdateProduct.promotion,
                                       text="delete")
    dp.register_message_handler(add_new_item, CheckAdmin(),
                                text=["Новинка"])
    dp.register_callback_query_handler(yes_new_item,
                                       state=UpdateProduct.new_product,
                                       text="yes_item")
    dp.register_callback_query_handler(cancel_new_item,
                                       state=UpdateProduct.new_product,
                                       text="no_item")
    dp.register_callback_query_handler(del_new_item,
                                       state=UpdateProduct.new_product,
                                       text="delete_item")
