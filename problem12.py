# def nb_divisors(n):
#     current_nb = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             current_nb += 1
#     return current_nb

# solution on internet, because my version was really not efficient
import math

def divisors(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            number_of_factors += 2
        if i * i == n:
            number_of_factors -= 1
    return number_of_factors


i = 1
j = 1
max_len = 0
result = 0
while True:
    length = divisors(j)
    if length > max_len:
        max_len = length
        print(max_len)
    if length > 500:
        result = j
        break
    i += 1
    j += i
print(result)
