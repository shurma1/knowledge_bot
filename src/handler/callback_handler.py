from aiogram import types
from handler.question_callback_handler import question_callback_handler

async def callback_handler(callback: types.CallbackQuery):
    callback_type = callback.data.split("#")[0]

    if callback_type == "question":
        await question_callback_handler(callback)
