from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_callback, book_callback

# 1-usul:
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='💻 Kurslar', callback_data='courses'),
            InlineKeyboardButton(text='📚 Kitoblar', callback_data='books'),
        ],
        [
            InlineKeyboardButton(text='🔗 Data Structure',
                                 url="https://www.youtube.com/playlist?list=PLBlnK6fEyqRj9lld8sWIUNwlKfdUoPd1Y")
        ],
        [
            InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="📨 Ulashish", switch_inline_query="Zo'r bot ekan! Ko'rib chiqing."),
        ],
    ])

# Kurslar uchun keyboard:
# 2-usul:
coursesMenu = InlineKeyboardMarkup(row_width=1)

python = InlineKeyboardButton(text="🐍 Python dasturlash asoslari", 
                              callback_data=course_callback.new(item_name="python"))
coursesMenu.insert(python)

django = InlineKeyboardButton(text="🌐 Django Web dasturlash", callback_data="course:django")
coursesMenu.insert(django)

algorithm = InlineKeyboardButton(text="📖 Ma'lumotlar tuzilmasi va Algoritmlar",
                                 callback_data=course_callback.new(item_name='algorithm'))
coursesMenu.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
coursesMenu.insert(back_button)

# 3-usul:
books = {
    "Python": "python_book",
    "Data Structure": "data_science",
    "Algorithm": "beauty_of_algorithm",
}

booksMenu = InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    booksMenu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
booksMenu.insert(back_button)



# Har bir kurs uchun tugma:

algorithm_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ko'rish", url="https://www.youtube.com/watch?v=xLetJpcjHS0&list=PLBlnK6fEyqRj9lld8sWIUNwlKfdUoPd1Y&index=1")
    ]
])


django_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Xarid qilish", url="https://www.youtube.com/watch?v=rHux0gMZ3Eg")
    ]
])





