from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.pythonKeyboard import menuPython

from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer("Kurs tanlang", reply_markup=menu)


@dp.message_handler(text='Telegram Bot')
async def send_link(message: Message):
    await message.answer('Telegram bot kursi: https://www.youtube.com/watch?v=vZtm1wuA2yc')

@dp.message_handler(text='Python')
async def send_link(message: Message):
    await message.answer("Mavzu tanlang", reply_markup=menuPython)


@dp.message_handler(text='#00 Kirish')
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=_uQrJ0TkZlc", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text='Boshiga')
async def send_link(message: Message):
    await message.answer("Kurs tanlang", reply_markup=menu)

