"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
from itertools import product
import time
import math


def finding_primes():
    pass


def is_prime_v1(num):
    if num == 1:
        return False  # 1 is not a prime
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_prime_v2(num):
    if num == 1:
        return False  # 1 is not a prime
    max_divisor = math.floor(math.sqrt(num))
    for i in range(2, max_divisor+1):
        if num % i:
            return False
    return True

def is_prime_v3(num):
    if num < 2:
        return False  # no number under 2 is a prime


    max_divisor = math.floor(math.sqrt(num))
    for i in range(2, max_divisor+1):
        if num % i:
            return False
    return True


if __name__ == '__main__':
    t0 = time.time()
    for n in range(1, 50000):
        is_prime_v1(n)
    t1 = time.time()
    time_v1 = t1 - t0

    t0 = time.time()
    for n in range(1, 50000):
        is_prime_v2(n)
    t1 = time.time()
    time_v2 = t1 - t0
    print(f"time taken v1: {time_v1}\ntime taken v2: {time_v2}")
