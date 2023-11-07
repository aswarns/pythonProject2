import string
import random

letters = string.ascii_uppercase + string.ascii_lowercase
nums = ("0123456789")
symbols = ("+!@#$%^&*()<>?,./"'{}[]')

ask_letters = int(input("How many letters needed in upper case letters? "))
ask_num = int(input("How many numbers neededs? "))
ask_symbols = int(input("How many symbols needed? "))

"""letters = random.choices(letters, k=ask_letters)
num = random.choices(num, k=ask_num)
symbols = random.choices(symbols, k=ask_symbols)

result = ''.join(letters+num+symbols)
print(result)"""

password = ""

for letter in range(1, ask_letters + 1):
    password += random.choice(letters)

for i in range(1, ask_num + 1):
    password += random.choice(nums)

for j in range(1, ask_symbols + 1):
    password += random.choice(symbols)


print(f"Your password is : {password}")

password_list = list(password)

# Shuffling all the chars
random.shuffle(password_list)

final_password = ""

# using for loop
for ii in password_list:
    final_password += ii


print(final_password)

# using string join function
"""final_password = "".join(password_list)
print(final_password)"""
