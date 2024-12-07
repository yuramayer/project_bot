from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('По команде <b>/start</b> работает функция cmd_start')
    await message.answer('Отправь команду <b>/test</b> чтобы затестить клавиатуру')



