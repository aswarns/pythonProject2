"""
def volume_converter(val):
    value = val * 29.57353
    return value

print(volume_converter(5))


def greet_with_name_city(name, city):
    print(f"Hello {name}, ur place {city} is beautiful.")


greet_with_name_city(name="Ashish", city="Hyd")
greet_with_name_city(city="Hyd", name="Ashish")

greet_with_name_city("Singh", "HP")


import math

def area_of_wall(h,w,c):
    area_of_wall_insdie_funct = h * w
    cans =math.ceil(area_of_wall_insdie_funct / 4)
    print("Area of Wall ", area_of_wall_insdie_funct)
    print("Numbers of cans of paint ", cans)

height = int(input("Enter Height of wall: "))
width = int(input("Enter Width of wall: "))

area_of_wall(h=height, w=width, c=4)
"""
addd new kine

