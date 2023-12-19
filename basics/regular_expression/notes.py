# Find phone number (US/UK)


import re


def is_phone_nu(p_string):
    if len(p_string) != 12:
        # Not phone nu as not 12 numbers including -
        return False
    for i in range(0, 3):
        if not p_string[i].isdecimal():
            # area code is missing
            return False
    if p_string[3] != '-':
        # missing first - dash
        return False
    for i in range(4, 7):
        if not p_string[i].isdecimal():
            # missing first digits
            return False
    if p_string[7] != '-':
        # missing 2nd - dash
        return False
    for i in range(8, 12):
        if not p_string[i].isdecimal():
            # missing last digits
            return False
    return True


print(is_phone_nu('222-333-1234'))
print(is_phone_nu('2022-333-1234'))
print(is_phone_nu('a22-333-1234'))

text = "this is my phone number: 222-333-1234 and office is: 444-555-4321"

for i in range(len(text)):
    text_piece = text[i:i+12]
    if is_phone_nu(text_piece):
        print(text_piece)
        is_number = True
if not is_number:
    print("There is not any phone number in given text.")

###############################
# Using Regular expressions
# import re

text = "this is my phone number: 222-333-1234 and office is: 444-555-4321"

"""match_objetc = re.search('\d\d\d-\d\d\d-\d\d\d\d', text)


if match_objetc is None:
    # if match_objetc == None:
    #  for None as per best practices use "is" operator like above example
    print("There is no Object")
else:
    print(match_objetc.group())"""


match_objetc = re.findall('\d\d\d-\d\d\d-\d\d\d\d', text)
print(match_objetc)


############################################
"""Find Three Consecutive Digits
Implement a function which takes a string as a parameter
to find out whether there is three consecutive digits or
not. If there is three consecutive digits, the function
will return first occurence otherwise 'Not found'."""

# import re
text = 'My phone number is: 234-45a6-8765'


def find_three_con(p_text):
    data = re.search('\d\d\d', p_text)

    try:
        data = data[0]
        if data.isdigit():
            return data
        else:
            return "Not found"
    except TypeError:
        return "Try Except BLOCK TypeError"


print(find_three_con(text))
############################################
"""Find Three Consecutive Digits
Implement a function which takes a string as a parameter
to find out whether there is three consecutive digits or
not. If there is three consecutive digits, the function
will return first occurence otherwise 'Not found'."""

# import re
text = 'My phone number is: 234-45a6-8765'


def find_three_con(p_text):
    data = re.search('\d\d\d', p_text)
    if data is None:
        return "Not found"
    else:
        return data.group()


print(find_three_con(text))

############################################
# Using Regular expressions
# ^$\?
# import re

"""phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d)')
mo = phone_num_regex.search("This is my number: 111-222-3456")

print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))

print("\n\n\n")
# (111) 666-7777
phone_num_regex = re.compile(r'\(\d\d\d\) (\d\d\d)-(\d\d\d)')
mo = phone_num_regex.search("This is my number: (111) 222-3456")

print(mo.group(0))"""


# Pipe charater looks for alternative

dis_regres = re.compile(r'dis(agree|allow|array|connect)')

text = "I disagree with this statement. disconnect and disallow"
print(dis_regres.search(text))

############################################
# Using Regular expressions
# ^$\?
# import re

"""phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d)')
mo = phone_num_regex.search("This is my number: 111-222-3456")

print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))

print("\n\n\n")
# (111) 666-7777
phone_num_regex = re.compile(r'\(\d\d\d\) (\d\d\d)-(\d\d\d)')
mo = phone_num_regex.search("This is my number: (111) 222-3456")

print(mo.group(0))"""


# Pipe charater

"""dis_regres = re.compile(r'dis(agree|allow|array|connect)')

text = "I disagree with this statement. disconnect and disallow"
print(dis_regres.search(text))
"""

# Repetition methacharacters
# * + ? {}

# ? methacharacters__ match zero or one time only
# import re

"""regex = re.compile(r'ba?na?na')
mo = regex.search("baaanna")
print(mo)"""

"""# ? methacharacters using () group
# iron_man = re.compile(r"ironman|ironwomen")
iron_man = re.compile(r"iron(wo)?man")
# mo = iron_man.search("ironman")
mo = iron_man.search("ironwoman")
print(mo)
print(mo.group())
"""


"""phone_num_regex = re.compile(r'(\d\d\d)? (\d\d\d)-(\d\d\d)')
mo = phone_num_regex.search("This is my number: 222-345")

print(mo.group())"""


