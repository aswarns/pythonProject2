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