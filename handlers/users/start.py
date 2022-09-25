import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Text, Command
from keyboards.inline.next import next_step, last_step
from loader import dp, bot
from states.inserting import TryingCatch


@dp.message_handler(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer('Привет')