"""quest_regex = re.compile(r'drink\?')
mo = quest_regex.search("Do you want to drink?")
print(mo)
print(mo.group())"""

#########################
"""# * start methacharacters__ match zero or mone
regex = re.compile(r'foo-*bar')
# mo = regex.search("foobar")
# mo = regex.search("foo----bar")
mo = regex.search("foo---bar")
print(mo)
print(mo.group())

# iron_man = re.compile(r"iron(wo)?man")
iron_man = re.compile(r"iron(wo)*man")
mo = iron_man.search("ironwowowoman")
print(mo)
print(mo.group())"""

#########################
# + plus methacharacters__ match one or mone repetitions

regex = re.compile(r'foo-+bar')
mo = regex.search("foo-----bar")
# print(mo)
# print(mo.group())

# iron_man = re.compile(r"iron(wo)?man")
iron_man = re.compile(r"iron(wo)+man")
mo = iron_man.search("ironwowowoman")
# print(mo)
# print(mo.group())


#########################
# {} methacharacters__ matchgiven number repetitions
regex = re.compile(r'foo-{1}bar')
mo = regex.search("foo-bar")

regex = re.compile(r'foo-{3}bar')
mo = regex.search("foo---bar")

regex = re.compile(r'fooA{3}bar')
mo = regex.search("fooAAAbar")

regex = re.compile(r'foo-{2,5}bar')
mo = regex.search("foo-----bar")

regex = re.compile(r'foo-{,}bar')
mo = regex.search("foo-------bar")


phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phone_num_regex.search("This is my number: 111-222-3456, 333-444-1234")

phone_num_regex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phone_num_regex.search(
    "This is my number: 111-222-3456,333-444-1234,777-888-1234")


phone_num_regex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phone_num_regex.search(
    "This is my number: 111-222-3456,444-1234,777-888-1234")

print(mo)
print(mo.group())

############################################
"""Repetition EX1
Write a Python function that matches a string that
has an 'A' followed by zero or more 'B's."""

# import re

mo = re.compile(r'AB*(BC)?')


def text_match(p_match):
    result = mo.search(p_match)
    if result is not None:
        output = result.group()
        return "Matched", output


print(text_match("A"))
print(text_match("ABC"))
print(text_match("ABBC"))


############################################
# import re

mo = re.compile(r'AB{2,3}')


def text_match(p_match):
    result = mo.search(p_match)
    if result is not None:
        return "Matched"
    else:
        return "Not Matched"


print(text_match("A"))
print(text_match("ABC"))
print(text_match("ABBC"))

############################################
"""Repetition EX3
Write a Python function that matches given words in the text and count them."""

# import re

text = """Lovers in love
Love, love, love, love, love
Love, love, love, love, love
Love, love, love, love, love
Love, love, love, love, love
Lovers loving love just like these lovers are loving love in love
Lovers loving love just like these lovers are loving love in love"""

# Words: "Love, love, Lovers, lovers"


def text_match(p_text):
    # Pipe charater looks for alternative
    regex = re.compile(r'(L|l)ove(rs)?')
    list_text = p_text.split()
    count = 0
    for word in list_text:
        mo = regex.search(word)
        if mo is not None:
            count += 1
    return count


print(text_match(text))


"""
def text_match(p_text):
    # Pipe charater looks for alternative
    regex = re.compile(r'(L|l)ove(rs)?')
    mo_list = regex.findall(p_text)
    return len(mo_list)


print(text_match(text))
"""
############################################
# regex Greedy and Non Greedy matches

# regex Greedy

# import re

regex = re.compile('a?')
mo = regex.search('aaaa')
# print(mo)

regex = re.compile('a?')
mo = regex.findall('aaaa')
# print(mo)

regex = re.compile('a*')
mo = regex.search('aaaa')
# print(mo)

regex = re.compile('a+')
mo = regex.search('aaaa')
# print(mo)

regex = re.compile('a{1,3}')
mo = regex.search('aaaaaa')
# print(mo)

regex = re.compile('a?')
mo = regex.search('aaaaaa')
# print(mo)

# regex Non Greedy matches
regex = re.compile('a*')  # Greedy
mo = regex.findall('aaaaaa')
# print(mo)

# regex Non Greedy matches
regex = re.compile('a*?')  # Non-Greedy
mo = regex.findall('aaaaaa')
# print(mo)


# regex Greedy matches
digit_regex = re.compile(r'(\d){2,6}')  # greedy approach
mo = digit_regex.search('12345679')
# print(mo)


