"""
File: coin_flip_runs.py
Name: AO Chuang
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random


def main():
    """
    Input:
        num_run: int, goal of the number to be runs.
    Output:
        The result of random flip, which has reach the goal that entered by users.

    Example 1:
        num_run = 2
        Result: 'THHTHH', which has 2 runs 'HH' & 'HH'.

    Example 2:
        num_run = 4
        Result: "HTTTTTTHHHTTHH" , which has 4 runs 'TTTTTT' & 'HHH' & 'TT' & 'HH'.
    """
    print(f"Let's flip a coin!")
    num_run = int(input('Number of runs: '))

    flip_str = random_flip()
    first_same = False
    count = 0

    while count < num_run:
        flip = random_flip()
        if flip_str[-1] == flip:
            if not first_same:
                count += 1
                first_same = True
        else:
            first_same = False
        flip_str += flip

    print(flip_str)


def random_flip():
    """
    Create the random result of flip.
    :return: str, flip result 'H' or 'T'
    """
    num = random.choice(range(2))
    return 'T' if num else 'H'


if __name__ == "__main__":
    main()
