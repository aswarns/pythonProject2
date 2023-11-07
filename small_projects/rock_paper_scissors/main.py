import random
# rock, pspper scissors


def select_computer_action():
    possible_actoin = ("rock", "papper", "scissors")
    computer_action = random.choice(possible_actoin)
    return computer_action


def determine_winner(computer_action, user_action):
    if user_action == computer_action:
        print(f"Both choose {user_action}, it's' tie.")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("\nRock smashed scissors! You WIN!")
        else:
            print("\nPapper covers rock!, You LOOSE")
    elif user_action == "papper":
        if computer_action == "scissors":
            print("\nscissors cuts papper! You LOOSE!")
        else:
            print("\nPapper covers rock!, You WIN")
    elif user_action == "scissors":
        if computer_action == "papper":
            print("\nScissors cuts papper! You WIN!")
        else:
            print("\nRock covers scissors!, You LOOSE")


while True:
    user_action = input("Enter a chice (rock, papper, scissors): rock ")
    computer_action = select_computer_action()
    determine_winner(computer_action, user_action)

    print(f"u choose {user_action}, computer chose {computer_action}.")

    play_again = input("Play again (Y/N) ")
    if play_again != "Y":
        break
