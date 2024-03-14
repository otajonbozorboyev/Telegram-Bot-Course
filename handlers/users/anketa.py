from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import PersonalData

@dp.message_handler(Command("anketa"))
async def enter_test(message: types.Message):
    await message.answer("To'liq ismingizni kiriting")
    await PersonalData.fullname.set()


@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    # await state.update_data(name = fullname)
    await state.update_data(
        {'name': fullname}
        )

    await message.answer("Elektron pochta manzilingizni kiriting")
    await PersonalData.next()
    # await PersonalData.email.set()


@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text

    # await state.update_data(email = email)
    await state.update_data(
        {'email': email}
        )

    await message.answer('Telefon raqamingizni kiriting')

    await PersonalData.next()


@dp.message_handler(state=PersonalData.phoneNumber)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text

    # await state.update_data(phone = phone)
    await state.update_data(
        {'phone': phone}
        )
    

    # Ma'lumotlarni qayta o'qiymiz:
    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    msg = "Quyidagi ma'lumotlarni qabul qilindi:\n"
    msg += f"Ismingiz - {name}\n"
    msg += f"Pochta manzilingiz - {email}\n"
    msg += f"Phone - {phone}"   
    await message.answer(msg)

    await state.finish()
    # await state.reset_state(with_data = False)
