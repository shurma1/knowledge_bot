from aiogram import types
from ..bot import bot
from ..config import docs_folder_path, default_message


async def answer_handler(message: types.Message):
    await message.answer(message.text)