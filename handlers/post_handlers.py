from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove

from states.PostState import PostForm
from keyboards.reply_keyboards.cancel_keyboard import get_cancel_keyboard
from keyboards.reply_keyboards.main_keyboard import get_main_keyboard
from keyboards.inline_keyboards.time_keyboard import get_time_keyboard

from main import dp

state_router = Router()


@state_router.message(F.text == "Cancel post creation")
async def stop_post_creation(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("post creation cancelled", reply_markup=get_main_keyboard(False))


@state_router.message(F.text == "Create a post")
async def start_post_creation(message: Message, state: FSMContext):
    await state.set_state(PostForm.name)
    await message.answer("Enter the name of the post:", reply_markup=ReplyKeyboardRemove())


@state_router.message(PostForm.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(PostForm.description)
    await message.answer("Provide description of the post", reply_markup=get_cancel_keyboard())


@state_router.message(PostForm.description)
async def process_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(PostForm.time)
    await message.answer("Send current time using the button below", reply_markup=get_time_keyboard())


@dp.callback_query_handler(state=PostForm.time)
async def process_time(callback: CallbackQuery, state: FSMContext):
    print("Here")
    await state.update_data(time=await callback.message.date.time())
    print(await callback.message.date.time())
    await state.set_state(PostForm.date)
    await callback.message.answer("Send current date using the button below")


dp.include_router(state_router)

