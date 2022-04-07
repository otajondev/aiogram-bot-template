from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Regexp

# Regex larni iHateRegex.io saytidan olamiz
EMAIL_REGEXP = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
PHONE_NUM = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
COMMAND_EMAIL_REGEXP = r"/email: " + EMAIL_REGEXP


@dp.message_handler(Regexp(EMAIL_REGEXP))
async def regexp_email(msg: types.Message):
    await msg.answer("Email qabul qilindi.")


@dp.message_handler(Regexp(PHONE_NUM))
async def regexp_phone_number(msg: types.Message):
    await msg.answer("Telefon raqam qabul qilindi.")


@dp.message_handler(regexp_commands=[COMMAND_EMAIL_REGEXP])
async def command_regexp_example(msg: types.Message):
    await msg.answer("Email qabul qilindi!")
