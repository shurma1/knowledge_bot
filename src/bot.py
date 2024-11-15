import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN

from handler.main import answer_handler

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def any_text_message(message: types.Message):
    await answer_handler(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)