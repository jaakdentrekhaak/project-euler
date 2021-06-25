# Project Euler Problem 4
# Author: Jens Putzeys
# Date: 04-09-2019


def is_palindrome(number):
	number_string = str(number)
	for i in range(len(number_string)//2):
		if number_string[i] != number_string[-(i+1)]:
			return False
	return True

assert is_palindrome(707)
assert is_palindrome(840048)
assert not is_palindrome(123)


list_with_palindromes = []

def highest_palindrome():
	for i in range(0, 1000):
		for n in range(0, 1000):
			current_num = (999-i)*(999-n)
			if is_palindrome(current_num):
				list_with_palindromes.append(current_num)
	return max(list_with_palindromes)

print(highest_palindrome())