# Blind auction
import os
import platform
from ascii_art import logo


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')  # for windows
    elif platform == "linux":
        os.system('clear')  # for mac and linux


clear_screen()
print("Welcome to Auction\n\n")
# print(logo)


def bidding_auction():
    bidder = "y"
    my_dict = {}

    while bidder == "y":
        print(logo)
        name = input("What is your name?: ")
        bid_amount = input("What is your bid amount?: ")
        my_dict[name] = bid_amount
        bidder = input("Are there any other bidder?(y/n): ")
        print(my_dict)
        v = list(my_dict.values())
        k = list(my_dict.keys())

        max_bidder = k[v.index(max(v))]
        max_val = my_dict[max_bidder]

        min_bidder = k[v.index(min(v))]
        min_val = my_dict[min_bidder]
        clear_screen()

    return f"{max_bidder} is winner and quoted amount is {max_val}$ \n \
        \b{min_bidder} is last and quoted amount is {min_val}$"


print(bidding_auction())


# ===================#
"""
# Blind auction
import os
import platform


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')  # for windows
    # elif platform == "linux":
    else:
        os.system('clear')  # for mac and linux


clear_screen()
print("Welcome to Auction\n\n")


bids = {}
bidding_finish = False


def highest_bidder(p_bids):
    highest_bid = 0
    bidder_name = ""
    for key, value in p_bids.items():
        if value > highest_bid:
            highest_bid = value
            bidder_name = key
    print(f"The winner is {bidder_name} with bid of {highest_bid}")


while not bidding_finish:
    name = input("What is your name?: ")
    bid_amount = int(input("What is your bid amount?: $"))
    bids[name] = bid_amount
    should_continue = input("Are there any other bidder?(y/n): ")
    if should_continue == "n" or should_continue == "N":
        bidding_finish = True
        highest_bidder(bids)
    elif should_continue == "Y" or should_continue == "y":
        clear_screen()
"""
