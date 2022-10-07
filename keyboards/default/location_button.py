from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=
[
    [
        KeyboardButton(text="send your location", request_location=True)
    ]
]
                               )
