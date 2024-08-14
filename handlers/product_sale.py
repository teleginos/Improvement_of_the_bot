from aiogram import Router, F, types

from keyboard.inline.generator_inline import generator_inline
from database.db import get_all

router = Router()


@router.message(F.text.lower() == 'купить')
async def get_buying_list(message: types.Message):
    products = await get_all()
    for product, price, description, image_url in products:
        print(image_url)
        # with open(absolute_image_path, 'r') as image_file:

        caption = f"Название:{product} | Описание: {description} | Цена: {price}"
        await message.answer_photo(photo=image_url, caption=caption)
    keyboard = await generator_inline([product[0] for product in products], 4)
    await message.answer('Выберите продукт для покупки:',
                         reply_markup=keyboard)


@router.callback_query(lambda c: c.data.lower() in ['product1', 'product2', 'product3', 'product4'])
async def buy_product(callback_query: types.CallbackQuery):
    product_name = callback_query.data
    await callback_query.message.answer(f"Вы вы успешно приобрели {product_name}")
