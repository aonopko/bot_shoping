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
        await m.answer("НАТИСНИТЬ ЩО НЕБУДЬ", reply_markup=add_product)


async def inline_del(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Додайте товар спочатку")
    await call.answer()
    await state.finish()



# async def inline_add(call: CallbackQuery, state: FSMContext):
#     await AddProduct.add_prod.set()
#     await call.message.answer("Нажали єту кнопку")
#     await call.answer()
#     await state.finish()





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
    # dp.register_callback_query_handler(inline_add,
    #                                    add_callback.filter(add_prod="add_item"),
    #                                    state=AddProduct.add_prod)
    dp.register_callback_query_handler(inline_del,
                                       delete_callback.filter(del_prod="del_item"),
                                       state=AddProduct.del_prod)
