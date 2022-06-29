"""
File: anagram.py
Name: AO Chuang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
DICTIONARY = {}
CURRENT_NUM = []


def main():
    """
    TODO:
    """
    read_dictionary()
    print(f'Welcome to stanCode "Anagram Generator" ( or {EXIT} to quit)')

    while True:
        word_to_find = input('Find Anagrams for: ')

        start = time.time()
        ####################
        if word_to_find == EXIT:
            break
        else:
            print('Searching...')
            found_word = find_anagrams(word_to_find)
            if len(found_word) == 0:
                print('NO ANAGRAM BEEN FOUND.')
            else:
                print(f'{len(found_word)} anagrams: {found_word}')

        ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:

        word_lst = []
        for line in f:

            word = line[:len(line)-1]
            first_alp = word[0:2]

            if first_alp in DICTIONARY:
                word_lst.append(word)
                DICTIONARY[first_alp] = word_lst
            else:
                word_lst = [word]
                DICTIONARY[first_alp] = word_lst


def find_anagrams(s):
    """
    :param s: str, the word to find anagrams
    :return found_word: lst, list of anagrams been found in dictionary
    """
    found_word = find_anagrams_helper(s, [], '', [])
    return found_word


def find_anagrams_helper(s, current_num, current_s, found_word):
    """
    :param s: str, the combination of letters to be anagrams
    :param current_num: lst, index of each alphabet
    :param current_s: str, current anagrams
    :param found_word: lst, list of anagrams been found in dictionary
    :return found_word: lst, list of anagrams been found in dictionary
    """
    if len(current_num) == len(s):
        if current_s[0:2] in DICTIONARY:
            if current_s in DICTIONARY[current_s[0:2]]:
                if current_s not in found_word:
                    print(f'Found : {current_s}')
                    found_word.append(current_s)
                    print('Searching...')

    else:
        for n in range(len(s)):

            if n in current_num:
                pass
            else:

                # choose
                current_s += s[n]
                current_num.append(n)

                # explore
                # if has_prefix(current_s):
                find_anagrams_helper(s, current_num, current_s, found_word)

                # un-choose
                current_s = current_s[0:len(current_s)-1]
                current_num.pop()

    return found_word


if __name__ == '__main__':
    main()
