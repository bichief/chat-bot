from data.config import CHAT_ID
from loader import dp


async def start_lesson():
    await dp.bot.send_message(
        chat_id=CHAT_ID,
        text='👨‍💻 Привет!\n\n'
             '🙆🏼 Хочу тебе напомнить, что через 30 минут начинается занятие!\n\n'
             '📍 Тема занятия: <b>Разбор API, посмотрим наш темплейт и начнем кодить :)</b>'
             '📍 Ссылка для подключения: <a href="https://discord.com/channels/687964407975772160/1015896927566573568"> здесь, нажми</a>',
        disable_web_page_preview=True
    )