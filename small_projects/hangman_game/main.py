import random
from logo_ascii_art import hangman_stages
from logo_ascii_art import logo
from replit import clear
# from hangman_words import word_list

print(logo)

word_list = ["UDEMY", "ASHISH", "PYTHON"]
secret_word = random.choice(word_list)
length_word = len(secret_word)
blanks = []
print(secret_word)
for _ in range(length_word):
    blanks.append("_")

guessed_letters = []
lives = 6
end_game = False
while not end_game:
    guess = input("Guess a letter: ").upper()
    clear()
    if guess in guessed_letters:
        print("You have already guessed this letter!")
        continue
    else:
        guessed_letters.append(guess)
    for position in range(length_word):
        letter = secret_word[position]
        if guess == letter:
            blanks[position] = letter
    if guess not in secret_word:
        lives -= 1
    if lives == 0:
        end_game = True
        print("You Loose!!!")
    print(" ".join(blanks))
    print(hangman_stages[lives])
    if "_" not in blanks:
        end_game = True
    if end_game:
        ask = input("Do you want to play the game? (Y/N)")
        if ask == "Y":
            secret_word = random.choice(word_list)
            blanks.clear()
            length_word = len(secret_word)
            for _ in range(length_word):
                blanks.append("_")
            end_game = False
            guessed_letters.clear()
            lives = 6
        else:
            print("See you next time!")
