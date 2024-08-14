from aiogram import Router, types
from aiogram.filters import Command

from keyboard.reply.generator_reply import generator_reply

router = Router()


@router.message(Command('start'))
async def start_handlers(message: types.Message):
    keyboard = await generator_reply(['Рассчитать', 'Информация', 'Купить'], 2)
    await message.answer("Привет! Я бот помогающий твоему здоровью.",
                         reply_markup=keyboard)

