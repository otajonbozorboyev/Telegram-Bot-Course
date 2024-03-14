from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from keyboards.inline.buy_book import book_keys
from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command('kitob'))
async def send_book(message: types.Message):
    photo_id = "AgACAgIAAxkBAAIBR2W8lnJxmgRtg5UbqmZIEZAX4-WoAALcxjEbxjTBSlO-p-VoyybZAQADAgADeQADNAQ"
    msg = "<b>The Art of Computer Programming</b> kitobi.\n"
    msg += "Narxi: $ 260\n\n"   
    msg += "<b>Kitob quyidagi joylarda sotiladi:</b>\n👉🏼 Hilol Nashr\n👉🏼 Amazon company\n👉🏼 Asaxiy books"
    await message.reply_photo(photo_id, caption=msg, reply_markup=book_keys)

    # photo_id = "AgACAgIAAxkBAAIBR2W8lnJxmgRtg5UbqmZIEZAX4-WoAALcxjEbxjTBSlO-p-VoyybZAQADAgADeQADNAQ"
    # await message.reply_photo(photo_id, caption="The Art of Computer Programming. \nNarxi: $ 260", reply_markup=book_keys)

    # photo_file = InputFile(path_or_bytesio="photos/book.jpeg")
    # await message.reply_photo(photo_file, caption="The Art of Computer Programming. \nNarxi: $ 260")

    # photo_url = "https://i.imgur.com/HCiYwQ0.jpeg"
    # await message.reply_photo(photo_file, caption="The Art of Computer Programming. \nNarxi: $ 260")
    # await message.answer_photo(photo_id, caption="The Art of Computer Programming. \nNarxi: $ 260")
    # await bot.send_photo(chat_id=message.from_user.id, photo=photo_url,
                            #  caption="The Art of Computer Programming. \nNarxi: $ 260")


@dp.message_handler(Command('kurslar'))
async def send_courses(message: types.Message):
    album = types.MediaGroup()
    photo1 = "https://uproger.com/wp-content/uploads/2021/11/163292-programmist_na_python-piton-algoritmicheskij_yazyk-stoyanie-integrirovannaya_sreda_razrabotki-3840x2160-1.png"
    photo2 = "https://i.imgur.com/HCiYwQ0.jpeg"
    photo3 = InputFile(path_or_bytesio="photos/book.jpeg")
    photo4 = InputFile(path_or_bytesio="photos/blackhole.png")
    video1 = "BAACAgQAAxkBAAIBYmW881EE7tOMYhRzWfySGjka_5GjAAIpBQAC1UykUO_TorZ3d3DnNAQ"
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)
    album.attach_photo(photo=photo4)
    album.attach_video(video=video1, caption="Bizning online kurslarimiz.")
    await message.reply_media_group(media=album)
