from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from filters.bot_filter import CheckAdmin
from states.admin_state import AddProduct


async def add_id(m: Message):
    await AddProduct.id_product.set()
    await m.answer("\U0000231B Додайте id товару")


async def load_id(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["id_product"] = int(m.text)
        except ValueError:
            await m.answer("\U0000203C  Потрібно ввести число")
        else:
            await AddProduct.next()
            await m.answer("\U0000231B Додайте назву товару")


async def load_name(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["name"] = str(m.text)
        except ValueError:
            await m.answer("\U0000203C Потрібно ввести буквами")
        else:
            await AddProduct.next()
            await m.answer("\U0000231B Додайте категорию товару")


async def load_category(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["category"] = m.text
        except ValueError:
            await m.answer("\U0000203C Потрібно ввести буквами")
        else:
            await AddProduct.next()
            await m.answer("\U0000231B Додайте підкатегорію")


async def load_sub_category(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["sub_category"] = str(m.text)
        except ValueError:
            await m.answer("\U0000203C Потрібно ввести буквами")
        else:
            await AddProduct.next()
            await m.answer("\U0000231B Додайте ціну товара")


async def load_price(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["price"] = int(m.text)
        except ValueError:
            await m.answer("Потрібно ввести число")
        else:
            await AddProduct.next()
            await m.answer("\U0000231B Додайте кількість товару")


async def load_quantity(m: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["quantity"] = int(m.text)
        except ValueError:
            await m.answer("Потрібно ввести число")
        else:
            await AddProduct.next()
            await m.answer("\U0000231B Додайте фото товру")


async def load_photo(m: Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = m.photo[0].file_id
        await AddProduct.next()
        await m.answer("Натисни на кнопку щоб додати або видалити товар")


def register_add_product_handlers(dp: Dispatcher):
    dp.register_message_handler(add_id, CheckAdmin(),
                                Text(equals=["Додати товар"],
                                     ignore_case="/"))
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
