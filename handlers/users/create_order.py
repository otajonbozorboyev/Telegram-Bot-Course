# Card_number: 4242 4424 2424 2422
# Data: 03 30
# Password: 950

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from data.config import ADMINS

from loader import dp, bot
from data.products import programming_book, ds_praktikum, FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING
from keyboards.inline.product_keys import build_keyboard


@dp.message_handler(Command("kitob"))
async def show_invoices(message: types.Message):
    caption = "<b>The Art of Computer Programming</b> kitobi\n\n"
    caption += "Ushbu kitob Donald Knut tomonidan yozilgan bo'lib anchayin kuchli va foydali kitob deb topilgan.\n"
    caption += "Qo'lingizdagi kitobning o'ziga xos jihati shundaki, uni tavsiya qilgan juda ko'p katta muhandis va tadbirkorlar bor.\n"
    caption += "Jumladan Bill Gates \"Agar ushbu kitobni o'qib va tushuna olgan muhandisning Resumesini shaxsan o'zim ko'rib chiqishga tayyorman\" deb ta'kidlab o'tgan.\n" 
    caption += "Ushbu kitobni hozirda O'zbekistondan topishingiz anchayin qiyin. Uni Amazon online do'konidan buyurtma bersangiz bo'ladi.\n"
    caption += "Narxi: <b>260 $</b>"
    await message.answer_photo(photo="http://pioneer.chula.ac.th/~skrung/main/images/l03_algorithm.png",
                               caption=caption, reply_markup=build_keyboard("book"))


@dp.message_handler(Command("praktikum"))
async def show_invoices(message: types.Message):
    caption = "<b>Data Science va Sun'iy Intellekt</b> praktikum.\n\n"
    caption += "Kurs tarkibi:\n"
    caption += "✅ Python Dasturlash Asoslari\n"
    caption += "✅ Data Sciencega kirish va DS metodologiyasi\n"
    caption += "✅ Maʻlumotlar tahlili (Data Analysis)\n"
    caption += "✅ Maʻlumotlarga ishlov berish\n"
    caption += "✅ Vizualizasiya\n"
    caption += "✅ Machine Learning\n"
    caption += "✅ Deep Learning\n"
    caption += "✅ Natural Language Processing\n\n"
    caption += "Narxi: <b>150 $</b>"

    await message.answer_photo(photo="https://i.pinimg.com/originals/f6/be/63/f6be6309b6ac1a630978ac14431fe5ec.jpg",
                               caption=caption, reply_markup=build_keyboard("praktikum"))


@dp.message_handler(Command('mahsulotlar'))
async def book_invoice(message: Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **programming_book.generate_invoice(),
                           payload="123456")
    await bot.send_invoice(chat_id=message.from_user.id,
                           **ds_praktikum.generate_invoice(),
                           payload="123457")


@dp.callback_query_handler(text="product:book")
async def book_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **programming_book.generate_invoice(),
                           payload="payload:kitob")
    await call.answer()


@dp.callback_query_handler(text="product:praktikum")
async def praktikum_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **ds_praktikum.generate_invoice(),
                           payload="payload:praktikum")
    await call.answer()


@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Chet elga yetkazib bera olmaymiz")
    elif query.shipping_address.city.lower() == 'tashkent' or query.shipping_address.city.lower() == 'toshkent':
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[REGULAR_SHIPPING],
                                        ok=True)


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Xaridingiz uchun tashakkur!")
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"Ushbu mahsulot sotildi: {pre_checkout_query.invoice_payload}\n"
                                f"ID: {pre_checkout_query.id}\n"
                                f"Telegram user: {pre_checkout_query.from_user.first_name}\n"
                                f"Xaridor: {pre_checkout_query.order_info.name}, tel: {pre_checkout_query.order_info.phone_number}")
