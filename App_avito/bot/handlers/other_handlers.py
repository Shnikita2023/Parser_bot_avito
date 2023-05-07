from aiogram import Router
from aiogram.types import Message
from bot.lexicon import LEXICON_RU

router: Router = Router()


# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message) -> None:
    await message.answer(text=LEXICON_RU['other_answer'])
