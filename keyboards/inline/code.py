from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

code = InlineKeyboardMarkup(row_width=3,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(text='Открыть', url='https://github.com/bichief/chat-bot')
                                ]
                            ])