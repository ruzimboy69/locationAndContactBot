import asyncio
from aiogram import types

# from data.config import ADMINS
from loader import dp, db, bot

ADMIN = 1029027888


@dp.message_handler(text="/reklama", user_id=ADMIN)
async def send_advertising_to_all(message: types.Message):
    users = await  db.select_all_user()
    for user in users:
        await bot.send_message(chat_id=user[3], text="Kanalga obuna boling")
