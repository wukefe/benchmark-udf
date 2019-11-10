import numpy as np
import time

def is_prime(n):
    if n <= 1:
        return 1
    i = 2
    while i < n:
        if i * i > n:
            break
        if n % i == 0:
            return 0
        i = i + 1
    return 1

for x in range(2, 20):
    print '%d ==> %d' % (x, is_prime(x))


