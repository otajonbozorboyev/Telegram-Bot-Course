from aiogram import types

courses = [
    {
        "id": "001",
        "title": "Introduction",
        'url': "https://www.youtube.com/watch?v=mG4NLNZ37y4&list=PLBlnK6fEyqRjKA_NuK9mHmlk0dZzuP1P5&index=3",
        'description': "Java dasturlash tiliga kirish"
    },
    {
        "id": "002",
        "title": "Java displayi bilan tanishish",
        'url': "https://www.youtube.com/watch?v=ifirpBZLeCk&list=PLBlnK6fEyqRjKA_NuK9mHmlk0dZzuP1P5&index=5",
        'description': "Java dasturlash tilidagi display haqida tanishamiz"
    },
    {
        "id": "003",
        "title": "The first project in Java",
        'url': "https://www.youtube.com/watch?v=AVpLMoTnwM8&list=PLBlnK6fEyqRjKA_NuK9mHmlk0dZzuP1P5&index=9",
        'description': "Java dasturlash tilidagi birinchi loyihamiz"
    }
]


inline_results_java = []
for course in courses:
    inline_results_java.append(
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