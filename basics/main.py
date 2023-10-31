#Are of circle using math module and PI and POWER of number
import math

radius = int(input("Enter Radius: "))

area = round(math.pi * math.pow(radius, 2), 2)
print("The area of circle is: ", area)