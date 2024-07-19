def user_choice():

    choice = 'WRONG'
    acceptable_range = range(0, 10)
    within_range = False

    # 2 condications check
    # Digit or within range == false
    while choice.isdigit() is False or within_range is False:
        choice = input("Pls enter a num (0-10): ")

        # Digit check
        if choice.isdigit() is False:
            print("Sorry that is not a digit.\n\n")

        # Range check
        if choice.isdigit() is True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of range.\n")
                within_range = False

    return int(choice)


print(user_choice())
