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
	This program can create the random flip result,
	and stop when the given continue number of flips was reached
	"""
	print("Let's flip a coin!")
	num_run = int(input('Number of runs: '))  # int

	num_continue = 0  # counting the number of continue in the random flips
	str_flips = ''  # record the all the flip results
	prior = ''  # record the prior result
	same = 0  # counting the number of the continue flip result

	while True:

		if num_continue == num_run:  # finishing the loop when the goal number was reached
			break
		else:
			flip = random_flip()  # 'flip' is the random result of flips
			str_flips += flip  # record all the result of flip
			if prior == flip:  # record as 'same' whe 'flip' == 'prior'
				same += 1
			else:
				same = 0  # clean 'same'
			if same == 1:  # record as continue only when 'same' == 1
				num_continue += 1
			prior = flip  # update 'prior'

	print(str_flips)


def random_flip():
	"""
	Creating the random result of flip
	:return: str, the flip result 'T' or 'H'
	"""
	num = random.choice(range(2))
	if num == 0:
		return 'T'
	elif num == 1:
		return 'H'


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
