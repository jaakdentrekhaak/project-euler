# Project Euler Problem 1
# Author: Jens Putzeys
# Date: 01-08-2019


import time
start = time.time()

l1 = []

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        l1.append(i)

answer = sum(l1)
print(answer)

end = time.time()
print('time =', end - start, 'seconds')
