from aiogram import types
from aiogram.dispatcher import filters

from keyboards.default import keyboards as kb
from loader import dp


SUPERUSERS = [896560538]
BLACKLIST = []


# @dp.message_handler(filters.IDFilter(chat_id=SUPERUSERS))
@dp.message_handler(chat_id=SUPERUSERS, commands="start")
async def id_filter(msg: types.Message):
    await msg.answer("Xush kelibsiz! SUPERUSER 🙃", reply_markup=kb.mainMenu)
