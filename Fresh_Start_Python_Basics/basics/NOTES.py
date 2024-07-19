
from random import shuffle

name = "Ashish Singh"
shuffle(name)
# print('Thisd is a String {}'.format('INSERTED'))

# print('The {2} {2} {2}'.format('Fox', 'Brown', 'last'))

# print('The {f} {b} {f}'.format(f='Fox', b='Brown', q='last'))

# result = 100/777
# print(result)

# print("The result was {r:1.2f}".format(r=result))

# print(f'Hello, his name is {name}')

# name = 'Sam'
# age = 3
# print(f'{name} is {age} years old.')


# list
my_list = [1, 2, 3]
# print(len(my_list))
my_list1 = ['one', 'two', 'three']
# print(my_list1[-1])

new_list = my_list + my_list1
# print(new_list)

# new_list[0] = 'ONE'
# print(new_list)

# new_list.append('six')
# print(new_list)

# new_list.append(8)
# print(new_list)


# print(new_list.pop())
# print(new_list)

# popped_item = new_list.pop()
# print(popped_item)
# print(new_list)

# popped_item_from_begining = new_list.pop(0)
# print(popped_item_from_begining)
# print(new_list)

# new_list = ['e','d','c','a','e']
# num_list = [4,5,6,3,1,2,5,3,2]

# new_list.sort()
# print(new_list)

# print(num_list)
# num_list.sort()
# print(set(num_list))

# How do I index a nested list? For example grab 2 from [1,1,[1,2]]?
# ll = [1, 1, [1, 2]]
# print(ll[2][1])

# Disctionary

# my_dict = {1: "One", 2: "Two", 3: "Three"}
# print(my_dict[3])

# my_dict['new_key'] = 200
# print(my_dict)

# print(my_dict.values())

# print(my_dict.items())

# tuple
# t = (1, 2, 3, 'one')
# print(t[-1])

# t = ('a', 'c', 'a', 'a', 'b', 'b')
# print(t.count('b'))

# t[0] = 1


# Set

# my_set = set()
# my_set.add(1)
# my_set.add(1)
# my_set.add(1)
# print(my_set)


# my_list = [1,1,1,2,2,2,3,3,3,4,4,4]
# print(my_list)
# print(set(my_list))

# print(set('Mississippi'))

# print(type(set([1, 2, 3])))

# myfile = open
# ("C:\\Users\\aadi\\Downloads\\DEVOPS\\py-projects\\pythonProject2\\Fresh_Start_Python_Basics\\basics\\NOTES.py")

# print(myfile.read())
# myfile.seek(0)
# print(myfile.readlines())
# myfile.close()

# with open("NOTES.py") as new_file:
#    contents = new_file.readlines()
#    print(contents)

# with open('NOTES.py', 'a') as new_file:
#    new_file.write("\nthis is added by script")

# with open("asaasdhj.txt", 'w') as f:
#    f.write("I CREATED THIS FILE")

# with open("asaasdhj.txt", 'r') as new_file:
#    contents = new_file.readlines()
#    print(contents)

# print( 4 + 6 * 5)
# PEMDAS

# String
# s = 'hello'
# print(s[1])
# print(s[::-1])
# print(s[-1])
# print(s[4])


# List
# l = [0,0,0]
# print(type(l))

# list3 = [1, 2, [3, 4, 'hello']]
# print(list3[2][2])
# list3[2][2] = "goodbye"
#
# list4 = [5,4,3,2,1,3,4,1]
# list4.sort()
# print(type(list(set(list4))))


# Disctionary
# d = {'simple_key': "hello"}
# print(d['simple_key'])
# d = {'k1': {'k2': 'hello'}}
# print(d['k1']['k2'])
# d = {'k1': [{'nest_key': ['this is deep', ['hello',1]]}]}
# print(d['k1'][0]['nest_key'][1][0])

# print(1 < 2)
# print(2 < 3)
# print(1 < 2 and 2 < 3)
# print(('h' == 'h') and (2 == 2))
# print(1 == 1 or 2 == 2)
# print(1 == 1 or 2 != 2)
# print(not 1 == 1)

# hungary = False
# hungary = True
# if hungary:
#    print("Feeed me")
# else:
#    print("NOT Hungary")


"""loc = 'Auto'

if loc == "Auto Shop":
    print('Cars are cool')
elif loc == 'Bank':
    print("get ur money")
elif loc == 'Store':
    print("Get ur stuff")
else:
    print("I do not know much")"""

"""mystring = 'Sammy'

for i in mystring:
    if i == 'a':
        break
    print(i)"""

'''x = 0
while x < 5:
    if x == 2:
        # pass
        break
        # continue
    print(x)
    x += 1'''

# for num in range(0,11,3):
#    print(num)

# print(list(range(0,11,2)))

'''index_count = 0

for letter in 'abcdef':
    print("At Index {} the letter is {}".format(index_count, letter))
    index_count += 1'''

