from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

SUPERUSERS = [303493441, 838538802, 1002098477]
BLACKLIST = [615371773, 6521170345]

# @dp.message_handler(filters.IDFilter(chat_id=SUPERUSERS))
@dp.message_handler(chat_id=SUPERUSERS, text='secret')
# @dp.message_handler(chat_id='303493441', text='start')
async def id_filter_example(msg: types.Message):
    await msg.answer('Xush kelibsiz, SuperUSER!')