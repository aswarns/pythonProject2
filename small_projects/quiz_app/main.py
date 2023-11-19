from logo import logo
from questions import quiz
from clear_screen import clear_screen

# Greeting function


def greeting(p_question_num):
    print(logo)
    print(f"There are a total of {p_question_num} questions, you can skip\
        anytime by typing 'skip'")
    input("Enter any key to continue ... ")


# Checking Question and answers
def check_answer(question_num, answer, attempts, player):
    clear_screen
    correct_answer = quiz[question_num]["answer"]
    if correct_answer.lower() == answer.lower():
        print(
            f"Corret answer! \n{player} score is {players_score[player] + 1}")
        return True
    else:
        print(
            f"Wrong answer: (\nYou have {attempts-1} attempt left\nTry Again)")


# for Switching users
def switch_user(p_user_index):
    if p_user_index == 0:
        return 1
    return 0


# Find winner
def find_wiiner(player1, player2):
    clear_screen
    if players_score[player1] > players_score[player2]:
        print(f"{player1} WON! the score is players_score[player1].")
    elif players_score[player1] > players_score[player2]:
        print(f"{player2} WON! the score is players_score[player2].")
    else:
        print("It is a DRAW!!!")


greeting(len(quiz))
players = input("Enter 2 players with spaces: ")
players_list = players.split(" ")

# Dictionary add list as key and defualt value as 0
# players_dict = {}
# for p in players_list:
#    players_dict[p] = 0
# print(players_dict)

# Python way :-  Dictionary add list as key and defualt value as 0
players_score = dict.fromkeys(players_list, 0)
current_player = players_list[0]  # starting with first player

for question in quiz:
    print("---------------------------------------")
    print(f"It is {current_player}'s turn.")
    attempts = 2
    while attempts > 0:
        print(quiz[question]["question"])
        answer = input("Enter answer (to move to next questopn, type 'skip): ")
        if answer == "skip":
            break
        check = check_answer(question, answer, attempts, current_player)
        if check:
            players_score[current_player] += 1
            break
        attempts -= 1
    current_player_index = players_list.index(current_player)
    next_player_index = switch_user(current_player_index)
    current_player = players_list[next_player_index]

find_wiiner(players_list[0], players_list[1])
show_correct_answers = input("Do you wan to see correct answers? Y/N: \n\n\n")
if show_correct_answers == "y":
    for question_num, nested_dic in quiz.items():
        for key, value in nested_dic.items():
            print(key + ":", value)
print("Thanks for playing")
