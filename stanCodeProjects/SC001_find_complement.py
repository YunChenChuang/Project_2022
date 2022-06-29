"""
File: complement.py
Name: AO Chaung
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Input.
    input_dna : str, a string composed with element 'A', 'T', 'C' ,and 'G'.
               which is case insensitive, you can enter in both upper case and lower case.
    Output.
    output_dna : str, a string composed with element 'A', 'T', 'C' ,and 'G'.
    _
    Example 1,
    input_dna = 'ATC', output_dna = 'TAG'

    Example 2,
    input_dna = 'ATCGta', output_dna = 'TAGCAT'
    """
    input_dna = input("Please give me a DNA strand and I'll find the complement: ")
    output_dna = build_complement(input_dna)
    print(f'The complement of {input_dna} is {output_dna}')


def build_complement(input_dna):
    """
    This function can find the complement string of 'input_dna',
    Letters 'A' and 'T' are complements to each other, and so are 'C' and 'G'.
    """
    input_dna = input_dna.upper()    # case insensitive
    output_dna = ''
    for ele in input_dna:
        if ele == 'A':
            output_dna += 'T'
        elif ele == 'T':
            output_dna += 'A'
        elif ele == 'C':
            output_dna += 'G'
        elif ele == 'G':
            output_dna += 'C'
    return output_dna


if __name__ == '__main__':
    main()