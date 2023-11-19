import os
import platform


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')  # for windows
    elif platform == "linux":
        os.system('clear')  # for mac and linux


clear_screen()