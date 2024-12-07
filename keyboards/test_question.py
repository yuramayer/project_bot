from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_yesno_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='ага 😎')
    kb.button(text='bruh 😮‍💨')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
