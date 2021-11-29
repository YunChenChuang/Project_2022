"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	# input_data = input_test()
	# print('input_data: ', input_data)
	input_data = {0: ['f', 'y', 'c', 'l'],
				  1: ['i', 'o', 'm', 'g'],
				  2: ['o', 'r', 'i', 'l'],
				  3: ['h', 'j', 'h', 'u']}
	dictionary = read_dictionary()

	start = time.time()
	####################
	find_match(input_data, dictionary)

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def input_test():
	"""
	:return input_data: (dic)
			key : (int) row number, from 0 to 3
			value: (lst) single alphabet, e.g. ['a', 'b', 'f', 's']
	"""
	input_data = {}
	for i in range(4):  # from 0 to 3, 4 times
		in_str = input(f'{i+1} row of letters: ')
		in_str = in_str.lower()  # case insensitive

		# legal test
		test = 0
		if 8 >= len(in_str) >= 7:

			test = 1

			if str(in_str[1]) == ' ' and str(in_str[3]) == ' ' and str(in_str[5]) == ' ':
				test += 1

				alp1, alp2, alp3, alp4 = in_str.split()

				# alphabet legal test
				if alp1.isalpha() and len(alp1) == 1:
					test += 1
					if alp2.isalpha() and len(alp2) == 1:
						test += 1
						if alp3.isalpha() and len(alp3) == 1:
							test += 1
							if alp4.isalpha() and len(alp4) == 1:
								test += 1
								input_data[i] = in_str.split()

		if test < 6:  # test == 6, legal input; else, illegal input
			print('Illegal Input')
			return False

	return input_data


def find_match(input_data, dictionary):

	ele_d = {}
	match_lst = []
	for i in range(len(input_data)):  # i = -1, 0 , 1
		for j in range(len(input_data[0])):
			create_element_dict(input_data, i, j, ele_d)

	for ele in ele_d:
		coordinate_lst = []
		find_match_helper(ele_d, ele, '', 0, coordinate_lst, dictionary, match_lst)

	print(f'There are {len(match_lst)} words in total')


def find_match_helper(d, cur, current_s, match_num, coordinate_lst, dictionary, match_lst):

	if len(current_s) >= 4:
		if current_s not in match_lst:
			if current_s in dictionary[current_s[:2]]:
				print(f'FOUND {current_s}')
				match_lst.append(current_s)
				# match_coor.append(coordinate_lst[-len(current_s)])
				match_num += 1

	for coordinate in d[cur]:
		if coordinate in coordinate_lst:
			pass
		elif len(current_s) >= 2 and current_s[:2] not in dictionary:
			current_s = ''
			pass
		else:
			if len(current_s) >= 4 and current_s not in dictionary[current_s[:2]]:
				current_s = ''
				pass
			else:
				# choose
				cur = coordinate
				current_s += d[coordinate][coordinate]
				coordinate_lst.append(coordinate)

				# explore
				if len(current_s) < 2:
					match_num = find_match_helper(d, cur, current_s, match_num, coordinate_lst, dictionary, match_lst)
				elif (len(current_s) >= 2) and (current_s[:2] in dictionary) and (len(current_s) <= 16):
					match_num = find_match_helper(d, cur, current_s, match_num, coordinate_lst, dictionary, match_lst)

				# un-choose
				current_s = current_s[0:len(current_s)-1]
				coordinate_lst.pop()

	return match_num


def create_element_dict(input_data, i, j, ele_d):
	ele = input_data[i][j]
	ele_d[f'{i}{j}'] = {}
	ele_d[f'{i}{j}'][f'{i}{j}'] = ele
	if i - 1 >= 0:
		if j - 1 >= 0:
			ele_d[f'{i}{j}'][f'{i-1}{j-1}'] = input_data[i - 1][j - 1]
		ele_d[f'{i}{j}'][f'{i-1}{j}'] = input_data[i - 1][j]
		if j + 1 < len(input_data):
			ele_d[f'{i}{j}'][f'{i-1}{j+1}'] = input_data[i - 1][j + 1]

	if j - 1 >= 0:
		ele_d[f'{i}{j}'][f'{i}{j-1}'] = input_data[i][j - 1]
	if j + 1 < len(input_data[0]):
		ele_d[f'{i}{j}'][f'{i}{j+1}'] = input_data[i][j + 1]

	if i + 1 < len(input_data):
		if j - 1 >= 0:
			ele_d[f'{i}{j}'][f'{i+1}{j-1}'] = input_data[i + 1][j - 1]
		ele_d[f'{i}{j}'][f'{i+1}{j}'] = input_data[i + 1][j]
		if j + 1 < len(input_data):
			ele_d[f'{i}{j}'][f'{i+1}{j+1}'] = input_data[i + 1][j + 1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	:return dictionary: (dic) collection of word in FILE that len(word) >= 4
						key: (str) first 2 alphabet of word in value
						value: (lst) words start with [key]  e.g. ['ve'] : ['veal', 'vealed', 'vealer', ...]
	"""
	dictionary = {}
	with open(FILE, 'r') as f:

		for line in f:
			if len(line) >= 4:
				word = line.strip()
				first_alp = word[0:2]

				if first_alp in dictionary:
					dictionary[first_alp].append(word)
				else:
					word_lst = [word]
					dictionary[first_alp] = word_lst

	return dictionary


if __name__ == '__main__':
	main()
