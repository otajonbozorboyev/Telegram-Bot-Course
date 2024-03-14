from aiogram import types

courses = [
    {
        "id": "001",
        "title": "Introduction",
        'url': "https://www.youtube.com/watch?v=f-znGRnP3nY&list=PLTV1jAY3nKHPvKZGpjxoIujxW05MTtEL6&index=1",
        'description': "Django frameworkiga kirish"
    },
    {
        "id": "002",
        "title": "Environment",
        'url': "https://www.youtube.com/watch?v=wWaquGTz_ak&list=PLTV1jAY3nKHPvKZGpjxoIujxW05MTtEL6&index=2",
        'description': "Djangoda loyiha muhitini yaratish"
    },
    {
        "id": "003",
        "title": "Application",
        'url': "https://www.youtube.com/watch?v=MEw9I03J_Rg&list=PLTV1jAY3nKHPvKZGpjxoIujxW05MTtEL6&index=3",
        'description': "Djangoda application yaratish"
    }
]


inline_results_django = []
for course in courses:
    inline_results_django.append(
        types.InlineQueryResultArticle(
            id=course['id'],
            title=course['title'],
            input_message_content=types.InputTextMessageContent(
                message_text=f"{course['title']} darsiga link: {course['url']}",
                parse_mode="HTML"
            ),
            url=course['url'],
            description=course['description']
        )
    )