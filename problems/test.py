import math
import numpy as np


def sieve_primes(U=100_000_000):
    U += 1
    sieve = np.full(U, True, dtype=bool)
    sieve[0] = sieve[1] = False

    for i in range(U):
        if not sieve[i]: continue
        sieve[i*i::i] = False
        yield i


def faculty(n):
    if n == 0: return 0
    if n == 1: return 1
    return n * faculty(n-1)


if __name__ == '__main__':
    for prime in sieve_primes(7):
        print(prime)



