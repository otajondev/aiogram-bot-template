from aiogram import types

from loader import dp


@dp.message_handler(hashtags="money")
@dp.message_handler(cashtags=["eur", "usd"])
async def bot_echo(message: types.Message):
    await message.answer("Yee, Akang kuchaydi 😆")
