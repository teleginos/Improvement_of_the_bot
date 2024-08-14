from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def generator_inline(key_list, buttons_in_a_row):
    buttons = [[]]
    for key in key_list:
        if len(buttons[-1]) < buttons_in_a_row:
            buttons[-1].append(InlineKeyboardButton(text=key, callback_data=str(key)))
        else:
            buttons.append([InlineKeyboardButton(text=key, callback_data=str(key))])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard
