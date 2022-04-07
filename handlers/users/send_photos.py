# from aiogram import types
# from aiogram.dispatcher.filters import Command
# from aiogram.types import InputFile
#
# from loader import dp, bot
#
#
# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def get_file_id_p(message: types.Message):
#     await message.reply(message.photo[-1].file_id)
#
#
# @dp.message_handler(content_types=types.ContentType.VIDEO)
# async def get_file_id_v(message: types.Message):
#     await message.reply(message.video.file_id)
#
#
# @dp.message_handler(Command("kitob"))
# async def send_book(message: types.Message):
#     photo_id = "AgACAgIAAxkBAAIDuGJJhurIF7Xa0UdXbEmEfj0L86ZRAAJGuzEbo7hQSq8TDTSVxkfeAQADAgADeQADIwQ"
#     # photo_url = "https://kitoblardunyosi.uz/image/cache/catalog/001-Kitoblar/003_boshqalar/006_ilmiy_ommabop/python-3d-web-500x500h.jpg"
#     # photo_file = InputFile(path_or_bytesio="photos/kitob.jpg")
#     # await message.reply_photo(
#     #     photo_file, caption="Dasturlash asoslari kitobi. \n Narxi: 50000 so'm"
#     # )
#     await message.answer_photo(
#         photo_id, caption="Dasturlash asoslari kitobi. \n Narxi: 50000 so'm"
#     )
#     # await bot.send_photo(
#     #     chat_id=message.from_user.id,
#     #     photo=photo_url,
#     #     caption="Dasturlash asoslari kitobi. \nNarxi: 50000 so'm",
#     # )
#
#                 # --- Rasmlarni albom qilib jo'natish ---
#
# # @dp.message_handler(Command("kurslar"))
# # async def send_courses(message: types.Message):
# #     album = types.MediaGroup()
# #     photo1 = "AgACAgIAAxkBAAIDuGJJhurIF7Xa0UdXbEmEfj0L86ZRAAJGuzEbo7hQSq8TDTSVxkfeAQADAgADeQADIwQ"
# #     photo2 = "https://kitoblardunyosi.uz/image/cache/catalog/001-Kitoblar/003_boshqalar/003_bolalar/uchdan-keyin-kech-web-500x500h.jpg"
# #     photo3 = "https://kitoblardunyosi.uz/image/cache/catalog/001-Kitoblar/003_boshqalar/004_oquv_qullanma/ingliz-oltin-web-500x500h.jpg"
# #     # photo4 = InputFile(path_or_bytesio="photos/algoritm.png")
# #     # video1 = "BAACAgUAAxkBAAIHT2ErOXldS7NxbW9mdL4tsI18ZqlvAALdAgACXltZVVoMJafxpb77IAQ"
# #     album.attach_photo(photo=photo1)
# #     album.attach_photo(photo=photo2)
# #     album.attach_photo(photo=photo3, caption="Bizning online kurslarimiz")
# #     # album.attach_photo(photo=photo4)
# #     # album.attach_video(video=video1)
# #     await message.reply_media_group(media=album)