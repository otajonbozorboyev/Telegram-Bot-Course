from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.main_menu import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer_photo(caption=f"Salom, {message.from_user.full_name}!",
                            photo="https://images.unsplash.com/photo-1534802046520-4f27db7f3ae5?crop=entropy&amp;cs=tinysrgb&amp;fit=max&amp;fm=jpg&amp;ixid=MnwxMTc3M3wwfDF8c2VhcmNofDEwfHxhcHBsZXxlbnwwfHx8fDE2MTcxODM4Nzc&amp;ixlib=rb-1.2.1&amp;q=80&amp;w=2000",
                        reply_markup=menu)
