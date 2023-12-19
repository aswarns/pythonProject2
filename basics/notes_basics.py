# from ascii_art import logo
import platform
import os
import copy  # needed for DEEP COPY
import string
import math
import random
import pprint

#######################################
#######################################
# list
list_symbol = []
tuple_symbol = ()
set_symbol = {}
dict_symbol = {"key": "value"}
# Tuple new_tupple = (1,2,3)
# List  new_list = [1,2,3]
# Dictionary new_dict = {1: "a", 2: "b", 3: "c"}


# Convert string to list
string_one = "I love India"
word = string_one.split(" ")
print(type(word))


# convert list to string
string1 = ""
new_string = string1.join(word)
print(type(new_string))
#######################################
#######################################
my_tuple = (1, 2, 3)
print(my_tuple)

new_list = [1, 2, 3]
print(new_list)

print("\n\nPrinting TUPLE values")
club = ("FC Bareclone", "Spain", 1899)
a, b, c = club
print(a)
print(b)


print("\n\nPrinting list values")
my_list = ["one", "two", "three"]
one, two, three = my_list
print(one)
print(two)
print(three)
#######################################
# Celsius to fahrenheit
# (C * (9/5) + 32) = Fahrenheit

cel = int(input("Enter temp in Celcius\n"))
temp = int(cel * (9/5) + 32)

print(f"{cel} Celsius = {temp} Fahreneit")
##############
#  Trip cost calulator
print("Welcome to the trip Calulator")
days = float(input("How many days will you stay?  "))
hotel = float(input("how much per night? "))
flight = float(input("Flight cost? "))
car = float(input("Car rent? "))
other = float(input("other expence ? "))
total = round((days * hotel) + flight + (days * car) + other, 2)
print(f"Total cost: ${total}")
##########################################
# Mortgage Calculator

salary = int(input("WHats ur salary? "))

if salary >= 2000:
    print("Eligible for loan")
    credit_score = int(input("Whats credit score? "))
    if credit_score >= 800:
        print("Interst rate: 4%")
    elif credit_score >= 750:
        print("Interst rate: 6%")
    else:
        print("Interest rate rate: 8%")
else:
    print("Not eligible for loan.")
##########################################
# Even or odd

num = int(input("Enter a no... "))
if (num % 2) == 0:
    print("Even number")
else:
    print("Odd number")
##########################################
# BMI Calculator
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight/(height*height), 2)

if bmi < 18.5:
    print(f"ur BMI: {bmi}, ur UNDEWEIGHT")
elif bmi < 25:
    print(f"ur BMI: {bmi}, ur NORMAL")
elif bmi < 30:
    print(f"ur BMI: {bmi}, ur OVERWEIGHT")
else:
    print(f"ur BMI: {bmi}, ur OBESE")


if bmi > 30 and bmi < 35:
    print(f"ur BMI: {bmi}, ur OBESE")
elif bmi > 25:
    print(f"ur BMI: {bmi}, ur overweight")
elif bmi >= 18.5:
    print(f"ur BMI: {bmi}, ur NORMAL")
else:
    print(f"ur BMI: {bmi}, ur UNDERweight")

##########################################
# Burger order

burger = '''Price List.

Mini Burger (M) : $5
Normal Burger (N): $8
Large Burger (L) : $10

Add Mushroom : For Mini and Normal = $1, For Large = $2
Extra Cheese : $1
'''

print(burger)

mini_burger = 5
normal_burger = 8
large_burger = 10

mushroom = 1
mushroom_large = 2
extra_cheese = 1

order = input("M for Mini, N for Normal L for Large burger...")
mushroom_opt = input("Do u want mushroom, Please Y or no")
extra_cheese_opt = input("Do u want Cheese, Y or N...")

mushroom_opt_order = 0
extra_cheese_opt_order = 0

if order == "M":
    given_order = 5
    if mushroom_opt == "Y":
        mushroom_opt_order = 1
elif order == "N":
    given_order = 8
    if mushroom_opt == "Y":
        mushroom_opt_order = 1
elif order == "L":
    given_order = 10
    if mushroom_opt == "Y":
        mushroom_opt_order = 2
if extra_cheese_opt == "Y":
    extra_cheese_opt_order = 1

bill = given_order + mushroom_opt_order + extra_cheese_opt_order
print("Your Final bill: ", bill)
##########################################
# Mortgage Calculator

try:
    salary = int(input("WHats ur salary? "))
except ValueError:
    print("Enter an integer number!")
    salary = int(input("WHats ur salary? "))
else:
    if salary >= 2000:
        print("Eligible for loan")
        credit_score = int(input("Whats credit score? "))
        if credit_score >= 800:
            print("Interst rate: 4%")
        elif credit_score >= 750:
            print("Interst rate: 6%")
        else:
            print("Interest rate rate: 8%")
    else:
        print("Not eligible for loan.")
finally:
    print("Thanks for using Mortgage Calculator")
##########################################
# Gross pay with Overtime 1.5 times over 40 hours
work_hour = int(input("Enter working hours in number.."))
rate = int(input("Enter rate per hour..."))

pay = 0
min_hour = 40

