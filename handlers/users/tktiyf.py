from aiogram import types
from loader import dp, bot
from keyboards.default import keyboards as kb
from keyboards.inline import inline_keyboard as ikb
# from utils.db_api.schedule import schedule as sche

@dp.message_handler()
async def bot_navbar(message: types.Message):
    mess = message.text
    if mess == "📞 Biz bilan bog'lanish":
        photo = "AgACAgIAAxkBAAIEsGJKok5DoLL9ik7I1zmOeSCvAtdjAAKpvTEbPjhQSv_TUBrZKlccAQADAgADeQADIwQ"
        await message.answer_photo(photo,
                                   caption='''🏢 Toshkent kimyo-texnologiya instituti Yangiyer filiali
📧 Email: tktiyf_info@mail.ru
☎️ Tel: +998955115856


🙋🏻‍♂️ Taklif va shikoyatlaringiz bo'lsa, @Otajon_Olimbaev ga murojat qiling.''', reply_markup=ikb.aboutMenu)

    elif mess == "🏢Manzil":
        photo = "AgACAgIAAxkBAAIFgGJL2TLeZEmzgy1RNo0eVqQDtB93AAI2uDEbNtdgSm3MOEPvJhQuAQADAgADeAADIwQ"
        await message.answer_photo(photo, caption='''📍 Sirdaryo viloyati Yangiyer shahri Ma'rifat mahallasi Tinchlik ko'chasi 1-uy\n
📍Google xaritadan ham ko'rishingiz mumkin👇''', reply_markup=ikb.mapMenu)
#         await bot.send_message(message.from_user.id, '''📍 Sirdaryo viloyati Yangiyer shahri Ma'rifat mahallasi Tinchlik ko'chasi 1-uy\n
# 📍Google xaritadan ham ko'rishingiz mumkin👇''', reply_markup=ikb.mapMenu)

    elif mess == "🎯 Dars jadvallari":
        await bot.send_message(message.from_user.id, "Kursingizni tanlang!", reply_markup=kb.coursesMenu)
    elif mess == "💰Hisob raqam":
        photo = "AgACAgIAAxkBAAIlEmJObmG0qSE7LaEe_8pNrisxtRBWAAIeujEbTAdxSut30uRwEiy7AQADAgADbQADIwQ"
        await message.answer_photo(photo, caption="🏢 Toshkent kimyo-texnologiya instituti Yangiyer filiali hisob raqami: \n"
                                                     "💳 400910860244137094100079001\n"
                                                     "📞 Tel: +998993248008")
    elif mess == "🎓Kirish ballari":
        photo = "AgACAgIAAxkBAAIFgGJL2TLeZEmzgy1RNo0eVqQDtB93AAI2uDEbNtdgSm3MOEPvJhQuAQADAgADeAADIwQ"
        await message.answer_photo(photo, caption="🏢 TOSHKENT KIMYO-TEXNOLOGIYA INSTITUTI YANGIYER FILIALI\n"
                                                    "Qabul kvotalari va kirish ballari", reply_markup=ikb.engrade)




        #   ---- Courses ----
    elif mess == "1-kurs":
        await bot.send_message(message.from_user.id, "Guruhingizni tanlang", reply_markup=kb.groupMenu1)
    elif mess == "2-kurs":
        await bot.send_message(message.from_user.id, "Guruhingizni tanlang", reply_markup=kb.groupMenu2)
    elif mess == "3-kurs":
        await bot.send_message(message.from_user.id, "Guruhingizni tanlang", reply_markup=kb.groupMenu3)
    elif mess == "🏠 Menyu":
        await bot.send_message(message.from_user.id, "🏠 Menu", reply_markup=kb.mainMenu)
    elif mess == "⬅️Orqaga":
        await bot.send_message(message.from_user.id, "Orqaga", reply_markup=kb.mainMenu)
    elif mess == "⬅️ Orqaga":
        await bot.send_message(message.from_user.id, "Orqaga", reply_markup=kb.coursesMenu)





                    #--- Groups ---

    elif mess == "👑 7-19 AB" or mess == "5-19 TMJ" or mess == "6-19 TMJ":
        photo = "AgACAgIAAxkBAAIE12JKyNrOqAt0HSgaAspu8v_x0kVwAAJuuDEbPjhYSrmU7zhap0_lAQADAgADeQADIwQ"
        await message.answer_photo(photo)
    #     await bot.send_message(message.from_user.id, "Hafta kunini tanlang", reply_markup=kb.weekMenu)
    # elif mess == "🔥Dushanba" or mess == "⭐️Seshanba" or mess == "🕊Chorshanba" or mess == "🌿Payshanba" or mess == "☀️Juma" or mess == "🌈Shanba":
    #     await bot.send_message(message.from_user.id, sche['7-19'][message.text.lower()])

    elif mess == "1-19 NMKT" or mess == "2-19 NMKT" or mess == "3-19 QMKT" or mess == "4-19 QMKT":
        photo = "AgACAgIAAxkBAAIE3mJKyXPbfkBDTIPtbbjvM-yQyv2CAAJvuDEbPjhYSmPc1Pc38-4LAQADAgADeQADIwQ"
        await message.answer_photo(photo)


    #  --- 1-courses ---

    elif mess == "1,2,3-21 NMKT":
        photo = "AgACAgIAAxkBAAIE_WJKzGC9hneZpY-Hyv0-ELW1V-K-AAJquDEbPjhYSmkMwTuvUuRIAQADAgADeQADIwQ"
        await message.answer_photo(photo)
    elif mess == "1,2,3,4-21 QMKT":
        photo = "AgACAgIAAxkBAAIE-2JKzF-7LCEqD9ZfuuWJvpQ63Do2AAJzuDEbPjhYSvHYj8FaVMlAAQADAgADeQADIwQ"
        await message.answer_photo(photo)
    elif mess == "1,2,3-21 TMJ":
        photo = "AgACAgIAAxkBAAIFAWJKzJ3pWuhaPNX7TlUbtYhh8efPAAJ2uDEbPjhYSs7b_KKR--ScAQADAgADeQADIwQ"
        await message.answer_photo(photo)
    elif mess == "1,2-21 AB":
        photo = "AgACAgIAAxkBAAIFA2JKzKH4K6V3MjiJhXS82FXCfb2CAAJ3uDEbPjhYSgP0tbVonPRkAQADAgADeQADIwQ"
        await message.answer_photo(photo)
    elif mess == "1,2-21 KT":
        photo = "AgACAgIAAxkBAAIFA2JKzKH4K6V3MjiJhXS82FXCfb2CAAJ3uDEbPjhYSgP0tbVonPRkAQADAgADeQADIwQ"
        await message.answer_photo(photo)
    elif mess == "1,2,3-21 OOT":
        photo = "AgACAgIAAxkBAAIFBWJKzNiVRE6tpuSw5WDssm1ZH-K_AAJ4uDEbPjhYSvXRZ8QAAZQ1jQEAAwIAA3kAAyME"
        await message.answer_photo(photo)
    elif mess == "4R-21":
        photo = "AgACAgIAAxkBAAIE_2JKzJwn1ORoB3XRRYmXvC6NfxjKAAJ1uDEbPjhYSkXMBoEfeox-AQADAgADeQADIwQ"
        await message.answer_photo(photo)

        #  --- 2-courses ---

    elif mess == "1,2,4,5-20":
        photo = "AgACAgIAAxkBAAIFK2JK3O6Y3VdipkwnStWjxLJcuT8SAAK8uDEbPjhYSswKzU1_8eAEAQADAgADeQADIwQ"
        await message.answer_photo(photo)
    elif mess == "7,8,9-20":
        photo = "AgACAgIAAxkBAAIFLWJK3O8dCkXhWERAD8l1pxM0t4a3AAK9uDEbPjhYSr5A_v1KdMsFAQADAgADeQADIwQ"
        await message.answer_photo(photo)
    elif mess == "14,15-20":
        photo = "AgACAgIAAxkBAAIFL2JK3PGqYX2PEc6nsFMvDKDyiL6ZAAK-uDEbPjhYShw06EwIxW7iAQADAgADeQADIwQ"
        await message.answer_photo(photo)
    elif mess == "21,22-20":
        photo = "AgACAgIAAxkBAAIFL2JK3PGqYX2PEc6nsFMvDKDyiL6ZAAK-uDEbPjhYShw06EwIxW7iAQADAgADeQADIwQ"
        await message.answer_photo(photo)
    elif mess == "17,18,19-20":
        photo = "AgACAgIAAxkBAAIFMWJK3U4PYCvm_xuCkH6WYpaQyTUCAAK_uDEbPjhYSr5j6aphb4zLAQADAgADeQADIwQ"
        await message.answer_photo(photo)
    elif mess == "11R,12R-20":
        photo = "AgACAgIAAxkBAAIFM2JK3VIVQ6NYFMOC8UF4oC7nmmJzAALAuDEbPjhYSkLEPHCdvCrCAQADAgADeQADIwQ"
        await message.answer_photo(photo)
    elif mess == "13R,24R-20":
        photo = "AgACAgIAAxkBAAIFM2JK3VIVQ6NYFMOC8UF4oC7nmmJzAALAuDEbPjhYSkLEPHCdvCrCAQADAgADeQADIwQ"
        await message.answer_photo(photo)



    else:
        await bot.send_message(message.from_user.id, "To'g'ri ma'lumot kiriting...")