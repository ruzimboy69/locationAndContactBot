import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)
        await message.answer("Xush kelibsiz")

    # Adminga xabar beramiz
    count = await db.count_users()
    msg = f"{user[1]} bazaga qo'shildi.\n Bazada {count} ta user bo'ldi"
    await bot.send_message(chat_id=1029027888, text=msg)