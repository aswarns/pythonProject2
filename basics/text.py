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
