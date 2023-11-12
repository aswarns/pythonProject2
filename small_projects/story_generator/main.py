def sentence_maker(text):
    question_words = ["what", "how", "where"]
    capitalized_text = text.capitalize()
    for word in question_words:
        if text.startswith(word):
            return "{}?".format(capitalized_text)
    return "{}.".format(capitalized_text)


result = []
while True:
    user_input = input("What is in your mind? ")
    if user_input == "\end":
        break
    else:
        complete_statement = sentence_maker(user_input)
        result.append(complete_statement)

story = " ".join(result)
print(story)