if work_hour <= min_hour:
    pay = work_hour * rate
elif work_hour > min_hour:
    work_hour_ot = work_hour - min_hour
    pay_ot = (work_hour_ot * 1.5) * rate
    pay = (min_hour * rate) + pay_ot

print(pay)

##########################################
# Find leap year
year = int(input("Pls enter year:. "))

if year % 4 == 0:
    if year % 100 == 0:
        # print("Leap year.....")
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("LEAP YEAR")
else:
    print("Not a Leap year")
##########################################
# Love score calulator

ur_name = input("Enter ur name: ")
lover_name = input("Enter Lover name: ")

name = ur_name.lower() + lover_name.lower()

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

true = t+r+u+e

llll = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

love = llll+o+v+e

love_score = int(str(true)+str(love))

if love_score < 10 or love_score > 85:
    print(f"ur score is {love_score}, u go togeather like coke and mentos")
elif love_score >= 40 and love_score <= 70:
    print(f"Ur score {love_score}, ur alright")
else:
    print(f"ur score {love_score}.")
##########################################

# Gross pay with Overtime 1.5 times over 40 hours,
# using TRY EXCEPT and using quit()
try:
    work_hour = int(input("Enter working hours in number.."))
except ValueError:
    print("Error, please enter numeric input for wprk hours.")
    quit()

try:
    rate = int(input("Enter rate per hour..."))
except ValueError:
    print("Error, please enter numeric input for rate.")
    quit()

pay = 0
min_hour = 40

if work_hour <= min_hour:
    pay = work_hour * rate
elif work_hour > min_hour:
    work_hour_ot = work_hour - min_hour
    pay_ot = (work_hour_ot * 1.5) * rate
    pay = (min_hour * rate) + pay_ot

print(f"Pay:- {pay}")
##########################################
# Score Checker
try:
    score = float(input("Choose between 0.0 to 1.0  > "))
except ValueError:
    print("BAD SCORE")
    quit()

if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
        print("GRADE: A")
    elif score >= 0.8:
        print("GRADE: B")
    elif score >= 0.7:
        print("GRADE: C")
    elif score >= 0.6:
        print("GRADE: D")
    elif score < 0.6:
        print("GRADE: F")
else:
    print("BAD SCORE")
##########################################
# Are of circle using math module and PI and POWER of number
# import math

radius = int(input("Enter Radius: "))

area = round(math.pi * math.pow(radius, 2), 2)
print("The area of circle is: ", area)
##########################################
# Factorial of any number
# import math

num = int(input("Enter a number:"))

fact = math.factorial(num)
print(f"The factorial of {num} is: {fact}")
##########################################
# import random

# Love score calulator using ramdom module

ur_name = input("Enter ur name: ")
lover_name = input("Enter Lover name: ")

love_score = random.randint(0, 100)

if love_score < 10 or love_score > 85:
    print(f"ur score is {love_score}, u go togeather like coke and mentos")
elif love_score >= 40 and love_score <= 70:
    print(f"Ur score {love_score}, ur alright")
else:
    print(f"ur score {love_score}.")
##########################################
# heads and tails

# import random

# words = ("Heads", "Tails")
# result = random.choice(words)
# print(result)

result = random.randint(0, 1)

if result == 1:
    print("Heads")
else:
    print("Tails")
##########################################


def volume_converter(val):
    value = val * 29.57353
    return value


print(volume_converter(5))


def greet_with_name_city(name, city):
    print(f"Hello {name}, ur place {city} is beautiful.")


greet_with_name_city(name="Ashish", city="Hyd")
greet_with_name_city(city="Hyd", name="Ashish")

greet_with_name_city("Singh", "HP")
##########################################
# import math


def area_of_wall(h, w, c):
    area_of_wall_insdie_funct = h * w
    cans = math.ceil(area_of_wall_insdie_funct / 4)
    print("Area of Wall ", area_of_wall_insdie_funct)
    print("Numbers of cans of paint ", cans)


height = int(input("Enter Height of wall: "))
width = int(input("Enter Width of wall: "))

area_of_wall(h=height, w=width, c=4)

##########################################


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Name or last name cannot be empty"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name}, {formated_l_name}"


first_name = input("Enter Name: ")
second_name = input("Enter SName: ")
output = format_name(first_name, second_name)
print(output)

##########################################
# password as a parameter and checks the length of password.
# If the length longer than 8 character it returns True


def password_controller(custompassword):
    if len(custompassword) > 8:
        return True
    else:
        return False


custompassword = input("Enter 8 char password... ")
print(password_controller(custompassword))
##########################################
# Calculator only limited to +,-,*,/


def format_name(f_name, l_name, operator):
    if operator == "+":
        return f_name + l_name
    elif operator == "-":
        return f_name - l_name
    elif operator == "*":
        return f_name * l_name
    elif operator == "/":
        return f_name / l_name
    else:
        print("Enter entter only one of these +,-,*,/  ")


first_nu = int(input("Enter first integer value: "))
second_nu = int(input("Enter second integer value: "))
operator = input("+,-,*,/....")
output = format_name(first_nu, second_nu, operator)
print(output)
##########################################
# Leap year with Function Solution


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            # print("Leap year.....")
            if year % 400 == 0:
                return "Leap year"
            else:
                return "Not a leap year"
        else:
            return "Leap year"
    else:
        return "Not a leap year"


