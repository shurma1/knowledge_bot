from bot import dp
from aiogram import types, executor
from handler.answer_handler import answer_handler

@dp.message_handler()
async def any_text_message(message: types.Message):
    await answer_handler(message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)