from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def get_cancel_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Cancel post creation"))
    return builder.as_markup(resize_keyboard=True)
