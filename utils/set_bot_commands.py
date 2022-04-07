from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            # types.BotCommand("kitob", "Kitoblar haqida"),
            # types.BotCommand("kurslar", "Kurslar haqida"),
        ]
    )
