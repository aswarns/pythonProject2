# Cryptography with Python: Caesor Cipher (Shift num 1 or 2 or 3 to left
# like ABC Shift 1 bceom - BCD, Shift 2 ABC become CDE )

import string
from logo import logo


print(logo)

albhabets = string.ascii_uppercase
alphabet = list(albhabets)


def refactor_position(p_position, p_cipher_type):
    if p_cipher_type == "E":
        while p_position > 25:
            p_position = p_position - 26
    else:
        while p_position < 0:
            p_position = p_position + 26
    return p_position

def ceasor_cipher(p_positon, p_shift_number, p_cipher_type):
    final_text = ""
    if p_cipher_type == "D":
        p_shift_number *= -1
    for char in alphabet:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + p_shift_number
            new_position = refactor_position(new_position, p_cipher_type)
            final_text += albhabet[new_position]
        else:
            final_text += char
    print(f"Here si the {'decode' if p_cipher_type == "D" else 'encode'}d result: {final_text}")


end_program = False
while not end_program:
    enc_dec = input("Type 'E' to encrypt, type 'D' to decrypt:\n")
    message = input("Enter your message:\n").upper()
    shift_number = int(input("Enter the shift number :\n"))
    ceasor_cipher(message, shift_number, enc_dec)
    restart = input("Type 'Y' if you want to continue. Otherwise type 'N'\n")
    if restart == "N":
        end_program = True
        print("See you next time.")
