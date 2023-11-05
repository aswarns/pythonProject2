import math
import random

#############
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
