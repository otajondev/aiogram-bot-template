from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn_main = KeyboardButton("🏠 Menyu")
btn_backMenu = KeyboardButton("⬅️Orqaga")
btn_back = KeyboardButton("⬅️ Orqaga")
btn_back2 = KeyboardButton("⬅️  Orqaga")  # to groupMenu

# --- Main menu ---
btn_groups = KeyboardButton("🎯 Dars jadvallari")
btn_hisob_raqam = KeyboardButton("💰Hisob raqam")
btn_manzil = KeyboardButton("🏢Manzil")
btn_contact_us = KeyboardButton("📞 Biz bilan bog'lanish")
mainMenu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(btn_groups, btn_hisob_raqam, btn_manzil, btn_contact_us)





# --- Courses list ---
btn1k = KeyboardButton("1-kurs")
btn2k = KeyboardButton("2-kurs")
btn3k = KeyboardButton("3-kurs")
coursesMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1k, btn2k, btn3k, btn_backMenu)


# --- Groups list ---
btn_1_19 = KeyboardButton("1-19 NMKT")
btn_2_19 = KeyboardButton("2-19 NMKT")
btn_3_19 = KeyboardButton("3-19 QMKT")
btn_4_19 = KeyboardButton("4-19 QMKT")
btn_5_19 = KeyboardButton("5-19 TMJ")
btn_6_19 = KeyboardButton("6-19 TMJ")
btn_7_19 = KeyboardButton("👑 7-19 AB")
btn_back1 = KeyboardButton("⬅️  Orqaga")  # to coursesMenu
# groupList = [btn_1_19, btn_2_19, btn_3_19, btn_4_19, btn_5_19, btn_6_19, btn_7_19, btn_8_19]       #---ishlamadi
groupMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_1_19, btn_2_19, btn_3_19, btn_4_19, btn_5_19, btn_6_19, btn_back, btn_7_19, btn_main)







# --- 7-19 Week Days ---
btn_monday = KeyboardButton("🔥Dushanba")
btn_tuesday = KeyboardButton("⭐️Seshanba")
btn_wednesday = KeyboardButton("🕊Chorshanba")
btn_thursday = KeyboardButton("🌿Payshanba")
btn_friday = KeyboardButton("☀️Juma")
btn_saturday = KeyboardButton("🌈Shanba")
weekMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_monday, btn_tuesday, btn_wednesday, btn_thursday, btn_friday, btn_saturday, btn_back2, btn_main)


# --- 1-19 Week Days ---
btnDu1_19 = KeyboardButton("🟠Dushanba")
btnSe1_19 = KeyboardButton("🟡Seshanba")
btnCho1_19 = KeyboardButton("🟢Chorshanba")
btnPa1_19 = KeyboardButton("🔵Payshanba")
btnJu1_19 = KeyboardButton("⚪️Juma")
btnSha1_19 = KeyboardButton("🔴Shanba")
weekMenu1_19 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDu1_19, btnSe1_19, btnCho1_19, btnPa1_19, btnJu1_19, btnSha1_19, btn_back2, btn_main)



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





