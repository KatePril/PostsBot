from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def get_main_keyboard(is_new):
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Create a post"))
    if not is_new:
        builder.add(KeyboardButton(text="My posts"))
    return builder.as_markup(resize_keyboard=True)
