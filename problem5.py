# Project Euler Problem 5
# Author: Jens Putzeys
# Date: 06-09-2019


def evenly_divisible_by(num):
	cur_num = 0

	while True:
		if cur_num != 0 and all(cur_num % i == 0 for i in range(1, num + 1)):
			return cur_num
		else:
			cur_num += num

assert evenly_divisible_by(10) == 2520

print(evenly_divisible_by(20))
