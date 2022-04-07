from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from keyboards.inline.callback_data import course_callback, book_callback

# 1-usul.
aboutMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    # [
    #     InlineKeyboardButton(text="💻 Kurslar", callback_data="courses"),
    #     InlineKeyboardButton(text="📚 Kitoblar", callback_data="books"),
    # ],
    [
        InlineKeyboardButton(text="🌐 Institutimiz saytiga o'tish", url="https://tktiyf.uz/"),
    ],
    [
        InlineKeyboardButton(text="📲 Rasmiy kanal", url="https://t.me/tkti_yangiyerf"),
    ],
    [
        InlineKeyboardButton(text="📚 ARM", url="https://t.me/kutubxona_tktiyf"),
    ],
    # [
    #     InlineKeyboardButton(text="🔗 HEMIS", url="https://t.me/tkti_yangiyerf"),
    # ],
    [
        InlineKeyboardButton(text="🌐 HEMIS (Talaba)", url="https://stktiyf.e-edu.uz/dashboard/login"),
    ],
    [
        InlineKeyboardButton(text="🌐 HEMIS (O'qituvchi)", url="https://tktiyf.e-edu.uz/dashboard/login"),
    ],
    [
        InlineKeyboardButton(text="✉️Ulashish", switch_inline_query="Zo'r bot ekan"),
    ],

])



mapMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    # [
    #     InlineKeyboardButton(text="💻 Kurslar", callback_data="courses"),
    #     InlineKeyboardButton(text="📚 Kitoblar", callback_data="books"),
    # ],
    [
        InlineKeyboardButton(text="🔗 Google Mapsga o'tish", url="https://maps.app.goo.gl/WVCTHiL7jzZWBqFr8"),
    ],
    # [
    #     InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat=""),
    # ],
    # [
    #     InlineKeyboardButton(text="✉️Ulashish", switch_inline_query="Zo'r bot ekan"),
    # ],
])

engrade = InlineKeyboardMarkup(
    inline_keyboard=[

    [
        InlineKeyboardButton(text="Kunduzgi kirish ballari", url="https://abt.uz/university/view?slug=toshkent-kimyo-texnologiya-instituti-yangiyer-filiali&year=2021&type=kunduzgi&lang=uz"),
    ],
    [
        InlineKeyboardButton(text="Kunduzgi kirish ballari (RUS)", url="https://abt.uz/university/view?slug=toshkent-kimyo-texnologiya-instituti-yangiyer-filiali&year=2021&type=kunduzgi&lang=ru"),
    ],
    [
        InlineKeyboardButton(text="Sirtqi kirish ballari", url="https://abt.uz/university/view?slug=toshkent-kimyo-texnologiya-instituti-yangiyer-filiali&year=2021&type=sirtqi&lang=uz"),
    ],
    [
        InlineKeyboardButton(text="Shaxsiy kabinet", url="https://my.dtm.uz/login"),
    ],

])

# # 2-usul
# coursesMenu = InlineKeyboardMarkup(row_width=1)
#
# python = InlineKeyboardButton(text="🐍 Python Dasturlash Asoslari", callback_data=course_callback.new(item_name="python"))
# coursesMenu.insert(python)
#
# django = InlineKeyboardButton(text="🌐 Django Web Dasturlash", callback_data=course_callback.new(item_name="django"))
# coursesMenu.insert(django)
#
# telegram = InlineKeyboardButton(text="🤖 Mukammal Telegram bot", callback_data="course:telegram")
# coursesMenu.insert(telegram)
#
# algorithm = InlineKeyboardButton(text="📈 Ma'lumotlar Tuzilmasi va Algoritmlar", callback_data="course:algorithm")
# coursesMenu.insert(algorithm)
#
# back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
# coursesMenu.insert(back_button)


# # 3 - usul
#
# books = {
#     "Python. Dasturlash asoslari": "python_book",
#     "C++. Dasturlash tili": "cpp_book",
#     "Mukammal Dasturlash. JavaScript": "js_book",
# }
#
# booksMenu = InlineKeyboardMarkup(row_width=1)
# for key, value in books.items():
#     booksMenu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
# booksMenu.insert(back_button)
#
# # Har bir kurs uchun tugma
# telegram_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Xarid qilish", url="https://mohirdev.uz/courses/telegram/")
#     ]
# ])
#
# algoritm_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Ko'rish", url="https://mohirdev.uz/courses/algoritmlar/")
#     ]
# ])
