from aiogram.types import Message, CallbackQuery
from loader import dp, bot

@dp.callback_query_handler(text="course:data")
async def data_course_info(call: CallbackQuery):
    msg = "Ushbu darsimizda siz ma'lumotlar tuzilmasi bilan mukammal darajada oʻrganasiz.\n\n"
    msg += "Darsimiz quyidagi mavzularni oʻz ichiga oladi:\n"
    msg += "✅ O'zgaruvchilar bilan tanishib, ular bilan ishlay olish\n"
    msg += "✅ Dasturiy funksiyalar tuzish\n"
    msg += "✅ Dastur logikasi\n"
    msg += "✅ Tekshirish operatorlaridan foydalanish\n"
    msg += "✅ Turli algoritmlardan foydalanish\n"
    msg += "✅ Foydali linklar\n"
    await bot.send_message(chat_id=call.from_user.id, text=msg)
    # await call.answer(msg)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="course:java")
async def data_course_info(call: CallbackQuery):
    msg = "Ushbu darsimizda siz Java dasturlash tilini mukammal darajada oʻrganasiz.\n\n"
    msg += "Darsimiz quyidagi mavzularni oʻz ichiga oladi:\n"
    msg += "✅ O'zgaruvchilar bilan tanishib, ular bilan ishlay olish\n"
    msg += "✅ Dasturiy funksiyalar tuzish\n"
    msg += "✅ Dastur logikasi\n"
    msg += "✅ Tekshirish operatorlaridan foydalanish\n"
    msg += "✅ Turli algoritmlardan foydalanish\n"
    msg += "✅ Foydali linklar\n"
    await bot.send_message(chat_id=call.from_user.id, text=msg)
    # await call.answer(msg)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="course:django")
async def data_course_info(call: CallbackQuery):
    msg = "Ushbu darsimizda siz Django frameworki bilan mukammal darajada oʻrganasiz.\n\n"
    msg += "Darsimiz quyidagi mavzularni oʻz ichiga oladi:\n"
    msg += "✅ Django bilan tanishish\n"
    msg += "✅ Environment yaratish\n"
    msg += "✅ Dastur logikasi\n"
    msg += "✅ Application yaratish\n"
    msg += "✅ Turli algoritmlardan foydalanish\n"
    msg += "✅ Foydali linklar\n"
    await bot.send_message(chat_id=call.from_user.id, text=msg)
    # await call.answer(msg)
    await call.answer(cache_time=60)

