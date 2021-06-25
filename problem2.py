# Project Euler Problem 2
# Author: Jens Putzeys
# Date: 01-08-2019


import time
start = time.time()

MAX = 4000000
total_sum = 0


def fibonacci(n):
    global total_sum

    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(500):
    fib = fibonacci(i)
    if fib <= MAX:
        print(fib)
        if fib % 2 == 0:
            total_sum += fib
    else:
        break

print('sum = ' + str(total_sum))

end = time.time()
print('time =', end - start, 'seconds')
