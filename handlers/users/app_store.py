from aiogram.types import Message, CallbackQuery
from keyboards.inline.main_menu import products_menu, macos_menu, menu, m4_menu, buy_product
from loader import dp

@dp.callback_query_handler(text="menu")
async def show_products_menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="<b>Apple Products</b>",
                                    photo="https://i.ytimg.com/vi/sWzLabnddoc/maxresdefault.jpg",
                                    reply_markup=products_menu)

@dp.callback_query_handler(text="macos")
async def show_macos_menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="<b>MacOS Products</b>",
                            photo="https://sun9-71.userapi.com/impg/uXYzTC00dh5uM7nSpTft7Dy9T_Rj0YJVktJsiw/lxlNiMwynyA.jpg?size=604x344&quality=96&sign=adf48d970f3da5ba1fa3874064fbee1b&type=album",
                            reply_markup=macos_menu)

@dp.callback_query_handler(text="back")
async def back_to_products_menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"Salom, {call.from_user.full_name}!",
                            photo="https://images.unsplash.com/photo-1534802046520-4f27db7f3ae5?crop=entropy&amp;cs=tinysrgb&amp;fit=max&amp;fm=jpg&amp;ixid=MnwxMTc3M3wwfDF8c2VhcmNofDEwfHxhcHBsZXxlbnwwfHx8fDE2MTcxODM4Nzc&amp;ixlib=rb-1.2.1&amp;q=80&amp;w=2000",
                        reply_markup=menu)


@dp.callback_query_handler(text="m4")
async def show_m4_menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="<b>MacBook M4 Products</b>",
                            photo="https://frankfurt.apollo.olxcdn.com/v1/files/d4kqct3wl49e1-UZ/image",
                            reply_markup=m4_menu)


@dp.callback_query_handler(text="m4_pro")
async def show_m4_pro(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"""
<b>MacBook Pro M4</b>\n
<b>Price:</b> $2,499\n
<b>Specifications:</b>
- 16-inch Retina display\n
- Apple M4 chip with 10-core CPU and 16-core GPU\n
- 16GB unified memory\n
- 1TB SSD storage\n
- Magic Keyboard with Touch Bar\n
- Touch ID""", photo="https://s0.rbk.ru/v6_top_pics/media/img/6/74/346987335517746.webp",
                            reply_markup=buy_product)


@dp.callback_query_handler(text="buy")
async def buy_detail_product(call: CallbackQuery):
    await call.message.delete()
    await call.answer("Buyurtmangiz qabul qilindi", cache_time=60, show_alert=True)
    await call.message.answer_photo(caption="<b>Apple Products</b>",
                                    photo="https://i.ytimg.com/vi/sWzLabnddoc/maxresdefault.jpg",
                                    reply_markup=products_menu)

@dp.callback_query_handler(text="back1")
async def back_to_main_menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="<b>Apple Products</b>",
                                    photo="https://i.ytimg.com/vi/sWzLabnddoc/maxresdefault.jpg",
                                    reply_markup=products_menu)


@dp.callback_query_handler(text="back2")
async def back_to_main_menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="<b>MacOS Products</b>",
                            photo="https://sun9-71.userapi.com/impg/uXYzTC00dh5uM7nSpTft7Dy9T_Rj0YJVktJsiw/lxlNiMwynyA.jpg?size=604x344&quality=96&sign=adf48d970f3da5ba1fa3874064fbee1b&type=album",
                            reply_markup=macos_menu)

@dp.callback_query_handler(text="back3")
async def back_to_m4_menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="<b>MacBook M4 Products</b>",
                            photo="https://frankfurt.apollo.olxcdn.com/v1/files/d4kqct3wl49e1-UZ/image",
                            reply_markup=m4_menu)