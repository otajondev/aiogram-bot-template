from aiogram import types
from loader import dp
from aiogram.dispatcher import filters


# @dp.message_handler(filters.Command("ban_user"), filters.AdminFilter())
@dp.message_handler(commands='ban_user', is_chat_admin=True)
async def admin_handler_example(msg: types.Message):
    await msg.answer("Kimni ban qilamiz?")
