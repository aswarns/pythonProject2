import re
from data import text

# Todo 1 - Create regex for Phone number
# 333-0000, 314-444-1234, (425) 456-2323, 111-0000 ext 12345, ext. 67883, x1274

phone_regex = re.compile(r'''(
                         ((\d\d\d)|(\(\d\d\d\)))?   # Aread Code Optional
                         (\s|-)?                    # First Seprator
                         \d\d\d                     # First 3 digit
                         -                          # Seprator
                         \d\d\d\d                   # last 4 digit
                         (\s((ext(\.)?\s)|x)(\d{2,5}))?
                         )''', re.VERBOSE)
# print(phone_regex.search('(807) 888-0000 x345'))


# Todo 2 - Create regrex for email
# some.+_thing@gmail.com
email_regex = re.compile("""
                        [a-zA-Z_.+]+        # Name Part
                        @                   # @ Symbol
                        [a-zA-Z_.+]+        # domain part
                         """, re.VERBOSE)
# print(email_regex.search('info@gmail.co.in'))
# print(email_regex.search('info_admin@gmail.co.in'))
# print(email_regex.search('info+admin@gmail.com'))


# Todo 3 - Extart phone number/email from text
extracted_phone_number = phone_regex.findall(text)
# print(extracted_phone_number)
all_phone_number = []
for phone_nu in extracted_phone_number:
    all_phone_number.append(phone_nu[0])
# print(all_phone_number)

extracted_emails = email_regex.findall(text)
print(extracted_emails)


# Todo 4 - Print Phone number and emails each on new line
results = '\n'.join(all_phone_number) + '\n'.join(extracted_emails)
print(results)
