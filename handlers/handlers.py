from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.reply_keyboards.main_keyboard import get_main_keyboard


router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Now you can create post", reply_markup=get_main_keyboard(True))

