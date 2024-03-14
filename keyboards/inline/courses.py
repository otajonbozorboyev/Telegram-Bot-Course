from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

data_keys = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Kursni boshlash", url="https://www.youtube.com/playlist?list=PLBlnK6fEyqRj9lld8sWIUNwlKfdUoPd1Y"),
        InlineKeyboardButton(text="Batafsil:", callback_data="course:data")
    ],
    [
        InlineKeyboardButton(text="✉️ Ulashish", switch_inline_query="kurs"),
    ],
])

java_keys = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Kursni boshlash", url="https://www.youtube.com/playlist?list=PLBlnK6fEyqRjKA_NuK9mHmlk0dZzuP1P5"),
        InlineKeyboardButton(text="Batafsil:", callback_data="course:java")
    ],
    [
        InlineKeyboardButton(text="✉️ Ulashish", switch_inline_query="kurs"),
    ],
])

django_keys = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Kursni boshlash", url="https://www.youtube.com/playlist?list=PLTV1jAY3nKHPvKZGpjxoIujxW05MTtEL6"),
        InlineKeyboardButton(text="Batafsil:", callback_data="course:django")
    ],
    [
        InlineKeyboardButton(text="✉️ Ulashish", switch_inline_query="kurs"),
    ],
])