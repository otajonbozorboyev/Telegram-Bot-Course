# Ushbu regex haqida yana ham bilmoqchi bo'lsakquyidagi sayt qorqali bilib olishimiz mumkin:
# https://ihateregex.io/

from aiogram import types
from aiogram.dispatcher.filters import Regexp
from loader import dp

EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
COMMAND_EMAIL_REGEX = r'/email:' + EMAIL_REGEX

@dp.message_handler(Regexp(EMAIL_REGEX))
async def regexp_email(msg: types.Message):
    await msg.answer('Email qabul qilindi')

@dp.message_handler(Regexp(PHONE_NUM))
async def regex_phone(msg: types.Message):
    await msg.answer('Telefon raqam qabul qilindi')
