"""
File: similarity.py
Name: AO Chuang
----------------------------
It will compare short dna sequence, match_dna,
with sub sequences of a long dna sequence, search_dna
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program will compare the DNA sequence(search_dna) and the match DNA sequence(match_dna).
    And finding out the best match percentage, and the best match part of search_dna.
    _
    Example 1,
    search_dna: ACTGACATTG
    match_dna: TGCCA
    max_match_percentage: 80.0%
    ans: TGACA

    Example 2,
    search_dna: ATcgAtCGatCgC
    match_dna: tCgC
    max_match_percentage: 100.0%
    test_ans: TCGC
    """
    search_dna = input('Please give me a DNA sequence to search: ').upper()  # case insensitive
    match_dna = input('What DNA sequence would you like to match? ').upper()  # case insensitive

    max_match_num = 0
    max_match = ''

    for i in range(len(search_dna) - len(match_dna) + 1):
        test_dna = search_dna[i:len(match_dna)+i]
        match_num = 0
        for j in range(len(test_dna)):
            if test_dna[j] == match_dna[j]:
                match_num += 1

        if match_num > max_match_num:
            max_match_num = match_num
            max_match = test_dna

    print(f'The best match percentage is {(max_match_num/len(match_dna)*100)}%')
    print(f'The best match is {max_match}')


if __name__ == '__main__':
    main()