ask_year = int(input("Pls enter year:. "))

op_year = leap_year(year=ask_year)
print(op_year)
##########################################
"""A List of scores of students are given, implement a
program that calculates the highest score
from the given list.
DO NOT use any built in function such as max() and sum() !"""
student_scores = [80, 60, 50, 65, 75, 55]

student_scores.sort()
student_score = student_scores[-1]

print(f"The highest score in the class is: {student_score}")

sum = 0

for i in student_scores:
    sum += i

print(sum)
##########################################
student_scores = [80, 60, 50, 65, 75, 55]

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(score, highest_score)

##########################################
student_scores = [80, 60, 50, 65, 75, 55]


"""def sum_score_above_average(student_scores):
    sum = 0
    num = 0
    for i in student_scores:
        sum += i
        num += 1

    avg = round(sum/num, 2)
    print(f"sum_score_above_average(student_scores) # {avg}")


sum_score_above_average(student_scores)"""


def sum_score_above_average(p_student_score):
    sum_score = 0
    num_of_student = 0
    for score in p_student_score:
        sum_score += score
        num_of_student += 1
    average_score = sum_score / num_of_student
    sum_above_average = 0
    for score in p_student_score:
        if score > average_score:
            sum_above_average += score
        return sum_above_average


print(sum_score_above_average(student_scores))

##########################################


def password_controller(password):
    if len(password) > 8:
        return True
    else:
        return False


password_list = ["qwe", "123456", "987521267577", "abcdefgh"]

for password in password_list:
    result = password_controller(password)
    print(password, result)
##########################################
"""Implement a function that calculates the sum of
all odd numbers from 1 to 100 by using range()
function inside loop.
"""


def add_odd_numbers():
    total = 0
    for num in range(1, 101, 2):
        total += num
    return total


print(add_odd_numbers())
##########################################
"""Implement a function that calculates the sum of
all even numbers from 1 to 100 by using range()
function inside loop.
"""


def add_even_numbers(start, end):
    total = 0
    for num in range(start, end):
        if num % 2 == 0:
            total += num
    return total


start = int(input("Enter start nu: "))
end = int(input("Enter end nu: "))
end = end + 1

print(add_even_numbers(start, end))
##########################################
'''Implement a while loop which gets continuously
username from console by using input function and
terminates when the input is equal to "test".'''

# username = input("Enter username:")

username = ""


while username != "test":
    username = input("Enter username:")
##########################################
"""Numbers Divisible by 5 Until 130 Implement a function
which takes a given ordered list as a parameter and
displays numbers divisible by 5 and if a number is
greater than 130 display STOP in the console."""

list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]


def numbers_divisible_byfive(p_list):
    for i in list1:
        if i > 130:
            break
        if i % 5 == 0:
            print(i)
    print("STOP")


numbers_divisible_byfive(list1)
##########################################
# Factorial of any number
p_num = int(input("Enter a number:"))


def factorial(p_num):
    val = 1
    if p_num < 0:
        return "Factorial does not exist for negative numbers"
        exit()
    elif p_num == 0:
        return "The factorial of 0 is 1"
    else:
        for i in range(1, (p_num + 1)):
            val = val * i
        return f"The factorial of {p_num} is {val}"


print(factorial(p_num))
##########################################


def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError, TypeError):
        print("Error, Please enter numeric input")
        return False


count = 0
total = 0.0
average = 0.0

while True:
    input_num = input("Enter a number: ")
    if input_num == "done":
        break

    number = check_for_float(input_num)
    if not number:
        continue

    count += 1
    total = total + number

if count != 0:
    average = total/count
print(total, count, average)

##########################################


def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError, TypeError):
        print("Error, Please enter numeric input")
        return False


input_num = input("Enter a number: ")
if input_num == "done":
    quit()
number = check_for_float(input_num)
if not number:
    print("The first entered has to be number to continue..")
    quit()

smallest = number
biggest = number

while True:
    input_num = input("Enter a number: ")
    if input_num == "done":
        break
    number = check_for_float(input_num)
    if not number:
        continue
    if number > biggest:
        biggest = number
    if number < smallest:
        smallest = number

print(f"Maximum number: {biggest}, Minimum nu: {smallest}")

##########################################

# import random


def dice1():
    op = random.randint(1, 6)
    return op


def dice2():
    op = random.randint(1, 6)
    return op


print(f"Dice1: {dice1()}")
print(f"Dice2: {dice2()}")

##########################################
# import string
# import random

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

##########################################
# Square Of Items using Lists


def square_list(custom_list):
    new_list = []
    for i in custom_list:
        j = i**2
        new_list.append(j)
    return new_list


custom_list = [1, 2, 3, 4, 5]
print(square_list(custom_list))

##########################################


def square_list(custom_list):
    for index in range(len(custom_list)):
        custom_list[index] = custom_list[index] * custom_list[index]
    return custom_list


custom_list = [1, 2, 3, 4, 5]
print(square_list(custom_list))

