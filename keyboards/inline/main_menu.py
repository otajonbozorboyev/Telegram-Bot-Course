from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛍 Menu", callback_data="menu"),
        ]
    ]
)

products_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 MacOS", callback_data="macos"),
            InlineKeyboardButton(text="📱 iPhones", callback_data="iphones"),
        ],
        [
            InlineKeyboardButton(text="⌚ Smart Watches", callback_data="smart_watches"),
            InlineKeyboardButton(text="📲 iPad", callback_data="ipad"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="back"),
        ]
    ]
)

macos_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 M1", callback_data="m1"),
            InlineKeyboardButton(text="💻 M2", callback_data="m2"),
        ],
        [
            InlineKeyboardButton(text="💻 M3", callback_data="m3"),
            InlineKeyboardButton(text="💻 M4", callback_data="m4"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="back1"),
        ]
    ]
)
m4_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 MacBook Pro", callback_data="m4_pro"),
            InlineKeyboardButton(text="💻 MacBook Air", callback_data="m4_air"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="back2"),
        ]
    ]
)

buy_product = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛒 Buy", callback_data="buy"),
            InlineKeyboardButton(text="🔙 Ortga", callback_data="back3"),
        ]
    ]
)