# Step1 - Ask user to enter 5 numbers between  1 and 69
import random

while True:
    print("Enter 5 num from 1 to 69 with spaces between\n each \
num (ie 1, 17 23 42 50)")
    responce = input("> ")

    numbers = responce.split()
    if len(numbers) != 5:
        print("Please enter 5 numbers, seprated by spaces.")
        continue
    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print("Please enter numbers like 1, 5 or 35.")
        continue

    between_1_69 = True
    for item in numbers:
        if not (1 <= item <= 69):
            print("The numbers must be between 1 and 69")
            between_1_69 = False
            break
    if not between_1_69:
        continue
    if len(set(numbers)) != 5:
        print("You must enter 5 diff numbers")
        continue
    break

while True:
    responce = input("Enter the PowerBall num from 1 to 26.> ")
    try:
        powerball = int(responce)
    except ValueError:
        print("Enter a num like 1 or 11 or 26")
        continue

    if not (1 <= powerball <= 26):
        print("The Powerball um must be between 1 and 26")
        continue
    break

while True:
    print("How many times toy want to play (Max 1000000)?: ")
    responce = input('>')
    try:
        numPlays = int(responce)
    except ValueError:
        print("Please enter numbers like 1, 5 or 35.")
        continue
    # Check that the number is between 1 and 1000000
    if not (1 <= numPlays <= 1000000):
        print("You can play between 1 and 1000000 times.")
        continue
    break

# Run the Simulation
price = '$ ' + str(2 * numPlays)
print(f"It costs {price} to play {numPlays} times, \
    \nbut dont worry. I'm sure you will win it all back.")
input("Press any key to start...")
possibleNumber = list(range(1, 70))
for i in range(numPlays):
    # Come up with lottery numbers
    random.shuffle(possibleNumber)
    winningNumbers = possibleNumber[0:5]
    winningPowerball = random.randint(1, 26)
    # Display the winning numbers
    print("The winining numbers are: ", end="")
    allWinningNumbers = ""
    for num in winningNumbers:
        allWinningNumbers += str(num) + ' '
    allWinningNumbers += "and " + str(winningPowerball)
    print(allWinningNumbers, end="")
    # Check winner
    if (set(numbers) == set(winningNumbers) and powerball == winningPowerball):
        print("You have won the powerball lottery.")
        break
    else:
        print(" You lost.")
print(f"You have wasted {price}")
print("Thanks for playing")