##########################################
list1 = [10, 10, 5, 15, 50, 50, 20]

# find all  occurenace of 50 and replce with 50

# for index, count in enumerate(list1):
#    if count == 50:
#        list1[index] = 5
# print(list1)

# find first occurenace of 50 and replce with 50
count = list1.index(50)
list1[count] = 5
print(list1)
##########################################
"""First and Last Characters
Implement a function which takes the string type list
as a parameter and returns the count of the number of
strings where the string length is 2 or more and the
first and the last characters are"""


def count_words(list1):
    counter = 0
    for i in list1:
        if len(i) >= 2 and i[0] == i[-1]:
            counter += 1
    return counter


list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']
print(count_words(list1))
##########################################
numlist = []

while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    numlist.append(value)

avg = sum(numlist) / len(numlist)
print(f"Average: {avg}")
##########################################
"""Create a List from Two Lists
Given two lists create a third list by picking
an odd-index element from the first list and
even-index elements from the second."""

list_one = [4, 12, 16, 21, 24, 28, 32]
list_two = [5, 10, 15, 20, 25, 30, 35]

third_list = []

odd_element = list_one[1::2]
print(odd_element)

even_element = list_two[0::2]
print(even_element)

third_list.extend(odd_element)
third_list.extend(even_element)
print(third_list)
##########################################
"""Remove an element at index 4 in a given list and
add it to the 2nd position and at the end of the list."""

sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]

length = len(sample_list)
chunk_size = int(length / 3)

start = 0
end = chunk_size

for i in range(1, 4):
    list_chunk = sample_list[start:end]
    print(f"Chunk-{i} = {list(reversed(list_chunk))}")
    start = end
    end += chunk_size
##########################################
"""Format List
Print a given list in the format that is shown below using join method."""

custom_list = [1, 2, 3, 4, 5]

op = []
for i in custom_list:
    op.append(str(i))

custom_string = " | ".join(op)
print(custom_string)

##########################################
sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]

length = len(sample_list)
chunk_size = int(length/3)

start = 0
end = chunk_size

for i in range(1, 4):
    list_chunk = sample_list[start:end]
    print(f"Chunk-1: {list(reversed(list_chunk))}")
    start = end
    end += chunk_size

##########################################
custom_list = [1, 2, 3, 4, 5]
op = []
for i in custom_list:
    op.append(str(i))
custom_str = "|".join(op)
print(custom_str)

##########################################
# list insert function

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].insert(1, 7000)
print(list1)
##########################################
"""Extend Nested List
Given a nested list and update the list with
sub list ["h", "i", "j"] in such a way that
it will look like the following list."""

list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']

# print(list1[2][1][2])

ll = ["h", "i", "j"]
list1[2][1][2].extend(ll)
print(list1)

##########################################
"""Concatenate Two Lists in One List Item Wise
Implement a function which takes two lists as parameter and
return concatenation of these lists item wise."""


def concatenate(p_list1, p_list2):
    list3 = []
    for item1 in p_list1:
        for item2 in p_list2:
            list3.append(item1+item2)
    return list3


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
print(concatenate(list1, list2))
##########################################
# Bill roulette

user_input = input("Enter names seprated by comma and ends with ")

ll_list = user_input.split(",")

random_name = random.choice(ll_list)
print(f"{random_name} is going to pay the bill.")
##########################################
# Dictionary section

my_dict = {"Name": "Ashish", "Sirname": "Singh", "App s": "MS Office"}

my_dict["Apps"] = "MSOffice"
print(my_dict)
##########################################
# print(generate_dictionary(p_val))


def generate_dictionary(p_val):
    my_dict = {}
    for num in range(1, p_val+1):
        my_dict[num] = num * num
        num += num
    return my_dict


print(generate_dictionary(5))

##########################################
# Multiply Dictionary Items
# Implement a function which takes dictionary as a
# parameter and returns multiplication of values of this dictionary

my_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4}


def multiply_values(p_my_dict):
    output = 1
    for key in p_my_dict:
        output = output * p_my_dict[key]
    return output


print(multiply_values(my_dict))
##########################################
"""Student Grades
Implement a function which takes a dictionary as
a parameter in which student scores are stored and
converts their scores to grades and return it as new dictionary.

Scores 85 - 100: Grade = "Outstanding"
Scores 65 - 84: Grade = "Good"
Scores 50 - 64: Grade = "Acceptable"
Scores 50 lower: Grade = "Fail"
"""
student_scores = {
    "John": 90,
    "Edy": 48,
    "Marry": 88,
    "Ewan": 79,
    "Park": 62,
    "Miller": 41,
    "AAdi": 50,
    "Ashu": 59
}


def convert_grade(p_student_scores):
    for key, value in p_student_scores.items():
        if value >= 85:
            p_student_scores[key] = "Outstanding"
        elif value >= 65:
            p_student_scores[key] = "Good"
        elif value >= 50:
            p_student_scores[key] = "Acceptable"
        elif value < 50:
            p_student_scores[key] = "Fail"
    return p_student_scores


print(convert_grade(student_scores))

##########################################


