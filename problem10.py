from math import sqrt
from itertools import count, islice


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


assert is_prime(19)

LIMIT = 2000000
sum = 0
i = 0
while i < LIMIT:
    if is_prime(i):
        sum += i
    i += 1

print(sum)
