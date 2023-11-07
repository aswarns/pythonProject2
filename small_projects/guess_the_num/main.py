import math
import random

lower = int(input("Enter lower no..."))
upper = int(input("Enter upper no..."))

number_of_chances = int(math.log(upper-lower+1, 2))
print(f"\n\t You've only {number_of_chances}  to guess the integer!\n")

generated_num = random.randint(lower, upper)

count = 0

while count < number_of_chances:
    count += 1
    guess = int(input("Guess the number ... "))
    if generated_num == guess:
        print(f"Congtrs u did it {count}")
        break
    elif guess > generated_num:
        print("U guess too high")
    elif guess < generated_num:
        print("U guess too LOW")

print(f"\n The number is {generated_num}")
print("\n Better Luck next time!")
