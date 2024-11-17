from aiogram import types
from config import TEXT_FOR_QUESTIONS_COMMAND
from ai_model.init import knowledge

async def questions_command_handler(message: types.Message):
    questions = knowledge.get_knowledge_questions(only_first_question=True)
    await message.answer(TEXT_FOR_QUESTIONS_COMMAND + "\n\n- " + "\n- ".join(questions))