from aiogram import types
from ai_model.init import knowledge
from bot import bot
from config import DOCS_FOLDER_PATH

async def question_callback_handler(callback: types.CallbackQuery):
    question_id = callback.data.split("#")[1]

    question = knowledge.get_question_by_id(int(question_id))
    answer = knowledge.get_answer_by_id(int(question_id))

    answer_text = answer["text"]
    message_text = f"<b>{question}</b>\n\n{answer_text}"

    await bot.send_message(callback.from_user.id, message_text)

    if answer.get('file_name'):
        with open(DOCS_FOLDER_PATH + answer['file_name'], 'rb') as file:
            await bot.send_document(callback.from_user.id, file)
