from aiogram import types
from ai_model.init import knowledge
from config import (DOCS_FOLDER_PATH,
                    MIN_SIMILARITY,
                    MIN_SIMILARITY_FOR_ACCURATE_ANSWER,
                    TEXT_FOR_FREQUENT_QUESTIONS,
                    TEXT_FOR_NOT_FOUND_QUESTION,
                    MAX_ANSWER_OPTIONS)
from bot import bot

async def answer_handler(message: types.Message):
    await bot.send_chat_action(message.from_user.id, action="typing")

    try:
        questions = knowledge.get_similar_questions(message.text)

        if questions[0].probability < MIN_SIMILARITY:
            raise ValueError()

        if questions[0].probability < MIN_SIMILARITY_FOR_ACCURATE_ANSWER:
            keyboard = types.InlineKeyboardMarkup()

            for question in questions[:MAX_ANSWER_OPTIONS]:
                if question.probability < MIN_SIMILARITY:
                    continue
                question_id = knowledge.find_question_id(question.text)
                question_data = knowledge.get_question_data_by_id(question_id)
                question_short = question_data['question_short'] if question_data.get('question_short') else question.text
                button = types.InlineKeyboardButton(text=question_short, callback_data=f"question#{question_id}")
                keyboard.add(button)

            await message.answer(TEXT_FOR_FREQUENT_QUESTIONS, reply_markup=keyboard)
            return

        question_id = knowledge.find_question_id(questions[0].text)

        question = knowledge.get_question_by_id(question_id)
        answer = knowledge.get_answer_by_id(question_id)

        message_text = f"<b>{question}</b>\n\n{answer['text']}"

        await message.answer(message_text)

        if answer.get('file_name'):
            with open(DOCS_FOLDER_PATH + answer['file_name'], 'rb') as file:
                await bot.send_document(message.chat.id, file)

    except Exception as error:
        print(error)
        await message.answer(TEXT_FOR_NOT_FOUND_QUESTION)