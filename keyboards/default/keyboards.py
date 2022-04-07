from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn_main = KeyboardButton("🏠 Menyu")
btn_backMenu = KeyboardButton("⬅️Orqaga")
btn_back = KeyboardButton("⬅️ Orqaga")
#          --- Main menu ---

mainMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🎯 Dars jadvallari"),
            KeyboardButton("💰Hisob raqam"),
        ],
        [
            KeyboardButton("🎓Kirish ballari"),
            KeyboardButton("🏢Manzil"),
        ],
        [
            KeyboardButton("📞 Biz bilan bog'lanish"),
        ],
    ],
    resize_keyboard=True)


#       --- Courses list ---

coursesMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("1-kurs"),
            KeyboardButton("2-kurs"),
            KeyboardButton("3-kurs"),
        ],
        [
            btn_backMenu,
        ],
    ],
    resize_keyboard=True)



#           --- Groups list ---

#           --- 3-courses ---

groupMenu3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("1-19 NMKT"),
            KeyboardButton("2-19 NMKT"),
            KeyboardButton("3-19 QMKT"),
        ],
        [
            KeyboardButton("4-19 QMKT"),
            KeyboardButton("5-19 TMJ"),
            KeyboardButton("6-19 TMJ"),
        ],
        [
            btn_back,
            KeyboardButton("👑 7-19 AB"),
            btn_main,
        ],
    ],
    resize_keyboard=True)


#           --- 1-courses ---
groupMenu1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("1,2,3-21 NMKT"),
            KeyboardButton("1,2,3,4-21 QMKT"),
            KeyboardButton("1,2,3-21 TMJ"),
        ],
        [
            KeyboardButton("1,2-21 AB"),
            KeyboardButton("1,2-21 KT"),
            KeyboardButton("1,2,3-21 OOT"),
        ],
        [
            btn_back,
            KeyboardButton("4R-21"),
            btn_main,
        ],
    ],
    resize_keyboard=True)


#           --- 2-courses ---
groupMenu2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("1,2,4,5-20"),
            KeyboardButton("7,8,9-20"),
            KeyboardButton("14,15-20"),
        ],
        [
            KeyboardButton("21,22-20"),
            KeyboardButton("17,18,19-20"),
            KeyboardButton("11R,12R-20"),
        ],
        [
            btn_back,
            KeyboardButton("13R,24R-20"),
            btn_main,
        ],
    ],
    resize_keyboard=True)

