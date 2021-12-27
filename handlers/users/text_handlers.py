from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text


# @dp.message_handler(Text(contains="tentak"), ignore_case=True)
@dp.message_handler(Text(equals='ahmoq', ignore_case=True))
async def regexp_email(msg: types.Message):
    await msg.answer("O'zing ahmoq")


# Boshqa parametrlar
# startswith
# endswith
