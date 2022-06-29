"""
File: caesar.py
Name: AO Chuang
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""

# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Input.
    secret_num: int, the number of the alphabet to be shifted
    cipher: str, the string been ciphered

    Output.
    new_alp: str, the string that is deciphered
    _
    Example 1,
    secret_num = 4
    cipher = WLLHA
    the answer will be 'APPLE'

    Example 2,
    secret_num = 7
    copher = RHN TKX MAX UXLM!
    the answer will be 'YOU ARE THE BEST'
    """
    secret_num = int(input('Secret: '))
    cipher = input("What's the ciphered string: ")
    new_alp = create_alp(secret_num)
    find_ans(new_alp, cipher)


def create_alp(secret_num):
    """
    This function will create a new ALPHABET depends on the secret_num.
    Return:
        new_alp: str, a new ALPHABET that has been shifted.
    """
    new_alp = ''
    new_alp += ALPHABET[len(ALPHABET)-secret_num:len(ALPHABET)]
    new_alp += ALPHABET[0:len(ALPHABET)-secret_num]
    return new_alp


def find_ans(new_alp, cipher):
    """
    This function will find the answer of Caesar Cipher, and print it.
    """
    for i in range(len(cipher)):
        for j in range(len(new_alp)):
            if cipher[i] == new_alp[j]:
                print(ALPHABET[j], end='')


if __name__ == '__main__':
    main()
