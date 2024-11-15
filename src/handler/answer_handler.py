from aiogram import types
from ai_model.init import knowledge
from config import DOCS_FOLDER_PATH
from bot import bot

async def answer_handler(message: types.Message):
    await bot.send_chat_action(message.from_user.id, action="typing")

    try:
        answer = knowledge.get_answer(message.text)

        await message.answer(answer['text'])
        if answer.get('file_name'):
            with open(DOCS_FOLDER_PATH + answer['file_name'], 'rb') as file:
                await bot.send_document(message.chat.id, file)
    except:
        await message.answer('12')