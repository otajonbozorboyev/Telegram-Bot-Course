from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.product import Product


ds_praktikum = Product(
    title="Data Science va Sun'iy intellekt",
    description="Kursga to'lov qilish uchun ushbu tugmani boshing",
    currency="USD",
    prices=[
        LabeledPrice(
            label='Praktikum',
            amount=15000, # 150.00 USD
        ),
        LabeledPrice(
            label='Chegirma',
            amount=-1000, # -10.00 USD
        ),
    ],
    start_parameter="create_invoice_ds_praktikum",
    photo_url="https://i.pinimg.com/originals/f6/be/63/f6be6309b6ac1a630978ac14431fe5ec.jpg",
    photo_width=2746,
    photo_height=1819,
    need_email=True,
    need_name=True,
    need_phone_number=True,
)


programming_book = Product(
    title="The Art of Computer Programming",
    description="Kitobga to'lov qilish uchun ushbu tugmani bosing",
    currency="USD",
    prices=[
        LabeledPrice(
            label='Kitob',
            amount=10000, # 100.00 USD
        ),
        LabeledPrice(
            label='Yetkazib berish (7 kun)',
            amount=1000, # 10.00 USD
        ),
    ],
    start_parameter="create_invoice_programming_book",
    photo_url="http://pioneer.chula.ac.th/~skrung/main/images/l03_algorithm.png",
    photo_width=752,
    photo_height=648,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, # Foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)

REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title='Fargo (3 kun)',
    prices=[
        LabeledPrice(
            "Maxsus quti", 100),
        LabeledPrice(
            "3 ish kunida yetkazish", 500),
    ]
)

FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Express pochta (1 kun)',
    prices=[
        LabeledPrice(
            "1 kunda yetkazish", 15000),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(id='pickup',
                                       title="Do'kondan olib ketish",
                                       prices=[
                                           LabeledPrice("Yetkazib berishsiz", -500)
                                       ])