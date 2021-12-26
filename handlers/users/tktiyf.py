from aiogram import types
from aiogram import Bot, Dispatcher, executor, types
from loader import dp, bot
from keyboards.default import keyboards as kb


@dp.message_handler()
async def bot_navbar(message: types.Message):
    mess = message.text
    if mess == "📞 Biz bilan bog'lanish":
        await bot.send_message(message.from_user.id, '''🏢 Toshkent kimyo-texnologiya instituti Yangiyer filiali
📧 Email: tktiyf_info@mail.ru
☎️ Tel: +998955115856


🙋🏻‍♂️ Taklif va shikoyatlaringiz bo'lsa, @Otajon_Olimbaev ga murojat qiling.''')
    elif mess == "🏢Manzil":
        await bot.send_message(message.from_user.id, "📍 Sirdaryo viloyati Yangiyer shahri Ma'rifat mahallasi Tinchlik ko'chasi 1-uy\n"
                                                     "📍Google xaritadan ham ko'rishingiz mumkin👇")
        await bot.send_message(message.from_user.id, "https://goo.gl/maps/NfCWtdacCBZck5B97")
    elif mess == "🎯 Dars jadvallari":
        await bot.send_message(message.from_user.id, "Kursingizni tanlang!", reply_markup=kb.coursesMenu)
    elif mess == "💰Hisob raqam":
        await bot.send_message(message.from_user.id, "🏢 Toshkent kimyo-texnologiya instituti Yangiyer filiali hisob raqami: \n"
                                                     "💳 400910860244137094100079001\n"
                                                     "📞 Tel: +998993248008")
    elif mess == "1-kurs":
        await bot.send_message(message.from_user.id, "Hali ma'lumot kiritilmagan 😅")
    elif mess == "2-kurs":
        await bot.send_message(message.from_user.id, "Hali ma'lumot kiritilmagan 😅")
    elif mess == "3-kurs":
        await bot.send_message(message.from_user.id, "Guruhingizni tanlang", reply_markup=kb.groupMenu)
    elif mess == "🏠 Menyu":
        await bot.send_message(message.from_user.id, "🏠 Menu", reply_markup=kb.mainMenu)
    elif mess == "⬅️Orqaga":
        await bot.send_message(message.from_user.id, "Orqaga", reply_markup=kb.mainMenu)
    elif mess == "⬅️ Orqaga":
        await bot.send_message(message.from_user.id, "Orqaga", reply_markup=kb.coursesMenu)
    elif mess == "⬅️  Orqaga":
        await bot.send_message(message.from_user.id, "Orqaga", reply_markup=kb.groupMenu)




                    #--- Courses ---

    # elif mess == "👑 7-19 AB":
    #     await bot.send_message(message.from_user.id, "Hafta kunini tanlang", reply_markup=kb.weekMenu)
    # elif mess == "🔥Dushanba" or mess == "⭐️Seshanba" or mess == "🕊Chorshanba" or mess == "🌿Payshanba" or mess == "☀️Juma" or mess == "🌈Shanba":
    #     await bot.send_message(message.from_user.id, sche['7-19'][message.text.lower()])
    #
    # elif mess == "1-19 NMKT":
    #     await bot.send_message(message.from_user.id, "Hafta kunini tanlang", reply_markup=kb.weekMenu1_19)
    # elif mess == "🟠Dushanba" or mess == "🟡Seshanba" or mess == "🟢Chorshanba" or mess == "🔵Payshanba" or mess == "⚪️Juma" or mess == "🔴Shanba":
    #     await bot.send_message(message.from_user.id, sche['1-19'][message.text.lower()])
    #
    # elif mess == "2-19 NMKT":
    #     await bot.send_message(message.from_user.id, "Hafta kunini tanlang", reply_markup=kb.weekMenu2_19)
    # elif mess == "🟡Dushanba" or mess == "🟢Seshanba" or mess == "🔵Chorshanba" or mess == "⚪️Payshanba" or mess == "🔴Juma" or mess == "🟠Shanba":
    #     await bot.send_message(message.from_user.id, sche['2-19'][message.text.lower()])
    #
    # elif mess == "3-19 QMKT":
    #     await bot.send_message(message.from_user.id, "Hafta kunini tanlang", reply_markup=kb.weekMenu3_19)
    # elif mess == "🟢Dushanba" or mess == "🔵Seshanba" or mess == "⚪️Chorshanba" or mess == "🔴Payshanba" or mess == "🟠Juma" or mess == "🟡Shanba":
    #     await bot.send_message(message.from_user.id, sche['3-19'][message.text.lower()])
    #
    # elif mess == "4-19 QMKT":
    #     await bot.send_message(message.from_user.id, "Hafta kunini tanlang", reply_markup=kb.weekMenu4_19)
    # elif mess == "🔵Dushanba" or mess == "⚪️Seshanba" or mess == "🔴Chorshanba" or mess == "🟠Payshanba" or mess == "🟡Juma" or mess == "🟢Shanba":
    #     await bot.send_message(message.from_user.id, sche['4-19'][message.text.lower()])
    #
    # elif mess == "5-19 TMJ":
    #     await bot.send_message(message.from_user.id, "Hafta kunini tanlang", reply_markup=kb.weekMenu5_19)
    # elif mess == "⚪️Dushanba" or mess == "🔴Seshanba" or mess == "🟠Chorshanba" or mess == "🟡Payshanba" or mess == "🟢Juma" or mess == "🔵Shanba":
    #     await bot.send_message(message.from_user.id, sche['5-19'][message.text.lower()])
    #
    # elif mess == "6-19 TMJ":
    #     await bot.send_message(message.from_user.id, "Hafta kunini tanlang", reply_markup=kb.weekMenu6_19)
    # elif mess == "🔴Dushanba" or mess == "🟠Seshanba" or mess == "🟡Chorshanba" or mess == "🟢Payshanba" or mess == "🔵Juma" or message.text == "⚪️Shanba":
    #     await bot.send_message(message.from_user.id, sche['6-19'][message.text.lower()])

    else:
        await bot.send_message(message.from_user.id, "Iltimos tayyor tugmalardan foydalaning!")