def convert_grade(p_dict):
    student_grades = {}
    for key in p_dict:
        score = p_dict[key]
        if score >= 85:
            student_grades[key] = "Outstanding"
        elif score >= 65:
            student_grades[key] = "Good"
        elif score >= 50:
            student_grades[key] = "Acceptable"
        else:
            student_grades[key] = "Fail"
    return student_grades


print(convert_grade(convert_grade))
##########################################
# Dictionary section
"""Rename Key
Write a program which renames the key in the dictionary,
you need to rename key city to address in the following dictionary."""

my_dict = {
    "name": "Edy",
    "age": 30,
    "salary": 5000,
    "city": "London"
}


print(my_dict)

my_dict["address"] = my_dict.pop('city')
print(my_dict)

##########################################
# IN / NOT IN Operator

# List
list1 = [1, 2, 3, 4]
# print(2 in list1)
# print(9 in list1)

# String
string1 = "I Love Python"
# print("Love" in string1)
# print("Love" not in string1)
# print("ashish" in string1)

# Dictionary IN / NOT IN Operator
my_dict1 = {1: "one", 2: "Two", 3: "three"}
print("one" in my_dict1)
# Dictionary checks only keys ... not values
print(1 in my_dict1)
##########################################
"""Count Characters in a Word
Implement a function that takes a String as a parameter
and returns a dictionary with characters as keys from the
String and values are the occurrence of characters in the
String. Basically we are counting the occurrence of characters
in a given string and returning it as output in Dictionary."""


def count_character(p_val):
    my_dict = {}
    for i in p_val:
        if i not in my_dict:
            count_of_str = p_val.count(i)
            my_dict[i] = count_of_str
    return my_dict


print(count_character("BABACDAS"))

##########################################
# list inside Dictionary
lang = {
    "Ashish": ["Python", "Java", "Rubby"],
    "Aadi": "Pascal",
    "Akki": "VisualC"
}
# print(lang["Ashish"][0])
# print(lang["Ashish"][2])


# Dictionary inside Dictionary
modern_lang = {
    "Ashish": {"new_lang": ["Python", "Java", "Rubby"],
               "experience": 10
               },
    "Aadi": "Pascal",
    "Akki": "VisualC"
}

# print(modern_lang["Ashish"]["new_lang"][0])
# print(modern_lang["Ashish"]["new_lang"][1])
# print(modern_lang["Ashish"]["experience"])


# Dictionary inside list
my_list = [
    {"username": "Ashish",
     "new_lang": ["Python", "Java", "Rubby"],
     "experience": 10
     },
    {"username": "Aadi",
     "new_lang": ["Pascal", "VB", "Tally"],
     "experience": 10
     }
]
print(my_list)
print(my_list[1]["experience"])

##########################################
# import pprint

"""Nesting Dictionary Exercise
Implement a function that adds new key value pairs to
the programming_language list. You can see the list below
in which there is only two dictionaries, after insert method,
there should be three dictionaries. After insertion we need
to print programming_language list to the console.
"""
programming_language = [
    {"user_name": "Elshad",
     "favorite_languages": ["Python", "Java", "C#"],
     "experience": 10
     },
    {"user_name": "Renad",
     "favorite_languages": ["Scratch", "Python"],
     "experience": 2
     },
]


def add_new_user(p_user_name, p_favorite_languages, p_experience):
    new_user = {}
    new_user["user_name"] = p_user_name
    new_user["favorite_languages"] = p_favorite_languages
    new_user["experience"] = p_experience

    programming_language.append(new_user)
    pprint.pprint(programming_language)


add_new_user("Edy", ["Java", "Kotlin", "Swift"], 10)

##########################################
# import pprint

"""Count Characters in a Word
Implement a function that takes a String as a parameter
and returns a dictionary with characters as keys from the
String and values are the occurrence of characters in the
String. Basically we are counting the occurrence of characters
in a given string and returning it as output in Dictionary."""


def count_character(p_val):
    my_dict = {}
    for i in p_val:
        if i not in my_dict:
            count_of_str = p_val.count(i)
            my_dict[i] = count_of_str
    pprint.pprint(my_dict)


count_character("BABACDAS")

##########################################
item = {
    "computer": 10,
    "printer": 8,
    "mouse": 15,
    "keyboad": 4,
    "usb": 2
}

# print(item["webcam"])
# dictionary get method doesn't update the dictionary
# print(item.get("micro"), "item doesn't exists.")

# dictionary setdefault method update dictionary
quantity = item.setdefault("mic", 0)
print(quantity)
print(item)
##########################################
custom_dict = {
    0: "zero",
    1: "one",
    2: "two",
}

devices_list = ["phone", "tablet", "computer", "TV"]

# new_dict = {}.fromkeys(devices_list, 0)
# print(new_dict)

# keys = custom_dict.keys()
# print(keys)
for item in custom_dict.keys():
    print(item)
##########################################
"""Group Value Types
Implement a function which takes a List a parameter
and groups them according to their data types
(integer or string) and return dictionary."""

# import pprint

custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]

