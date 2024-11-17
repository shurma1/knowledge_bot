from bot import dp
from aiogram import types, executor
from handler.answer_handler import answer_handler
from handler.questions_command_handler import questions_command_handler
from handler.callback_handler import callback_handler

@dp.message_handler(commands=['questions'])
async def help_command(message: types.Message):
    await questions_command_handler(message)

@dp.message_handler()
async def any_text_message(message: types.Message):
    await answer_handler(message)

@dp.callback_query_handler()
async def process_callback(callback_query: types.CallbackQuery):
    await callback_handler(callback_query)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)