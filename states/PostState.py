from aiogram.fsm.state import State, StatesGroup


class PostForm(StatesGroup):
    name = State()
    description = State()
    time = State()
    date = State()
    image = State()