# regex Non- Greedy matches
digit_regex = re.compile(r'(\d){2,6}?')  # Non-greedy approach
mo = digit_regex.search('12345679')
# print(mo)


################
# Charater Class

phone_regrex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# phone_regrex = re.compile(r'(0|1|2|3|4|5|6|7|8|9)')

mo = phone_regrex.search('111-222-1234')
# print(mo)

phone_regrex = re.compile(r'\d')
mo = phone_regrex.search('abssjk3kkd')
# print(mo)


phone_regrex = re.compile(r'\w')
mo = phone_regrex.search('#!@#.,abssjk3kkd')
# print(mo)

phone_regrex = re.compile(r'\w')
mo = phone_regrex.findall('#!@#.,abssjk3kkd')
# print(mo)


phone_regrex = re.compile(r'\W')
mo = phone_regrex.findall('#!@#.,abssjk3kkd')
# print(mo)

phone_regrex = re.compile(r'\s')
mo = phone_regrex.search('#!@#.,ab ssjk3   kkd \t')
# print(mo)


phone_regrex = re.compile(r'\S')
mo = phone_regrex.search('#!@#.,ab ssjk3   kkd \t')
# print(mo)


text = '''The use of 1234 to say "I Love You" comes from
the followig idea: I have 1 thing 2 say:: 3 words 4 you'''

regex = re.compile(r'\d+\s\w+')
mo = regex.findall(text)
print(mo)

############################################
"""Implement regular expression pattern which finds the
numbers starting with 3."""

text = """What’s New In Python 3.10
Release 3.10.1
Date January 10, 2022
Editor Pablo Galindo Salgado
This article explains the new features in Python 3.10, compared to 3.9."""

# import re

regex = re.compile(r'3\S+')
mo = regex.findall(text)
print(mo)

############################################
"""Implement a function which extracts year, month and
date from an url by using regular expression pattern."""

# import re

url = """https://www.apmillers.com/news/daily/
wp/2022/02/02/regular-expressions-patterns/"""


def extract_date(url):
    regex = re.compile(r'(\d{4})/(\d{1,2})/(\d){1,2}')
    mo = regex.findall(url)
    return mo


print(extract_date(url))
############################################
"""Implement regular expression pattern which finds the
numbers starting with 3."""

# import re
text = """What’s New In Python 3.10
Release 3.10.1
Date January 10, 2022
Editor Pablo Galindo Salgado
This article explains the new features in Python 3.10, compared to 3.9."""


regex = re.compile(r'3\S+')
mo = regex.findall(text)
print(mo)

############################################
# Custom Character Classes

# r'[]'

# import re

regex_oject = re.compile(r'ba[artz]')
mo = regex_oject.search('foorbarqtux')
# print(mo)

vowel_regex = re.compile(r'[aeiou]')

lowercase_regex = re.compile(r'[a-z]')

mo = lowercase_regex.search('foorbarqtux')
# print(mo)

lower_and_upper_case_regex = re.compile(r'[a-zA-Z]')
# mo = lower_and_upper_case_regex.search('AScdafoorbarqtux')
# print(mo)

mo = lower_and_upper_case_regex.findall('AScdafoorbarqtux')
# print(mo)

vowel_regex = re.compile(r'[aeiouAEIOU]{2}')
mo = vowel_regex.findall('I like eat food ourside FOOD fOoD')
# print(mo)

# creating negitive case using ^
vowel_regex = re.compile(r'[^aeiouAEIOU]{2}')
mo = vowel_regex.findall('I like eat food ourside FOOD fOoD')
print(mo)

############################################
"""Implement regular expression pattern inside a function
to check that a string contains only a certain set of
characters (in this case a-z, A-Z and 0-9)"""

# import re


def check_char(p_input):
    regex = re.compile(r'[a-zA-Z0-9]')
    mo = regex.findall(p_input)
    return mo


print(check_char("ABCDEFabef1250"))
print(check_char("*&%@#{"))

############################################
"""Write a Python function to find all character combinations
starting with 'a' or 'e' in a given string."""

# import re


text = """The following example creates a list with 50 elements.
All elements are then added to the list when the list is created."""


def check_char(p_text):
    regex = re.compile(r'[ae]\w+')
    mo = regex.findall(p_text)
    return mo


print(check_char(text))

############################################
"""Write a Python function to tind the html tags that are more than 4 letters.

Html tags can be found inside <> characters and closing html tags can be found
in the same format after / character. </>
i.e.: <param> </param>"""


