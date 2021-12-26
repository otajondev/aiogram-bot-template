from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn_main = KeyboardButton("🏠 Menyu")
btn_backMenu = KeyboardButton("⬅️Orqaga")
btn_back = KeyboardButton("⬅️ Orqaga")
btn_back2 = KeyboardButton("⬅️  Orqaga")  # to groupMenu
#          --- Main menu ---

mainMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🎯 Dars jadvallari"),
            KeyboardButton("💰Hisob raqam"),
        ],
        [
            KeyboardButton("🏢Manzil"),
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

groupMenu = ReplyKeyboardMarkup(
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




#           --- 7-19 Week Days ---

weekMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🔥Dushanba"),
            KeyboardButton("⭐️Seshanba"),
            KeyboardButton("🕊Chorshanba"),],
        [
            KeyboardButton("🌿Payshanba"),
            KeyboardButton("☀️Juma"),
            KeyboardButton("🌈Shanba"),
        ],
        [
            btn_back2,
            btn_main,
        ],
    ], resize_keyboard=True)


#        --- 1-19 Week Days ---
weekMenu1_19 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🟠Dushanba"),
            KeyboardButton("🟡Seshanba"),
            KeyboardButton("🟢Chorshanba"),],
        [
            KeyboardButton("🔵Payshanba"),
            KeyboardButton("⚪️Juma"),
            KeyboardButton("🔴Shanba"),
        ],
        [
            btn_back2,
            btn_main,
        ],
    ], resize_keyboard=True)


# --- 2-19 Week Days ---
btnDu2_19 = KeyboardButton("🟡Dushanba")
btnSe2_19 = KeyboardButton("🟢Seshanba")
btnCho2_19 = KeyboardButton("🔵Chorshanba")
btnPa2_19 = KeyboardButton("⚪️Payshanba")
btnJu2_19 = KeyboardButton("🔴Juma")
btnSha2_19 = KeyboardButton("🟠Shanba")
weekMenu2_19 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDu2_19, btnSe2_19, btnCho2_19, btnPa2_19, btnJu2_19, btnSha2_19, btn_back2, btn_main)


# --- 3-19 Week Days ---
btnDu3_19 = KeyboardButton("🟢Dushanba")
btnSe3_19 = KeyboardButton("🔵Seshanba")
btnCho3_19 = KeyboardButton("⚪️Chorshanba")
btnPa3_19 = KeyboardButton("🔴Payshanba")
btnJu3_19 = KeyboardButton("🟠Juma")
btnSha3_19 = KeyboardButton("🟡Shanba")
weekMenu3_19 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDu3_19, btnSe3_19, btnCho3_19, btnPa3_19, btnJu3_19, btnSha3_19, btn_back2, btn_main)


# --- 4-19 Week Days ---
btnDu4_19 = KeyboardButton("🔵Dushanba")
btnSe4_19 = KeyboardButton("⚪️Seshanba")
btnCho4_19 = KeyboardButton("🔴Chorshanba")
btnPa4_19 = KeyboardButton("🟠Payshanba")
btnJu4_19 = KeyboardButton("🟡Juma")
btnSha4_19 = KeyboardButton("🟢Shanba")
weekMenu4_19 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDu4_19, btnSe4_19, btnCho4_19, btnPa4_19, btnJu4_19, btnSha4_19, btn_back2, btn_main)


# --- 5-19 Week Days ---
btnDu5_19 = KeyboardButton("⚪️Dushanba")
btnSe5_19 = KeyboardButton("🔴Seshanba")
btnCho5_19 = KeyboardButton("🟠Chorshanba")
btnPa5_19 = KeyboardButton("🟡Payshanba")
btnJu5_19 = KeyboardButton("🟢Juma")
btnSha5_19 = KeyboardButton("🔵Shanba")
weekMenu5_19 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDu5_19, btnSe5_19, btnCho5_19, btnPa5_19, btnJu5_19, btnSha5_19, btn_back2, btn_main)


# --- 6-19 Week Days ---
btnDu6_19 = KeyboardButton("🔴Dushanba")
btnSe6_19 = KeyboardButton("🟠Seshanba")
btnCho6_19 = KeyboardButton("🟡Chorshanba")
btnPa6_19 = KeyboardButton("🟢Payshanba")
btnJu6_19 = KeyboardButton("🔵Juma")
btnSha6_19 = KeyboardButton("⚪️Shanba")
weekMenu6_19 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDu6_19, btnSe6_19, btnCho6_19, btnPa6_19, btnJu6_19, btnSha6_19, btn_back2, btn_main)





