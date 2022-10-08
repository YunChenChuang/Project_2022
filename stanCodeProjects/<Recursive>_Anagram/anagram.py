"""
File: anagram.py
Name: YunChen Chuang
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

DIC = {}


def main():
    """
    TODO: Find out anagrams of input word from the give dictionary.
    """
    ####################
    read_dictionary()
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        s = input('Find Anagrams for: ')
        start = time.time()
        s = s.lower()

        if s == EXIT:
            break
        elif len(s) not in DIC:
            print(f'\"{s}\" has no anagram')
            break
        else:
            result = []
            print('Searching...')
            find_anagrams(s, result)
            print(f'{len(result)} anagrams :{result}')
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')
    ####################


def read_dictionary():
    """
    DIC :dic, {key_1 : value_1},
        key_1 : int, len(line), length of line
        value_2 : dic, {key_2 : value_2}
            key_2 : str, line[0:2], the first 2 letter of line
            value_2 : list, [1st line, 2nd line, 3rd line, ... ], list of lines
    :return:
    """
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            temp_dic = {}
            if len(line) in DIC:
                if line[0:2] in DIC[len(line)]:
                    temp_list = DIC[len(line)][line[0:2]]
                    temp_list.append(line)
                    DIC[len(line)][line[0:2]] = temp_list
                else:
                    temp_list = [line]
                    temp_dic[line[0:2]] = temp_list
                    DIC[len(line)][line[0:2]] = temp_list
            else:
                temp_list = [line]
                temp_dic[line[0:2]] = temp_list
                DIC[len(line)] = temp_dic


def find_anagrams(s, result, temp_str='', temp_index=[]):
    """
    :param s: '', this function will find out the permutation of 's'
    :param result:  [], store the anagrams of 's'
    :param temp_str:  '', 'temp_str' will store current permutation.
    :param temp_index: [], this function will search all the permutation of 's' by index,
                           this list will temporary store used indexes.
    :return: [], list of all permutations of 's'.
    """

    if len(temp_str) == len(s):
        if temp_str[0:2] in DIC[len(s)]:
            if temp_str in DIC[len(s)][temp_str[:2]]:
                if temp_str not in result:
                    print(f'Found: {temp_str}', end='\n\n')
                    print('Searching...')
                    return result.append(temp_str)

    else:
        for i in range(len(s)):
            if i not in temp_index:
                # CHOOSE
                temp_index.append(i)
                temp_str += s[i]

                # EXPLORE
                find_anagrams(s, result, temp_str, temp_index)

                # UNCHOOSE
                temp_index.pop()
                temp_str = temp_str[:-1]


if __name__ == '__main__':
    main()
