#############
#Celsius to fahrenheit
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
#BMI Calculator
height = float(input("Enter your height in m: "))
weight =  float(input("Enter your weight in kg: "))

bmi = round(weight/(height*height), 2)

if  bmi < 18.5:
    print(f"ur BMI: {bmi}, ur UNDEWEIGHT")
elif bmi < 25:
    print(f"ur BMI: {bmi}, ur NORMAL")
elif bmi < 30:
    print(f"ur BMI: {bmi}, ur OVERWEIGHT")
else:
    print(f"ur BMI: {bmi}, ur OBESE")

'''
if  bmi > 30 and bmi < 35:
    print(f"ur BMI: {bmi}, ur OBESE")
elif bmi > 25:
    print(f"ur BMI: {bmi}, ur overweight")
elif bmi >= 18.5:
    print(f"ur BMI: {bmi}, ur NORMAL")
else:
    print(f"ur BMI: {bmi}, ur UNDERweight")
'''
##########################################
# Burger order

burger='''Price List.

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

order = input("Enter what would you like  M for Mini, N for Normal L for Large burger...")
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
except:
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
#Gross pay with Overtime 1.5 times over 40 hours
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

if year%4 == 0:
    if year%100 == 0:
        #print("Leap year.....")
        if year%400 == 0:
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

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

love = l+o+v+e

love_score = int(str(true)+str(love))

if love_score < 10 or love_score > 85:
    print(f"ur score is {love_score}, u go togeather like coke and mentos")
elif love_score >= 40 and love_score <= 70:
    print(f"Ur score {love_score}, ur alright")
else:
    print(f"ur score {love_score}.")
##########################################

#Gross pay with Overtime 1.5 times over 40 hours, 
#using TRY EXCEPT and using quit()
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
    if score >= 0.9 :
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
#Are of circle using math module and PI and POWER of number
import math

radius = int(input("Enter Radius: "))

area = round(math.pi * math.pow(radius, 2), 2)
print("The area of circle is: ", area)
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

