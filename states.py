from aiogram.fsm.state import State, StatesGroup


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
