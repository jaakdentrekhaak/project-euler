# Project Euler Problem 6
# Author: Jens Putzeys
# Date: 05-09-2019


def sum_of_squares(num):
	cur_sum = 0
	for i in range(1, num + 1):
		cur_sum += i ** 2
	return cur_sum

assert sum_of_squares(10) == 385

def square_of_sums(num):
	cur_sum = 0
	for i in range(1, num + 1):
		cur_sum += i
	result = cur_sum ** 2
	return result

assert square_of_sums(10) == 3025

print(square_of_sums(100) - sum_of_squares(100))