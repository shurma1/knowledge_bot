import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN


# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаем объект бота
bot = Bot(token=API_TOKEN)

# Создаем диспетчер
dp = Dispatcher(bot)


@dp.message_handler()
async def any_text_message(message: types.Message):
    await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)