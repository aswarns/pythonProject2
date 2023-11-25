# Pig Latin game

vowels = ['a', 'e', 'i', 'o', 'u']
vowels_upper = ['A', 'E', 'I', 'O', 'U']
consonant_suffix = "ay"
vowels_suffix = "yay"

text = input("Enter the English message to tranlate into Pig Latiin: ")


words = text.split(" ")
for item in words:
    if item[0] in vowels or item[0] in vowels_upper:
        print(item+vowels_suffix)
    else:
        item = item.lower()
        item_fist_char = item[:1]
        item_without_fist_char = item[1:]
        print(item_without_fist_char+item_fist_char+consonant_suffix)
