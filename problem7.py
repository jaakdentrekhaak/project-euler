# Project Euler Problem 7
# Author: Jens Putzeys
# Date: 05-09-2019


def is_prime_number(x):
	if x >= 2:
		for y in range(2, x):
			if not (x % y):
				return False
	else:
		return False
	return True


def prime_number(position):
	cur_num = 2
	cur_prime = 0
	while cur_prime < position:
		if is_prime_number(cur_num):
			cur_prime += 1
		cur_num += 1
	return cur_num - 1

assert prime_number(6) == 13

print(prime_number(10001))
