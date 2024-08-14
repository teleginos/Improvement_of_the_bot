from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from states import UserState

from keyboard.inline.generator_inline import generator_inline

router = Router()


@router.message(F.text.lower() == 'рассчитать')
async def main_menu(message: types.Message):
    inline = await generator_inline(['Рассчитать норму калорий', 'Формула расчета'], 2)
    await message.answer("Выберите опцию", reply_markup=inline)


@router.callback_query(lambda c: c.data.lower() == 'рассчитать норму калорий')
async def set_age(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer('Укажите свой возраст: ')
    await state.set_state(UserState.age)


@router.callback_query(lambda c: c.data.lower() == 'формула расчета')
async def get_formulas(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Формула расчета:\n"
                                        "1. Мужчина: BMR = 66 + (6.23 * вес) + (12.7 * рост) - (6.8 * возраст)")


@router.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        await state.update_data(age=age)
        await message.answer('Укажите ваш рост в сантиметрах: ')
        await state.set_state(UserState.growth)
    except ValueError:
        await message.answer('Пожалуйста, введите корректное числовое значение для возраста')


@router.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    try:
        growth = float(message.text)
        await state.update_data(growth=growth)
        await message.answer('Укажите ваш вес в килограммах: ')
        await state.set_state(UserState.weight)
    except ValueError:
        await message.answer('Пожалуйста, введите корректное числовое значение для роста')


@router.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    try:
        weight = int(message.text)
        await state.update_data(weight=weight)

        user_data = await state.get_data()
        age = user_data['age']
        growth = user_data['growth']

        # Формула Харриса-Бенедикта для мужчин
        brm = 88.36 + (13.4 * weight) + (4.8 * growth) - (5.7 * age)

        await message.answer(f'Ваш базовый метаболизм составляет примерно {brm} ккал в день')
        await state.clear()
    except ValueError:
        await message.answer('Пожалуйста, введите корректное числовое значение для веса')
