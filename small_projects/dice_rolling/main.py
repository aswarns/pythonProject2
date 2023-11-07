import random


roll = "Y"

while roll == "Y":
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"Dice1: {dice1} \nDice2: {dice2}")
    roll = input("Roll dice again: (Y/N) ")
