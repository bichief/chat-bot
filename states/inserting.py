from aiogram.dispatcher.filters.state import StatesGroup, State


class TryingCatch(StatesGroup):
    password = State()