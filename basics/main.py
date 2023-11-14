import pprint

"""Nesting Dictionary Exercise
Implement a function that adds new key value pairs to
the programming_language list. You can see the list below
in which there is only two dictionaries, after insert method,
there should be three dictionaries. After insertion we need
to print programming_language list to the console.
"""
programming_language = [
    {"user_name": "Elshad",
     "favorite_languages": ["Python", "Java", "C#"],
     "experience": 10
     },
    {"user_name": "Renad",
     "favorite_languages": ["Scratch", "Python"],
     "experience": 2
     },
]


def add_new_user(p_user_name, p_favorite_languages, p_experience):
    new_user = {}
    new_user["user_name"] = p_user_name
    new_user["favorite_languages"] = p_favorite_languages
    new_user["experience"] = p_experience

    programming_language.append(new_user)
    pprint.pprint(programming_language)


add_new_user("Edy", ["Java", "Kotlin", "Swift"], 10)
