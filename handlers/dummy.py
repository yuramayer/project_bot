from aiogram import Router, F
from aiogram.types import Message

dummy_router = Router()

@dummy_router.message(F.text)
async def text_dummy(message: Message):
    await message.answer('Нажми на команды /start или /test 😉')


@dummy_router.message(F.sticker)
async def sticker_dummy(message: Message):
    await message.answer('Классный стикер!\n\nНажми на команды /start или /test 😉')
