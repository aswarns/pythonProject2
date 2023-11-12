# Cryptography with Python: Caesor Cipher (Shift num 1 or 2 or 3 to left
# like ABC Shift 1 bceom - BCD, Shift 2 ABC become CDE )

import string

albhabets = string.ascii_uppercase
alphabet = list(albhabets)
message = input("Enter your message:\n").upper()
shift_number = int(input("Enter the shift number :\n"))


def encrypt(p_message, p_shift_number):
    cipher_msg = ""
    for char in p_message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + p_shift_number

            while new_position > 25:
                new_position = new_position - 26

            new_char = alphabet[new_position]
            cipher_msg += new_char
        else:
            cipher_msg += char
    return f"The encoded message is {cipher_msg}"


encoded_message = encrypt(message, shift_number)
print(encoded_message)