"""
def group_types(p_custom_list):
    new_dict = {}
    for i in p_custom_list:
        if isinstance(i, int):
            new_dict = {}.fromkeys(p_custom_list, "Integer")
        elif isinstance(i, str):
            new_dict = {}.fromkeys(p_custom_list, "String")
    pprint.pprint(new_dict)"""


def group_types(p_custom_list):
    op_dict = {}.fromkeys(p_custom_list)
    for key in p_custom_list:
        if isinstance(key, int):
            op_dict[key] = "Integer"
        if isinstance(key, str):
            op_dict[key] = "String"
    return op_dict


print(group_types(custom_list))

##########################################
custom_dict = {
    0: "zero",
    1: "one",
    2: "two",
}

for item in custom_dict:
    print(item, custom_dict[item])

print()

for key, value in custom_dict.items():
    print(key, value)

##########################################
names_dict = {
    1: "Elshad",
    2: "Renad",
    3: "Johanna",
    4: "Appmillers"
}


def value_length(p_names_dict):
    new_dict = {}
    for key, value in p_names_dict.items():
        new_dict[key] = {}
        new_dict[key][value] = len(value)
    return new_dict


print(value_length(names_dict))

##########################################
dict1 = {1: "one", 2: "two"}
dict2 = {3: "three", 4: "four"}
dict3 = {5: "five", 6: "six"}


def concatenate(dict1, dict2, dict3):
    new_dict = {}
    for dic in (dict1, dict2, dict3):
        new_dict.update(dic)
    return new_dict


print(concatenate(dict1, dict2, dict3))

##########################################
"""Remove Empty Items
Implement a function which takes as a parameter
dictionary and removes empty items from it and
return new dictionary. If there is not any empty
item in the dictionary it will return itself."""


custom_dict = {
    "name": "Elshad",
    "age": 28,
    "city": None
}


def remove_empty_items(p_dict):
    for key, value in list(p_dict.items()):
        if value is None:
            p_dict.pop(key)
    return p_dict


print(remove_empty_items(custom_dict))

##########################################
""" Merge Two Dictionary
Implement a function which takes as parameter two
dictionaries and merge these two dictionaries using
Dictionary methods into third dictionary."""


dict1 = {'One': 2, 'Two': 2, 'Three': 3}
dict2 = {'Three': 3, 'Four': 4, 'Five': 5}


def merge_dict(p_dict1, p_dict2):
    new_dict = {}
    new_dict.update(p_dict1)
    new_dict.update(p_dict2)
    return new_dict


print(merge_dict(dict1, dict2))

##########################################
""" Merge Two Dictionary
Implement a function which takes as parameter two
dictionaries and merge these two dictionaries using
Dictionary methods into third dictionary."""


dict1 = {'One': 2, 'Two': 2, 'Three': 3}
dict2 = {'Three': 3, 'Four': 4, 'Five': 5}


def merge_dict(p_dict1, p_dict2):
    new_dict = {}
    new_dict.update(p_dict1)
    new_dict.update(p_dict2)
    return new_dict


print(merge_dict(dict1, dict2))

##########################################
# import copy

# Dictionary SHallow copy (means copied Dictionary still refer to org and
# vice-versa, and if update one place it will update both Dictionary)

person = {
    "name": "Elshad",
    "age": 28,
    "city": ["London", "UK", "USA"]
}

print(person["city"])

# new_person = person
# new_person["city"] = "Hyd"
# print(new_person["city"])
# print(person["city"])

new_person = person.copy()
new_person["city"] = "Mumbai"
print(new_person["city"])
print(person["city"])


# Dictionary DEEP copy
new_person_deep_copy = copy.deepcopy(person)
new_person_deep_copy["city"] = "Mumbai"
print(new_person_deep_copy["city"])
print(person["city"])

##########################################
"""Custom Deep Copy for List Values
Implement custom deep copy method for a dictionary
where the values are lists."""


original_dict = {
    "names": ["Elshad", "John", "Edy"],
    "numbers": [1, 2, 3, 4, 5]
}


def deep_copy(p_original_dict):
    new_dict = {}
    for key, value in p_original_dict.items():
        new_value = value.copy()
        new_dict[key] = new_value
    return new_dict


copied_dict = deep_copy(original_dict)
copied_dict["names"].append("Jack")
copied_dict["numbers"].append(6)

print(original_dict)
print(copied_dict)

##########################################
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

##########################################
# Blind auction
# import os
# import platform
# from ascii_art import logo


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
        # print(logo)
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

##########################################
"""Sum Tuple Elements using Unpack
Write a Python program to unpack tuple in several
variables and print out sum of these variables, the
output must be as shown below."""

my_tuple = (10, 40, 80, 90)

a, b, c, d = my_tuple

print(f"{a}+{b}+{c}+{d}={a+b+c+d}")
##########################################
my_tuple = ("one", "two", "three")

"""for index in range(len(my_tuple)):
    value = my_tuple[index]
    print(index, value)"""


for index, value in enumerate(my_tuple):
    print(index, value)

print("\n\n")

# enumerate(list,1) we can use 2nd parameter to start index with given value
my_list = [1, 2, 3, 4]
for index, value in enumerate(my_list, 1):
    print(index, value)

