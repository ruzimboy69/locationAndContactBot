from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from keyboards.inline.buy_books import book_keys
from loader import dp, bot


@dp.message_handler(Command("kitob"))
async def send_book(message: types.Message):
    photo_url = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.ukrgate.com%2Feng%2Fwp-content%2Fuploads%2F2021%2F02%2FThe-Ukrainian-Book-Institute-Purchases-380.9-Thousand-Books-for-Public-Libraries1.jpeg&imgrefurl=https%3A%2F%2Fwww.ukrgate.com%2Feng%2F%3Fp%3D7087&tbnid=Og8bA5zMQNf8FM&vet=12ahUKEwixmquIj6v6AhWtlYsKHerKDiEQMygBegUIARDnAQ..i&docid=P1JVfGDZ9fT-AM&w=1024&h=640&q=book&ved=2ahUKEwixmquIj6v6AhWtlYsKHerKDiEQMygBegUIARDnAQ"
    msg = "<b>Pythonda dasturlsh asoslari</b> kitobi"
    msg += " Narxi:50000 so'm\n\n"
    msg += "<b>Kitob quyidagi do'konlarda sotiladi:</b>AkademNashr\n Hilol nashr \n Azon kitoblari"
    await message.reply_photo(photo_url, caption=msg, reply_markup=book_keys)
