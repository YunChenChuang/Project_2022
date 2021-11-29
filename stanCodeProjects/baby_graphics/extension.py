"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:

        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        ##################
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        targets = soup.find_all('table', {'class:', 't-stripe'})
        male_test = 0
        male = 0
        female_test = 0
        female = 0
        for target in targets:
            top_name_lst = target.tbody.text.split()
            for text in top_name_lst:
                if str(text[0]).isdigit():
                    number_lst = text.split(',')

                    if len(number_lst) <= 1:
                        pass
                    else:
                        number = 0

                        for i in range(len(number_lst)):
                            if i != len(number_lst)-1:
                                number += int(number_lst[i]) * (len(number_lst) - i - 1) * 1000
                            else:
                                number += int(number_lst[i])

                        if male_test == 0:
                            male += int(number)
                            male_test = 1
                            female_test = 1
                        elif female_test == 1:
                            female += int(number)
                            male_test = 0
                            female_test = 0

        print('---------------------------')
        print(year)
        print(f'Male Number: {male}')
        print(f'Female Number: {female}')

        ##################


if __name__ == '__main__':
    main()
