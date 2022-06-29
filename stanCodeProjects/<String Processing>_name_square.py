"""
File: name_sq.py
Name: AO Chuang
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    This program will turn the input sting into a square pattern
    * Notice, this program is Case-Sensitive, the output case will refer to input case.
    _
    Example 1, name = Jerry
    Output:
            Jerry
            e   r
            r   r
            r   e
            yrreJ

    Example 2, name = Dennis!!!
    Output:
            Dennis!!!
            e       !
            n       !
            n       s
            i       i
            s       n
            !       n
            !       e
            !!!sinneD
    """

    print('This program prints a nme in a square pattern!')
    name = input('Name: ')
    space_num = len(name) - 2
    space = ''

    # create a string with white space
    for i in range(space_num):
        space += ' '

    # create the final output
    for i in range(len(name)):
        if i == 0:
            print(name)
        elif i == len(name)-1:
            print(name[::-1])
        else:
            print(f'{name[i]}{space}{name[len(name)-i-1]}')


if __name__ == '__main__':
    main()
