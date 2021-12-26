from aiogram import types
from loader import dp, bot


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg: types.Message):
    await msg.answer("Bu nima rasm?")


@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def sticker_handler(msg: types.Message):
    await msg.answer("Bu qanaqa stiker bo'ldi 😆")


@dp.message_handler(content_types=types.ContentTypes.ANIMATION)
async def sticker_handler(msg: types.Message):
    await msg.answer("Gif zo'r ekanu a 😆")


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_handler(msg: types.Message):
    await msg.answer("Bu kimni nomeri? Tushunmadim 🤔")


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def document_handler(msg: types.Message):
    await msg.answer("Men endi buni qanday ochib ko'raman 😂")


@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def audio_handler(msg: types.Message):
    await msg.answer("Cho'tkisidan yo'mi 😁")


@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def voice_handler(msg: types.Message):
    await msg.answer("Yaxshi eshitolmadim 🙄")


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def location_handler(msg: types.Message):
    await msg.answer("Iya lokatsiyami 😆")


@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def video_handler(msg: types.Message):
    await msg.answer("Ooo video uchun rahmat 😁")



@dp.message_handler(content_types=types.ContentTypes.ANY)
async def sticker_handler(msg: types.Message):
    await msg.answer("Bu nima? 🙄")