import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text, Command
from keyboards.inline.next import next_step, last_step
from loader import dp, bot
from states.inserting import TryingCatch


@dp.message_handler(Command('start'))
async def start_cmd(message: types.Message):
    global msg
    note_id = 'DQACAgIAAxkBAAM5YnQkAaisK0aRCMICsw1SA3KrHq0AAnAbAAJk56FLVOB5eIEFduMkBA'
    if message.get_args() == '4G43o4198S12H549A':
        msg = await bot.send_video_note(chat_id=message.chat.id, video_note=note_id, reply_markup=next_step)
        # await message.answer('<b>Гоша, гошечка, гошанчик, дружок, друг, дружище</b>\n\n'
        #                      'Вероятнее всего, ты зашел сюда, когда мы уже все собрались, сидим в сауне\n\n'
        #                      'Я хотел бы, чтобы ты смотрел на это все уже выпившим, так душевнее будет, считаю\n'
        #                      'А как все получилось, не знаю :)\n\n'
        #                      'Для продолжения, просто <b>нажми на кнопку</b> ниже ', reply_markup=next_step)
    else:
        await message.answer('Прости, но данный бот был создан только для Гоши!')


@dp.callback_query_handler(Text(equals='click'))
async def first_button(call: types.CallbackQuery):
    await msg.delete()
    await call.message.answer('хахаххахах, ты думаешь что все настолько легко?\n\n'
                              'Чтобы получить <b>доступ к подарку</b>, ты должен <b>подобрать пароль</b>, '
                              'узнав цифры у находящихся :)\n\n'
                              'Как все узнаешь, нажми на кнопочку))', reply_markup=last_step)


@dp.callback_query_handler(Text(equals='insert_pass'))
async def last_button(call: types.CallbackQuery):
    await call.message.edit_text('Хорошо. Отправь мне КОД, состоящий из 4 цифр :)')
    await TryingCatch.first()


@dp.message_handler(state=TryingCatch.password)
async def trying_password(message: types.Message, state: FSMContext):
    if message.text == '1488':
        await message.answer('Умничка!\n'
                             'Подарок ты увидишь через три секунды :)')
        await state.reset_state()
        await asyncio.sleep(3)

        # тут кружочки
    else:
        await message.answer('Жесть.. Неправильно, пробуй еще раз :(')
