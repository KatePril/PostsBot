from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from aiogram.enums import ParseMode

from states.PostState import PostForm

from keyboards.reply_keyboards.cancel_keyboard import get_cancel_keyboard
from keyboards.reply_keyboards.main_keyboard import get_main_keyboard
from keyboards.reply_keyboards.final_keyboard import get_final_keyboard

from keyboards.inline_keyboards.time_keyboard import get_time_keyboard
from keyboards.inline_keyboards.date_keyboard import get_date_keyboard
from keyboards.inline_keyboards.image_keyboard import get_image_keyboard

state_router = Router()


@state_router.message(F.text == "Cancel post creation")
async def stop_post_creation(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("post creation cancelled", reply_markup=get_main_keyboard())


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


@state_router.callback_query(F.data == 'time_value')
async def process_time(callback: CallbackQuery, state: FSMContext):
    await state.update_data(time=callback.message.date.time())
    await state.set_state(PostForm.date)
    await callback.message.answer("Send current date using the button below", reply_markup=get_date_keyboard())


@state_router.callback_query(F.data == 'date_value')
async def progress_date(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date=str(callback.message.date.date()).replace("-", "\-"))
    await state.set_state(PostForm.image)
    await callback.message.answer("Send an image you want to add to the post or press the button below to skip this "
                                  "step", reply_markup=get_image_keyboard())


@state_router.callback_query(F.data == 'skip_image')
async def skip_image(callback: CallbackQuery, state: FSMContext):
    await final_reply(message=callback.message, data=await state.get_data())
    await state.clear()


@state_router.message(PostForm.image)
async def progress_image(message: Message, state: FSMContext):
    await state.update_data(image=message.photo[0].file_id)
    await final_reply(message=message, data=await state.get_data())
    await state.clear()


def create_post(data):
    output = (f"*_name:_* {data['name']}\n"
              f"*_description:_* {data['description']}\n"
              f"*_time:_* {data['time']}\n"
              f"*_date:_* {data['date']}\n")
    return output


async def final_reply(message: Message, data: dict):
    if 'image' in data.keys():
        await message.answer_photo(photo=data['image'], caption=create_post(data),
                                   parse_mode=ParseMode.MARKDOWN_V2, reply_markup=get_final_keyboard())
    else:
        await message.answer(text=create_post(data), parse_mode=ParseMode.MARKDOWN_V2,
                             reply_markup=get_final_keyboard())


@state_router.message(F.text == "Create post")
async def post_created(message: Message):
    await message.answer("Post created successfully", reply_markup=get_main_keyboard())


@state_router.message(F.text == "Fill the form again")
async def fill_again(message: Message, state: FSMContext):
    await state.set_state(PostForm.name)
    await message.answer("Enter the name of the post:", reply_markup=ReplyKeyboardRemove())