'''word = 'abcdf'

for item in enumerate(word):
    print(item)

for index, letter in enumerate(word):
    print(letter, index)'''

'''my_list1 = [1, 2, 3, 5, 6]
my_list2 = ['a', 'b', 'c']
my_list3 = [100, 200, 300]

for item in zip(my_list1, my_list2, my_list3):
    print(item)'''

'''
print('i' not in [1, 2, 3, 'i'])

print('a' in 'this is a car')

print('mykey' in {'mykey': 345})

d = {'mykey': 345}
print(345 in d.values())
print(345 in d.keys())'''

# mylist = [10, 20, 40, 22, 55, 33, 221, 321, 0]
# print(min(mylist))
# print(max(mylist))

# from random import shuffle

# my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# shuffle(my_list)
# print(my_list)

# from random import randint

# print(randint(0, 101))

'''
mystr = 'hello'
my_list = []

for letter in mystr:
    my_list.append(letter)

print(my_list)'''


# mystr = 'hello'
# my_list = [letter for letter in mystr]
# print(my_list)


# my_list = [x for x in "I love India"]
# print(my_list)

# my_list = [num**2 for num in range(0,11)]
# print(my_list)

# my_list = [x for x in range(0, 11) if x % 2 == 0]
# print(my_list)

'''
celcius = [0, 10, 20, 34.5]
# fahrenheit = [((9/5)*temp+32) for temp in celcius]
# print(fahrenheit)

fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9/5)*temp+32))

print(fahrenheit)'''

# results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
# print(results)
'''
my_list = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        my_list.append(x*y)
print(my_list)

my_list = [x*y for x in [2,4,6] for y in [1,10,1000]]
print("new list: ", my_list)'''

'''
# use for, .split() and if to create statement
# Print only the words that starts with s in this sentence
st = "Print only the words that starts with s in this sentence\
    this added Sentence by Ashish to Study"
words = st.split()
for i in words:
    if i[0] == 's' or i[0] == 'S':
        print(i)'''
'''
# for i in range(0,11,2):
#    print(i)

ll = []
for i in range(0, 51):
    if i % 3 == 0:
        ll.append(i)

print(ll)'''

'''
# Print  word if lenght of word is even print "even"
st = "Print only the words that starts with s in this sentence\
    this added Sentence by Ashish to Study"
word = st.split()

for i in word:
    if (len(i) % 2 == 0):
        print("even")
'''

'''
def save(name="Singh"):

    print("hi, ", name)


save('aaa')'''

'''
def add_num(num1, num2):
    return num1 + num2
    # print(num1+num2)


result = add_num('2', '20')
print(result)'''

'''
# rETURN true IF ANY NUMBER IS EVEN INSIDE A LIST
def even_check_list(num_list):

    even_num = []

    for num in num_list:
        if num % 2 == 0:
            even_num.append(num)
        else:
            pass
    return even_num


num_list = [1, 1, 2, 50]
print(even_check_list(num_list))'''


# stock_prices = {('APPEL', 200), ('GOOGLE', 400), ('MSFT', 100)}

# for item in stock_prices:
#    print(item)

# for tikcer, price in stock_prices:
#    print(price+(0.2*price))

'''
work_hours = [('Abay', 0), ('Billy', 4.0), ('Ashu', 10.2)]


def employee_check(work_hours):

    current_max = 0
    employee__of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee__of_month = employee

    # Return Employee of the month
    return (employee__of_month, current_max)


print(employee_check(work_hours))'''


# example = [1, 2, 3, 4, 5, 6, 7]

# from random import shuffle

'''
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


print(shuffle_list(my_list))


def player_guess():

    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input('Pick a number: 0, 1 or 2:> ')

    return int(guess)


def check_guess(my_list, guess):
    if my_list[guess] == '0':
        print(guess)
        print(mixedup_list)
        return "Correct"
    else:
        print(guess)
        print(mixedup_list)
        return "Wrong guess!!"


# Initial list
my_list = [' ', '0', ' ']

# Shuffle List
mixedup_list = shuffle_list(my_list)


# User Guess
guess = player_guess()

# Check Guess
print(check_guess(mixedup_list, guess))
'''

'''
# LESSER OF TWO EVENS: Write a function that returns the
# lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd


def lesser_of_two_evens(a, b):
    if a < b:
        return a
    elif b < a:
        return b
    else:
        return "Both are equal"


print(lesser_of_two_evens(12, 12))'''


'''
# Define a function called myfunc that takes in a Boolean
# value (True or False). If True, return 'Hello', and if
# False, return 'Goodbye'

# Remember, don't run the function, simply provide the definition

def myfunc(a):
    if a == True:
        return 'Hello'
    elif a == False:
        return 'Goodbye'


print(myfunc(True))'''

'''
# using Booleans
# Define a function called myfunc that takes three arguments, x, y and z.
# If z is True, return x.  If z is False, return y.

def myfunc(x, y, z):
    if z is True:
        return x
    else:
        return y


print(myfunc(True, 'Goodbye', 'a'))'''
