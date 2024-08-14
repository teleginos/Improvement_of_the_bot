from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


async def generator_reply(key_list, buttons_in_a_row):
    kb = [[]]
    for key in key_list:
        if len(kb[-1]) == buttons_in_a_row:
            kb.append([])
        kb[-1].append(KeyboardButton(text=key))

    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    return keyboard
