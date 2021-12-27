from aiogram import types
from loader import dp
from aiogram.dispatcher import filters


# IsReplyFilter
# @dp.message_handler(filters.Command("user_id"), filters.IsReplyFilter)
@dp.message_handler(commands='user_id', is_reply=True)
async def reply_filter_example(msg: types.Message):
    await msg.answer(msg.reply_to_message.from_user.id)


# IsSenderContact
# @dp.message_handler(filters.IsSenderContact(True), content_types='contact')
@dp.message_handler(content_types='contact', is_sender_contact=True)
async def sender_contact_example(msg: types.Message):
    await msg.answer("Rahmat, kontaktingiz qabul qilindi!")


# ForwardMessageFilter
@dp.message_handler(is_forwarded=True)
async def admin_handler_example(msg: types.Message):
    await msg.answer("Birovning xabarini menga jo'natyabsizmi 🙄")


# ChatTypeFilter
@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands="shaxsiy")
# @dp.message_handler(commands='shaxsiy', chat_type="private")
async def chat_type_example(msg: types.Message):
    await msg.answer("Bu shaxsiy chat")