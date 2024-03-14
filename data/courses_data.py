from aiogram import types

courses = [
    {
        "id": "001",
        "title": "Introduction",
        'url': "https://www.youtube.com/watch?v=xLetJpcjHS0&list=PLBlnK6fEyqRj9lld8sWIUNwlKfdUoPd1Y&index=1",
        'description': "Data structure kursiga kirish"
    },
    {
        "id": "002",
        "title": "Data types",
        'url': "https://www.youtube.com/watch?v=ZniDyolzrBw&list=PLBlnK6fEyqRj9lld8sWIUNwlKfdUoPd1Y&index=2",
        'description': "Data structure o'zgaruvchilarga kirish"
    },
    {
        "id": "003",
        "title": "Advantages",
        'url': "https://www.youtube.com/watch?v=2JroZSycSXs&list=PLBlnK6fEyqRj9lld8sWIUNwlKfdUoPd1Y&index=3",
        'description': "Data structure afzalliklari haqida"
    }
]


inline_results_data = []
for course in courses:
    inline_results_data.append(
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