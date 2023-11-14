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
