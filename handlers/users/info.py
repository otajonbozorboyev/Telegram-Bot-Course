from aiogram import types

from loader import dp

from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hstrikethrough, hlink

@dp.message_handler(commands='info')
async def bot_info(message: types.Message):
    text = f"Assalomu alykum {message.from_user.full_name}\n"
    text += "Bu" + hbold('qalin matn.\n')
    text += "Bu" + hitalic('egri matn.\n')
    text += "Bu" + hunderline('ostiga chizilgan matn.\n')
    text += "Bu" + hstrikethrough("o'chirilgan matn.\n")
    text += "Bu" + hlink("Python dasturlash kursiga link\n", "https://www.youtube.com/watch?v=_uQrJ0TkZlc")
    text += "Bu" + hcode('print("Hello World!")') + "kod\n"
    await message.answer(text)

@dp.message_handler(commands='info_html')
async def bot_info(message: types.Message):
    text = f"Assalomu alaykum {message.from_user.full_name}!\n"
    text += "Bu <b>qalin matn.</b>\n"
    text += "Bu <i>egri matn.</i>\n"
    text += "Bu <u>ostiga chizilgan matn.</u>\n"
    text += "Bu <s>o'chirilgan matn.</s>\n"
    text += "Bu <a href='https://www.youtube.com/watch?v=ydYBRLoBUpY'>Python beginner kursiga link</a>.\n"
    text += "Bu <code>print('Hello World!')</code> kod.\n"

    # text = ("Buyruqlar: ",
    #         "/start - Botni ishga tushirish",
    #         "/help - Yordam")

    await message.answer(text)


@dp.message_handler(commands='info_markdown')
async def bot_info(message: types.Message):
    text = f"Assalomu alaykum {message.from_user.full_name}\!\n"
    text += "Bu *qalin matn\.*\n"
    text += "Bu _egrimatn_\n"
    text += "Bu __ostiga chizilgan matn__\n"
    text += "Bu ~o'chirilgan matn~\n"
    text += "Bu [Python beginner kursiga link](https://www.youtube.com/watch?v=_uQrJ0TkZlc)\n"
    text += "Bu `print('Hello world!')` kod\n"

    await message.answer(text, parse_mode=types.ParseMode.MARKDOWN_V2)