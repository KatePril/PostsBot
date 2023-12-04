from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def get_final_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Create post"))
    builder.add(KeyboardButton(text="Fill the form again"))
    return builder.as_markup(resize_keyboard=True)
