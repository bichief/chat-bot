from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

next_step = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text='нажми на меня, зайка', callback_data='click')
        ]
])

last_step = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Ввести пароль', callback_data='insert_pass')
        ]
])