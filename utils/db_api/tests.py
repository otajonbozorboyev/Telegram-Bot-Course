import asyncio

from utils.db_api.db_commands import Database


async def test():
    db = Database()
    await db.create()

    print("Users jadvalini yaratamiz...")
    await db.drop_users()
    await db.create_table_users()
    print("Yaratildi")

    print("Foydalanuvchilarni qo'shamiz")

    await db.add_user("Otajon", "softwares571", 123456789)
    await db.add_user("abbos", "abbos401", 12341123)
    await db.add_user("1", "1", 131231)
    await db.add_user("1", "1", 23324234)
    await db.add_user("Odiljon", "Odiljon0414", 4388229)
    print("Qo'shildi")

    users = await db.select_all_users()
    print(f"Barcha foydalanuvchilar: {users}")

    user = await db.select_user(id=5)
    print(f"Foydalanuvchi: {user}")

    #### Mahsulotlar uchun test
    print("Products jadvalini yaratamiz...")
    await db.drop_products()
    await db.create_table_products()
    await db.add_product(
        "food",
        "🥙 Oziq-ovqat",
        "tea",
        "🥤 Cola",
        "Coca Cola",
        "https://mir-s3-cdn-cf.behance.net/project_modules/fs/5307ef37224391.57397a56d79da.jpg",
        2,
        "Coca Cola",
    )
    await db.add_product(
        "food",
        "🥙 Oziq-ovqat",
        "tea",
        "💧 Zam Zam",
        "Zam Zam water",
        "https://content-22.foto.my.mail.ru/community/muslimmarket/_groupsphoto/h-964.jpg",
        6,
    )
    await db.add_product(
        "food",
        "🥙 Oziq-ovqat",
        "coffee",
        "☕ Coffee",
        "Nescafe Gold",
        "https://grodno24.com/assets/images/2020/12/kofe.jpg",
        5,
        "Discover our signature smooth, rich instant coffee. Coffee connoisseurs will appreciate the well-rounded taste and rich aroma in every cup. Our expertly crafted blend is great for all coffee drinking occasions, whenever you want to make a moment special. So why not relax, enjoy the now and savour the distinctive taste of this premium blend.",
    )
    await db.add_product(
        "food",
        "🥙 Oziq-ovqat",
        "milk",
        "🥛 Sut",
        "Nestle Sut. 1L",
        "https://pushkinovse.files.wordpress.com/2017/11/moloko.jpg",
        2,
    )
    await db.add_product(
        "electronics",
        "🖥️ Elektronika",
        "phone",
        "📱 Telefonlar",
        "iPhone 14 Pro Max",
        "https://cdn.mos.cms.futurecdn.net/FcpqWbioduDdVXJCPTa3T7.jpg",
        1000,
        "Yangi iPhone 13",
    )
    await db.add_product(
        "electronics",
        "🖥️ Elektronika",
        "laptop",
        "💻 Laptoplar",
        "macBook Pro M3",
        "https://static.nachasi.com/wp-content/uploads/2021/11/61975f969fae3_obzor-macbook-pro-14-2021-m1-pro-10.jpg",
        1600,
    )

    categories = await db.get_categories()
    print(f"{categories=}")
    print(categories[0]["category_code"])

    subcategories = await db.get_subcategories("food")
    print(f"{subcategories=}")
    print(subcategories[0]["subcategory_name"])

    count_products = await db.count_products("food")
    print(f"{count_products=}")

    count_sub_products = await db.count_products("food", "tea")
    print(f"{count_sub_products=}")

    products = await db.get_products("food", "tea")
    print(f"{products=}")

    product = await db.get_product(1)
    print(f"{product=}")
    product = await db.get_product(5)
    print(f"{product=}")


loop = asyncio.get_event_loop()
loop.run_until_complete(test())