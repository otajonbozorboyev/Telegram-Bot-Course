from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

@dp.message_handler(content_types='photo')
@dp.message_handler(content_types='document')
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg: types.Message):
    await msg.answer('Bu nima ?')

@dp.message_handler(content_types='sticker')
# @dp.message_handler(content_types=types.ContentTypes.STICKER)
async def emoji_handler(msg: types.Message):
    await msg.answer('Bu sticker!')


@dp.message_handler(content_types='contact')
# @dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_handler(msg: types.Message):
    await msg.answer('Kim bu ?')

@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def audio_handler(msg: types.Message):
    await msg.answer('Bu audio')