##########################################
"""Even Index with Enumerate
Implement a function which takes as a parameter
a tuple and return a new tuple but only have even
index elements from original tuple."""

my_tuple = ("a", "b", "c", "d", "e", "f", "g")


def even_index_items(p_my_tuple):
    result_list = []
    for index, value in enumerate(p_my_tuple):
        result_list.append(value)
    return tuple(result_list)


print(even_index_items(my_tuple))

##########################################
"""Find Most Frequent Item
Implement a function which takes a tuple as a parameter
and returns another tuple with two elements. First element
is the most frequent item and the second element of number of repetition.

Hint: Use count() method"""

my_tuple = ("a", "b", "c", "d", "e", "a", "c",
            "e", "b", "e", "c", "a", "f", "e", "r")


def most_frequent(p_my_tuple):
    max_count = 0
    item = p_my_tuple[0]
    for value in p_my_tuple:
        current_item_count = p_my_tuple.count(value)
        if current_item_count > max_count:
            max_count = current_item_count
            item = value
    return (item, max_count)


print(most_frequent(my_tuple))

##########################################
"""Nested Tuple Indexing: - Using nested indexing print items from clubs tuple.
    The name of first player from Arsenal
    The year that Manchester United FC founded.
    Squad number of Dembele
    The tuple representing the 2nd player in Real Madrid CF"""


clubs = (("FC Barcelona", "Spain", 1899,
          [
              (3, "Pique"),
              (5, "Busquets"),
              (7, "Dembele"),
          ]
          ),
         ("Real Madrid CF", "Spain", 1902,
          [
              (7, "Hazard"),
              (9, "Benzema"),
              (10, "Modric"),
          ]
          ),
         ("Manchester United FC", "England", 1878,
          [
              (6, "Pogba"),
              (7, "Ronaldo"),
              (14, "Lingard"),
          ]
          ),
         ("Arsenal FC", "England", 1886,
          [
              (7, "Lacazette"),
              (14, "Aubameyang"),
              (16, "Holding"),
          ]
          ),
         )

# TODO
print(clubs[3][3][0][1])
print(clubs[2][2])
print(clubs[0][3][2][0])
print(clubs[1][3][1])

##########################################
"""Convert Tuple to Dictionary
Implement a function which takes a list of tuples
as a parameter and convert it to a dictionary and
return the dictionary."""

tuple_list = [("one", 11), ("two", 2), ("three", 3), ("four", 4)]


def convert_to_dict(p_tuple_list):
    result_dict = {}
    for key, value in p_tuple_list:
        result_dict.setdefault(key, value)
    return result_dict


print(convert_to_dict(tuple_list))

##########################################
"""Comparing Tuples
Implement a function which takes a string
(sentence) as a parameter and returns a tuple
in which the words from the given sentenced are
ordered based on their length."""

order_string = "Python is my favorite programming language"


def order_words(p_text):
    words = p_text.split(" ")
    nested_list = list()
    for word in words:
        nested_list.append((len(word), word))
    nested_list.sort()
    result = list()
    for length, word in nested_list:
        result.append(word)
    return tuple(result)


print(order_words(order_string))

##########################################
# sets
# fruits = {"apple", "pear", "limon", "grape", "orange"}

# print(type(fruits))

# empty set
# new_set = {*""}
# print(type(new_set))

my_set = set()
# print(type(my_set))

my_set.add(100)
my_set.add(99)
my_set.add(100)
print(my_set)


while len(my_set) < 5:
    element = input("Please enter value: ")
    my_set.add(element)


print(my_set)


my_list = ["apple", "apple", "orange", "grape", "grape", "orange", "apple"]

my_set = set(my_list)
print(my_set)

my_list = list(my_set)
print(my_list)
##########################################
"""Adding Members from List
Implement a function which takes as a parameter List
and add elements to a Set and return a set."""

my_list = [3, 4, 5, 1, 1, 3, 4, 9, 8]


def adding_set(my_list):
    my_set = set()
    for item in my_list:
        my_set.add(item)
    return my_set


print(adding_set(my_list))

##########################################
"""Delete Restricted Items
Set of items and set of restricted items are given,
based on the beach type (family or normal) the list
of items should be printed to the console. Restricted
items are not allowed to family beach and everything
else can be taken to normal beach except drugs."""

general_items = {
    "Sand toys",
    "Beach towels",
    "Beach umbrella",
    "Camp chair",
    "Snacks",
    "Hats",
    "Camera",
    "Sunglasses",
    "Alcholic Drinks",
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects"
}

restricted_items = {
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects",
    "Amplified Audio",
    "Drugs"
}

user_input = input("Select Beach type(1 - Family Beach, 2 - Normal Beach)")

if user_input == "1":
    for item in restricted_items:
        try:
            general_items.remove(item)
        except KeyError:
            print(f"Skipping {item}.")
else:
    try:
        general_items.remove("Drugs")
    except KeyError:
        print("Skipping Drugs.")
print("See below the list of item that you can take.")
for item in general_items:
    print(f"\t{item}")

##########################################
# fruits = {"apple", "apple", "orange", "grape", "grape", "orange", "apple"}

# print(fruits)

# furits.clear()
# print(furits)


