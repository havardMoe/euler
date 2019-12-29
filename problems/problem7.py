"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
import numpy as np
import math


def sieve_primes(U=1_000_000):
    U += 1
    sieve = np.full(U, True, dtype=bool)
    sieve[0] = sieve[1] = False

    for i in range(U):
        if not sieve[i]: continue
        sieve[i*i::i] = False
        yield i


if __name__ == '__main__':
    n = 10001
    count = 1
    nth_prime = -1

    upper_bound = math.ceil((n * (math.log(n) + math.log(n)**2)))

    primes = sieve_primes(upper_bound)
    for n in range(n):
        nth_prime = next(primes)
    print(nth_prime)
