'''
# OLD MACDONALD: Write a function that capitalizes the first
# and fourth letters of a name

def old_macdonald(name):
    p1 = name[0:3].capitalize()
    p2 = name[3:].capitalize()
    return p1+p2


print(old_macdonald('macdonald'))'''


'''
# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(name):
    name = name.split()
    name = name[::-1]

    # now converting list to string
    name = ' '.join(name)
    print(name)

    # print(" ".join(name.split()[::-1]))


master_yoda('I am home')
master_yoda('We are ready')
'''

'''
# Given a list of ints, return True if the array contains
# a 3 next to a 3 somewhere.

def has_33(num):
    for i in range(0, len(num) - 1):
        if num[i] == 3 and num[i+1] == 3:
            return True
    else:
        return False


print(has_33([3, 1, 1]))
print(has_33([3, 3, 0]))
print(has_33([3, 0, 3]))'''

'''
# ALMOST THERE: Given an integer n, return True if
# n is within 10 of either 100 or 200

def almost_there(num):
    if num in range(90, 111):
        return ("in range of 100s")
    elif num in range(190, 211):
        return ("in range of 200s")
    else:
        return ("{}... is not in 10s range of 100 or 200".format(num))


print(almost_there(111))'''

"""
# PAPER DOLL: Given a string, return a string where for
# every character in the original there are three characters

def paper_doll(mystring):
    '''
    # using list & string
    mylist = []
    for i in mystring:
        mylist.append(i*3)
    op = ''.join(mylist)
    return op'''

    # using string only
    new = ' '
    for i in mystring:
        new = new + (i*3)
    return new


print(paper_doll("Mississippi"))"""

'''
def blackjack(a, b, c):

    if sum((a, b, c)) <= 21:
        return sum((a, b, c))
    elif sum((a, b, c)) <= 31 and 11 in (a, b, c):
        return sum((a, b, c)) - 10
    else:
        return 'BUST'


print(blackjack(1, 2, 3))'''


# tick tak toe game

