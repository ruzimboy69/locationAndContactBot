import logging

from aiogram import Dispatcher

ADMIN = 1029027888


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(ADMIN, "Bot ishga tushdi")

    except Exception as err:
        logging.exception(err)
