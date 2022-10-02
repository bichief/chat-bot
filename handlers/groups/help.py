from aiogram import types
from aiogram.dispatcher.filters import Command

from filters.chat_filter import IsGroup
from loader import dp


@dp.message_handler(IsGroup(), Command('help'))
async def help_cmd(message: types.Message):
    await message.reply('👨🏼‍🔧Пока что я умею следующее:\n\n'
                        '- /ping | позволяет проверить работу бота\n'
                        '- /update_photo | изменить фото беседы (для админов)\n'
                        '- /set_title | изменить название беседы (для админов)\n\n'
                        'Так же я приветствую новых ребят в нашей беседе и напоминаю за 30 минут о начале занятия :)')
