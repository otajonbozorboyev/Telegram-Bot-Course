from aiogram import types
from data.courses_data import inline_results_data
from data.courses_django import inline_results_django
from data.courses_java import inline_results_java
from loader import dp
from keyboards.inline.courses import data_keys, java_keys, django_keys


@dp.inline_handler(text="data")
async def empty_query(query: types.InlineQuery):
    await query.answer(inline_results_data)

@dp.inline_handler(text="java")
async def empty_query(query: types.InlineQuery):
    await query.answer(inline_results_java)

@dp.inline_handler(text="django")
async def empty_query(query: types.InlineQuery):
    await query.answer(inline_results_django)



@dp.inline_handler(text="kurs")
async def photo_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultPhoto(
                id="photo #1",
                photo_url="https://w7.pngwing.com/pngs/996/137/png-transparent-introduction-to-algorithms-analysis-of-algorithms-algorithms-design-and-analysis-algorithm-design-introduction-text-label-orange.png",
                thumb_url="https://w7.pngwing.com/pngs/996/137/png-transparent-introduction-to-algorithms-analysis-of-algorithms-algorithms-design-and-analysis-algorithm-design-introduction-text-label-orange.png",
                caption="<b>Data structure and algorithms</b> kursi",
                reply_markup=data_keys
            ),
            types.InlineQueryResultPhoto(
                id="photo #2",
                photo_url="https://www.seoclerk.com/pics/000/935/056/5285b0772c335e6fcbbaa92560745c65.png",
                thumb_url="https://www.seoclerk.com/pics/000/935/056/5285b0772c335e6fcbbaa92560745c65.png",
                caption="<b>Java dasturlash tili</b> kursi",
                reply_markup=java_keys
            ),
            types.InlineQueryResultVideo(
                id="video #1",
                video_url="https://www.youtube.com/watch?v=63yr9dlI0cU",
                caption="Artificial Intelligence",
                description="Sun'iy ong sohasi haqida ajoyib video",
                title="AI revolutions",
                thumb_url="https://www.kindpng.com/picc/m/158-1585022_artificial-intelligence-services-machine-learning-transparent-background-hd.png",
                mime_type="video/mp4", # video/mp4 yoki text/html
            ),
        ]
    )

@dp.inline_handler()
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="Kurs #1",
                title="Data structure and algorithm",
                input_message_content=types.InputTextMessageContent(
                    message_text="Dars uchun link: https://www.youtube.com/playlist?list=PLBlnK6fEyqRj9lld8sWIUNwlKfdUoPd1Y",
                ),
                url="https://www.youtube.com/playlist?list=PLBlnK6fEyqRj9lld8sWIUNwlKfdUoPd1Y",
                thumb_url="https://w7.pngwing.com/pngs/996/137/png-transparent-introduction-to-algorithms-analysis-of-algorithms-algorithms-design-and-analysis-algorithm-design-introduction-text-label-orange.png",
                description="Data structure bu ma'lumotlar tuzilmasi bo'lib, dasturlash davomida juda qo'l keluvchi algoritm."
            ),
            types.InlineQueryResultArticle(
                id="Kurs #2",
                title="Java programming language",
                input_message_content=types.InputTextMessageContent(
                    message_text="Dars uchun link: https://www.youtube.com/playlist?list=PLBlnK6fEyqRjKA_NuK9mHmlk0dZzuP1P5",
                ),
                url="https://www.youtube.com/playlist?list=PLBlnK6fEyqRjKA_NuK9mHmlk0dZzuP1P5",
                thumb_url="https://www.seoclerk.com/pics/000/935/056/5285b0772c335e6fcbbaa92560745c65.png",
                description="Java dasturlash tili bu compiler tillar sirasiga kiradi"
            ),
            types.InlineQueryResultArticle(
                id="Kurs #3",
                title="Database management system",
                input_message_content=types.InputTextMessageContent(
                    message_text="Dars uchun link: https://www.youtube.com/playlist?list=PLBlnK6fEyqRi_CUQ-FXxgzKQ1dwr_ZJWZ",
                ),
                url="https://www.youtube.com/playlist?list=PLBlnK6fEyqRi_CUQ-FXxgzKQ1dwr_ZJWZ",
                thumb_url="https://www.kindpng.com/picc/m/158-1585022_artificial-intelligence-services-machine-learning-transparent-background-hd.png",
                description="Malumotlar ombori bu juda muhim bo'lgan qurilmdair"
            ),
        ],
    )