# import re
html_text = """html_text = "<html>
<head> <title>Page Title</title> </head>
<body>
<div class="tut-list tut-list-new tut-row ">
<div class="tut-list-primary"> <div class="tut-vote">
<video>intro</video>
<span class="count">50</span> <span class="tut-upvotes-text
hidden">Upvotes</span> </a> </div>
<center>k="11" rel="nofollow"></center>
<span class="tutorial-title-txt">The Complete Data Structures
and Algorithms Course in Python</span>
<span class="tut-title-link">  <span class="js-tutorial" data-id="3529"
title="The Complete Data Structures and Algorithms Course in Python"
target="_blank">(udemy.com)</span>
</span>  </a></div> <div class="action-footer">
<form class="save-tutorial-form" method="post" <button></button> </form>
</body>"""


def find_tag(html_text):
    regex = re.compile(r'<([a-z]{5,})>')
    mo = regex.findall(html_text)
    return mo


print(find_tag(html_text))

############################################
"""Implement regular expression pattern inside a function
to check that a string contains only a certain set of
characters (in this case a-z, A-Z and 0-9)"""

# import re


def check_char(p_input):
    regex = re.compile(r'[a-zA-Z0-9]')
    mo = regex.findall(p_input)
    return mo


print(check_char("ABCDEFabef1250"))
print(check_char("*&%@#{"))

