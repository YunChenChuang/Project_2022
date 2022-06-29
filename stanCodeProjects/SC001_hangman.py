"""
File: hangman.py
Name: AO Chuang
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

N_TURNS = 7  # This constant controls the number of guess the player has.


def main():
    """
    Input,
    input_ch: str, len(input_ch) == 1, the character guessed by users.
    """
    # ans = random_word()
    ans = 'HOSPITALITY'
    dash_str = ''
    lives = N_TURNS
    for i in range(len(ans)):
        dash_str += '-'

    while True:
        print()
        print(f'The word looks like {dash_str}')
        print(f'You have {lives} wrong to left')
        input_ch = input(f'Your guess: ').upper()

        # if input_ch is not alphabet or more than 1 character were entered --> Illegal Format
        if not input_ch.isalpha() or len(input_ch) != 1:
            print('Illegal format.')
        else:
            # Wrong input
            if input_ch not in ans:
                print(f"There's no {input_ch}'s in the word.")
                lives -= 1
            # Right input
            else:
                dash_str = replace(dash_str, input_ch, ans)
                print('You are correct!')

        # there's NO LIVES left, which is 'GAME OVER'.
        if lives == 0:
            print('__________________________')
            print('You are completely hung :(')
            break
        # the string to be guessed is same as the answer, which is 'You Win!'
        elif dash_str == ans:
            print('__________________________')
            print('You WIN!')
            break

    print(f'The word was {ans}')


def replace(last_guess, input_ch, ans):
    blank_str = ''
    for i in range(len(ans)):
        if ans[i] == input_ch:
            blank_str += input_ch
        else:
            blank_str += last_guess[i]
    return blank_str


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()
