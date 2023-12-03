from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def get_final_key_board():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Create post", callback_data="create_post"))
    builder.add(InlineKeyboardButton(text="Fill the form again", callback_data="fill_again"))
    return builder.as_markup()