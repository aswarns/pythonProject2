"""Calculcate Total Price
->Create a program calculates the total price of items
that we want to buy.
->When program starts it will display the list of items,
using available_parts dictionary
->Then program asks to select an item
->Then based on user selected item, the program checks if
the item exist in the store or not. Because when quantity
of item is 0 then it is out of stock
->Finally, if it is not out of stock we calculate total price
of items and decrease quantity from the stock. This continues
until user select 0. And when the loop is terminated the total
price is printed to the console"""


available_parts = {
    "1": "computer",
    '2': "monitor",
    '3': "keyboard",
    '4': "mouse",
    '5': "hdmi cable",
    '6': "dvd drive"
}

price_quantity = {
    "computer": {"price": 500, "quantity": 10},
    "monitor": {"price": 200, "quantity": 8},
    "keyboard": {"price": 500, "quantity": 5},
    "mouse": {"price": 10, "quantity": 0},
    "hdmi cable": {"price": 20, "quantity": 7},
    "dvd drive": {"price": 50, "quantity": 5},
}


current_choice = None
total_price = 0

while current_choice != '0':
    if current_choice in available_parts:
        choosen_part = available_parts[current_choice]
        if price_quantity[choosen_part]["quantity"] > 0:
            print(f"Adding {choosen_part}")
            price_quantity[choosen_part]["quantity"] -= 1
            total_price += price_quantity[choosen_part]["price"]
        else:
            print(f"{choosen_part} is out of stock.")
    else:
        print("Please add options from the list.")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")
    current_choice = input(">")

print(f"Total price: {total_price}")
