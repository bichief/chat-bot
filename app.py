import asyncio

import aioschedule
from aiogram import executor


from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


async def scheduler():
    aioschedule.every().sunday.at('10:30').do(start_lesson)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


if __name__ == '__main__':
    from utils.misc.mailing import start_lesson
    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())
    executor.start_polling(dp, on_startup=on_startup)
