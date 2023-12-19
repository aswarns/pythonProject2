import re


# TODO Step 1 - Create function which takes 1 parameter

def strong_password_checker(password):
    is_strong = True
    # TODO Step 2 - Check for length of password
    if len(password) < 8:
        print("The Pasword must be 8 characters long!!!")
        is_strong = False

    # TODO Step 3 - Create regex for lowercases
    lower_regex = re.compile(r'[a-z]')
    if not (lower_regex.search(password)):
        print("The password must include at least 1 lowercase!!!")
        is_strong = False

    # TODO Step 4 - Create regex for uppercases
    upper_regex = re.compile(r'[A-Z]')
    if not (upper_regex.search(password)):
        print("The password must include at least 1 uppercase!!!")
        is_strong = False

    # TODO Step 5 - Create regex for digits
    digit_regex = re.compile(r'\d')
    if not (digit_regex.search(password)):
        print("The password must include at least 1 digit!!!")
        is_strong = False

    # TODO Step 6 - Create regex for special characters
    special_regex = re.compile(r'[!@#$%^&*()_+,.<>:;\\]')
    if not (special_regex.search(password)):
        print("The password must include at least 1 special chaarater!!!")
        is_strong = False

    # TODO Step 7 - If any of this returns none print message to the console
    if is_strong:
        print("Your password is strong")


strong_password_checker("a1Q#1234")