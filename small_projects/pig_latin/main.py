# Pig Latin game
message = input("English to Pig Latin: ")
message_list = message.split()  # convert string to list
pig_latin = []
vowels = ('a', 'e', 'i', 'o', 'u')


def seprate_nonletters(p_word):
    prefix_non_letters = ""
    suffix_non_letters = ""
    while len(p_word) > 0 and not p_word[0].isalpha():
        prefix_non_letters += p_word[0]
        p_word = p_word[1:]
    if len(p_word) == 0:
        return (prefix_non_letters, suffix_non_letters, p_word)
    while not p_word[-1].isalpha():
        suffix_non_letters += p_word[-1]
        p_word = p_word[:-1]
    return (prefix_non_letters, suffix_non_letters, p_word)


# Translate pig latin
def translate_piglatin(p_word):
    prefix_consonant = ""
    if not p_word[0] in vowels:
        prefix_consonant += p_word[0]
        p_word = p_word[1:]
    if prefix_consonant != "":
        p_word += prefix_consonant + "ay"
    else:
        p_word += "yay"
    return p_word


for word in message_list:
    # Sepration the non letters at the beggining of word and end os the word
    prefix_non_letters, suffix_non_letters, word = seprate_nonletters(word)
    if word == "":
        pig_latin.append(prefix_non_letters)
        continue
    was_upper = word.isupper()
    was_title = word.istitle()
    word = word.lower()
    # Translate to pig latin
    word = translate_piglatin(word)
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()
    # Add non letters back to the start and end of the word
    pig_latin.append(prefix_non_letters+word+suffix_non_letters)
print(" ".join(pig_latin))
