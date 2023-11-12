# Cryptography with Python: Caesor Cipher (Shift num 1 or 2 or 3 to left
# like ABC Shift 1 bceom - BCD, Shift 2 ABC become CDE )

import string

albhabets = string.ascii_uppercase
alphabet = list(albhabets)
cipher_msg = input("Enter your message:\n").upper()
shift_number = int(input("Enter the shift number :\n"))


def decrypt(p_cipher_msg, p_shift_number):
    message = ""
    for char in p_cipher_msg:
        if char in alphabet:
            position = alphabet.index(char)
            old_position = position - p_shift_number
            while old_position < 0:
                old_position = old_position + 26
            letter = alphabet[old_position]
            message += letter
        else:
            message += letter
    return f"The decoded message is {message}"


print(decrypt(cipher_msg, shift_number))
