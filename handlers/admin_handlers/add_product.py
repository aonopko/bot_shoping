from aiogram.types import Message, CallbackQuery
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from filters.bot_filter import CheckAdmin
from states.admin_state import AddProduct
from keyboards.inline.callback_datas import add_callback, delete_callback
from keyboards.inline.admin_kb import add_product


async def add_id(m: Message):
    await AddProduct.id_product.set()
    await m.answer("Додайте id товару")


async def load_id(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["id_product"] = int(m.text)
        except ValueError:
            await m.answer("\U0001F69A  Потрібно ввести число")
        else:
            await AddProduct.next()
            await m.answer("id завантажено")
            await m.answer("Додайте назву товару")


async def load_name(m: Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = m.text
    await m.answer("Назву додано")
    await AddProduct.next()
    await m.answer("Додайте категорию товару")


async def load_category(m: Message, state: FSMContext):
    async with state.proxy() as data:
        data["category"] = m.text
        await m.answer("Категорію додано")
        await AddProduct.next()
        await m.answer("Додайте підкатегорію")


async def load_sub_category(m: Message, state: FSMContext):
    async with state.proxy() as data:
        data["sub_category"] = m.text
        await m.answer("ПідКатегорію додано")
        await AddProduct.next()
        await m.answer("Додайте ціну товара")


async def load_price(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["price"] = int(m.text)
        except ValueError:
            await m.answer("Потрібно ввести число")
        else:
            await m.answer("Ціну додано")
            await AddProduct.next()
            await m.answer("Додайте кількість товару")


async def load_quantity(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["quantity"] = int(m.text)
        except ValueError:
            await m.answer("Потрібно ввести число")
        else:
            await m.answer("Кількість додано")
            await AddProduct.next()
            await m.answer("Додайте фото товру")


async def load_photo(m: Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = m.photo[0].file_id
        await m.answer("фото додано", )
        await AddProduct.next()
        await m.answer("НАТИСНИТЬ ЩО НЕБУДЬ", reply_markup=add_product)


async def test(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Нажали єту кнопку")
    await call.answer()
    await state.finish()


def register_add_product_handlers(dp: Dispatcher):
    dp.register_message_handler(add_id, CheckAdmin(),
                                Text(equals=["Додати товар"], ignore_case="/"))
    dp.register_message_handler(load_id,
                                state=AddProduct.id_product)
    dp.register_message_handler(load_name,
                                state=AddProduct.name)
    dp.register_message_handler(load_category,
                                state=AddProduct.category)
    dp.register_message_handler(load_sub_category,
                                state=AddProduct.sub_category)
    dp.register_message_handler(load_price,
                                state=AddProduct.price)
    dp.register_message_handler(load_quantity,
                                state=AddProduct.quantity)
    dp.register_message_handler(load_photo, content_types=["photo"],
                                state=AddProduct.photo)
    dp.register_callback_query_handler(test, add_callback.filter(add_prod="add_item"),
                                       state=AddProduct.add_prod)
