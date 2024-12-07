from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.test_question import get_yesno_kb

test_router = Router()

@test_router.message(Command('test'))
async def cmd_test(message: Message):
    yes_no_kb = get_yesno_kb()
    await message.answer('Тебе понятно, как работает aiogram?',
                         reply_markup=yes_no_kb)


@test_router.message(F.text.lower() == 'ага 😎')
async def yes_test(message: Message):
    await message.answer('Вот и огонь!',
                         reply_markup=ReplyKeyboardRemove())


@test_router.message(F.text.lower() == 'bruh 😮‍💨')
async def no_test(message: Message):
    await message.answer('Спроси вопрос в беседе!', 
                         reply_markup=ReplyKeyboardRemove())