# fruits.remove("apple")
# print(fruits)

# fruits.discard("orange")
# print(fruits)

# Set Union
fruits = {"apple", "apple", "orange", "grape", "Cucumber"}
vegs = {"Cucumber", "pepper", "onion"}

all_togeather1 = fruits.union(vegs)
# print(all_togeather1)

# pipe operator to club all sets as UNION
all_togeather2 = fruits | vegs
# print(all_togeather2)


"""Combine Sets
Two sets are given write a program which creates a
new set with all items from both sets by removing
duplicates. And print final set to the console"""

set1 = {10, 20, 30, 40, 50}
set2 = {60, 20, 50, 70}

combined_set = set1.union(set2)
# print(combined_set)

#####################
"""Union List of Sets
Implement a function which takes list of sets as a
parameter and returns one set which includes all
elements from the given list of sets."""

list_of_sets = [
    {10, 20, 30, 40, 50},
    {"apple", "orange", "limon", "pear"},
    {"London", "Berlin", "Paris"},
    {"Python", "Java", "Swift"},
    {10, "ten", "20", 20}
]


"""def convert_ls(list_of_sets):
    new_list = []
    for item in list_of_sets:
        for val in item:
            new_list.append(val)
    new_set = set(new_list)
    return new_set
"""


def convert_ls(list_of_sets):
    result_set = set()
    for item in list_of_sets:
        result_set = result_set.union(item)
    return result_set


# print(convert_ls(list_of_sets))

#####################

# Set intersection (common elements of set)

fruits = {"apple", "apple", "orange", "grape", "Cucumber"}
vegs = {"Cucumber", "pepper", "onion"}
mixed = {"apple", "Cucumber", "onion"}

all_set = fruits.intersection(vegs, mixed)
print(all_set)

# set using & operator
intersect = fruits & vegs & mixed
print(intersect)

set1 = set(range(20))
print(set1)

set2 = set(range(0, 20, 2))
print(set2)

set3 = set(range(0, 20, 3))
print(set3)

print(set.intersection(set1, set2, set3))

#####################

"""Find Numbers Divisible by 3 and 4
Implement a function which takes a parameter
N and returns Set of numbers which are divisible
by 3 and 4 between 0 and N."""


def divisible_by_3and4(p_num):
    set1 = set(range(0, p_num, 3))
    set2 = set(range(0, p_num, 4))

    all = set1.intersection(set2)
    return all


num = 100
print(divisible_by_3and4(num+1))

#####################

"""Find Preposition
Implement a function which takes a quote as a
parameter to find out which given prepositions
have been used in the quote. The function should
return the set of prepositions that are used in the quote."""


quote = """Success is no accident. It is hard work,
perseverance, learning, studying, sacrifice and most
of all, love of what you are doing or learning to do."""

prep = {"as", "but", "by", "for", "in", "of", "on", "to", "with"}


def find_prep(p_quote):
    words = p_quote.split()
    words_set = set(words)
    preps_used = words_set.intersection(prep)
    print(preps_used)


find_prep(quote)

#####################
# Set Subtraction
fruits = {"apple", "apple", "orange", "grape", "Cucumber"}
vegs = {"Cucumber", "pepper", "onion", "garlic"}

diff_fruits1 = fruits.difference(vegs)
print(diff_fruits1)

diff_veg1 = vegs.difference(fruits)
print(diff_veg1)


diff_fruits2 = fruits - vegs
print(diff_fruits2)

diff_veg2 = vegs - fruits
print(diff_veg2)

#####################
"""Difference of More than two Sets
There are three Sets are given. Write a program
that finds the difference of them."""

a = {1, 2, 3, 40, 50, 300, 400}
b = {10, 20, 30, 40, 300}
c = {100, 200, 300, 400}

differenc_a_b = a.difference(b, c)
print(differenc_a_b)

print(a-b-c)
#####################
# Set Symmectric difference (remove common elements,
# print only element which is uncommon)

fruits = {"apple", "apple", "orange", "grape", "Cucumber"}
vegs = {"Cucumber", "pepper", "onion", "garlic"}

set_symmetric_difference = fruits.symmetric_difference(vegs)
print(set_symmetric_difference)

#####################
# modifying sets
fruits = {"apple", "apple", "orange", "grape", "Cucumber"}
vegs = {"Cucumber", "pepper", "onion", "garlic", "broccoli"}

union_set = fruits.union(vegs)
print(union_set)

fruits |= vegs
print(fruits)
#####################
# Subset and superset
animals = {"Dog", "Cat", "Robin", "Hoese", "Swallow"}
birds = {"Robin", "Swallow"}

result = birds.issubset(animals)
print(result)

result1 = animals.issubset(birds)
print(result1)

print(birds <= animals)

# set superset
result2 = birds.issuperset(animals)
print(result2)

result3 = animals.issuperset(birds)
print(result3)
##########################################
while True:
    ask = input("ENter a number: ")
    sum_of_digit = 0
    try:
        for digit in ask:
            sum_of_digit += int(digit)
    except ValueError:
        print("This value is not numeric!")
    else:
        print(f"Sum of the number: {sum_of_digit}")
    finally:
        break

##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
