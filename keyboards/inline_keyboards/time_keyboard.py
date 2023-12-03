from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def get_time_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Send time", callback_data="time_value"))
    return builder.as_markup()