############################################
# password check
while True:
    psw = input("Enter new password > ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) > 5:
        print("FINE")
    else:
        print("NOT OK")

############################################
"""Regex Pattern EX6
Write a Python function to find sequences of capital
letters joined with a underscore. If match is found it
returns Matched otherwise Not matched."""

# import re


def text_match(p_text):
    capital_letter = re.compile(r'^[A-Z]+_[A-Z]+$')
    mo = capital_letter.findall(p_text)
    if mo:
        return "Matched"
    else:
        return "Not matched."


print(text_match("BB_CCAA"))
print(text_match("aabb_DDDEFF"))
print(text_match("ADRGT_BCDEe"))

############################################
# import re

begin_hello_regex = re.compile(r'^Hello')
mo = begin_hello_regex.search('Hello there.')
# print(mo)

begin_hello_regex = re.compile(r'world$')
mo = begin_hello_regex.search('Hello world')
# print(mo)

all_digit_regex = re.compile(r'^\d+$')
mo = all_digit_regex.search('1231213415564')
# print(mo)


# using dot .
regex = re.compile(r'.ad')
mo = regex.findall('The lou you download to still is equal to the upload')
# print(mo)

regex = re.compile(r'.{1,7}ad')
mo = regex.findall('The lou you download to still is equal to the upload')
# print(mo)


# usin dot start .*
regex = re.compile(r'.*ad')
mo = regex.findall('The lou you download to still is equal to the upload')
# print(mo)

text = "Make: BMW Model: X5"
regex = re.compile(r'Make: (.*) Model: (.*)')
mo = regex.findall(text)
# print(mo)


# .* greedy
text = '<Hello world> Welcome!>'
regex = re.compile(r'<(.*)>')
mo1 = regex.search(text)
# print(mo1)


# .*  non greedy
text = '<Hello world> Welcome!>'
regex = re.compile(r'<(.*?)>')
mo2 = regex.search(text)
# print(mo2)


# .* new line
new_text = "I love Python.\n I am learning online."
regex = re.compile(r'.*', re.DOTALL)
mo = regex.search(new_text)
# print(mo)


# ignore case sensitive
# .* new line
new_text = "I love Python."
regex = re.compile(r'[aeiou]', re.IGNORECASE)
mo = regex.findall(new_text)
print(mo)

############################################
"""Write a Python function to extact the
email addresses from the given string."""

# import re
text = """From test@appmillers.com Wen Jan  5 09:14:16 2022
From info@appmillers.com Wen Jan  5 09:14:16 2022
From elshad@appmillers.com Wen Jan  5
From redy@appmillers.com Wen Jan  5
From info@appmillers.com Wen Jan  5 
from a9_ever@yahoo.co.in"""


def extract_email(p_text):
    match = re.findall(
        "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)
    return match


print(extract_email(text))

############################################
"""Write a Python function to match a string that has
a 'c' or 'C' followed by anything, ending in 'e' or 'E'.
If match is found it will return the list of matches."""

# import re


def text_match(p_text):
    capital_letter = re.compile(r'^c.+e$')
    mo = capital_letter.findall(p_text)
    if mo:
        return "Matched"
    else:
        return "Not matched."


print(text_match("cAsB_CCAA"))
print(text_match("cADRGT_BCDEe"))

############################################
"""Anchors
Implement a Python function which takes text as a parameter and return
the list of words which are three, four or five characters long."""

# import re


def find_words(text):
    regex = re.compile(r'\b\w{3,5}\b')
    result_list = regex.findall(text)
    return result_list


print(find_words("I like Python for Everyone course. It is the best one out."))

############################################
# Grouping constructs
# import re

# regex = re.compile(r'(ba[rz]){2,4}(qux)?')
# mo = regex.search('bazbarbaz')

# regex = re.compile(r'(foo(bar)?)+(\d\d\d)?')
# mo = regex.search('foofoobar')
# print(mo.groups())


regex = re.compile(r'(\w+),(\w+),(\w+)')
mo = regex.search('foo,que,bar')
print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(3))

print(mo.group(2, 3))

############################################
"""is Decimal
Implement a function which takes a parameter and checks for a decimal
with a precision of 1 or 2. If the number is decimal with a precision
of 1 or 2 it will return True otherwise False."""


# import re


def is_decimal(text):
    regex = re.compile(r'^[0-9]+\.[0-9]{1,2}$')
    mo = regex.search(text)
    return bool(mo)
    """if mo is None:
        return None
    else:
        return mo"""


print(is_decimal('123.11'))
print(is_decimal('123.1'))
print(is_decimal('123.123'))

############################################
# Backreferences <>
# import re

# regex = re.compile(r'(\w+),\1') # here \n means like same last pattern
# mo = regex.search('love,love')
# mo = regex.search('love,like')

# print(mo)


regex = re.compile(r'(\w+),(\w+),(\w+)')
mo = regex.search("foo,quux,bar")
# print(mo.groups())
print(mo.group(1))

############################################
# import re

"""Implement a Python function which takes as a parameter IP address,
removes leading zeros from it and returns it."""


def remove_zero(p_text):
    output = re.sub(r'\.[0]*', '.', p_text)
    return output


print(remove_zero("211.07.095.122"))
print(remove_zero("001.007.005.102"))
############################################
# re Module Functions
#   - Searching functions
#   - Substitution functions
#   - Utility functions

# import re

# - Searching functions
# re.search(<regex>, <string>, flags=0)

# mo = re.search(r'(\d+)', 'foo123baz')
# mo = re.search(r'[a-z]+', 'FOO123BAZ', re.I)
# print(mo)




# - Searching functions
# re.match(<regex>, <string>, flags=0)

# mo = re.match(r'[a-z]+', 'FOO123BAZ', re.I)
# mo = re.match(r'(\d+)', 'foo123baz')
# print(mo)




# - Searching functions
# re.fullmatch(<regex>, <string>, flags=0)

# mo = re.fullmatch(r'(\d+)', 'foo123baz')
# mo = re.fullmatch(r'(\d+)', '4353252323')
# print(mo)




# - Searching functions
# re.findall(<regex>, <string>, flags=0)

# mo = re.findall(r'(\w+)', 'foo123baz...asds...aaa')
# mo = re.fullmatch(r'(\d+)', '4353252323')
# print(mo)




# - Searching functions
# re.finditr(<regex>, <string>, flags=0)

# for i in re.finditer(r'(\w+)', 'foo123baz...asds...aaa'):
#    print(i)



# re Module Functions
#   - Substitution functions
# re.sub() - find and replce
# re.subn() - find and replace and display count
# re.sub(<rgex>, <repl>, <string>, count=0 flags=0)


# custom_string = 'foo.145.bar.987.baz'

# result_string = re.sub(r'\d+', '#', custom_string)
# result_string = re.sub(r'[a-z]+', '*', custom_string)

# print(result_string)



# re Module Functions
#   - Utility functions
# re.split
# re.split(<regex>, <string>, maxsplit=0, flags=0)

# result = re.split('\s*[,:/]\s*', "foo,bar :  text / python")
# result = re.split('(\s*[,:/]\s*)', "foo,bar :  text / python")

"""regex = r'(\s*[,:/]\s*)'
result = re.split(regex, "foo,bar :  text / python")
for i, s in enumerate(result):
    if not re.fullmatch(regex, s):
        result[i] = f'<{s}>'

result = ''.join(result)
print(result)


regex = r'(?:\s*[,:/]\s*)'
result = re.split(regex, "foo,bar :  text / python")

print(result)"""


# re.escape 
regex = r'foo^bar(baz)|qux'
result = re.match(re.escape(regex), 'foo^bar(baz)|qux')
print(result)

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################
