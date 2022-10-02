import io

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters.admin_filter import AdminFilter
from filters.chat_filter import IsGroup
from loader import dp, bot


@dp.message_handler(IsGroup(), Command('update_photo'), AdminFilter())
async def update_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(path_or_bytesio=photo)
    await bot.set_chat_photo(chat_id=message.chat.id, photo=input_file)
    await message.delete()


@dp.message_handler(IsGroup(), Command('set_title'), AdminFilter())
async def update_photo(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    await message.chat.set_title(title)
    await message.delete()
