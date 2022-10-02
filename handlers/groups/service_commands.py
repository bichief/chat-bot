from aiogram import types
from aiogram.dispatcher.filters import Command

from filters.chat_filter import IsGroup
from keyboards.inline.code import code
from loader import dp, bot


@dp.message_handler(IsGroup(), Command('ping'))
async def start_chat_cmd(message: types.Message):
    await message.reply('pong!')


@dp.message_handler(IsGroup(), Command('code'))
async def show_code(message: types.Message):
    await message.answer('Исходный код бота доступен по кнопке ниже :)', reply_markup=code)


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    await message.reply(f'{message.from_user.get_mention(as_html=True)} теперь с нами, возрадуемся!')


@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def left_member(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f'{message.left_chat_member.get_mention(as_html=True)} покинул чат.\n\n'
                             f'Я написал ему, чтобы узнать причину.')
        # await dp.bot.send_message(
        #     chat_id=message.left_chat_member.id,
        #     text='Что случилось? Почему ты решил покинуть наши ряды в телеграмме?'
        # )
    elif message.from_user.id == (await bot.me).id:
        return
