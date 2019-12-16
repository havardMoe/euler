import math
import numpy as np


def sieve_primes(U):
    sieve = np.full(U, True, dtype=bool)
    sieve[0] = sieve[1] = False

    for i in range(U):
        if not sieve[i]: continue
        sieve[i*i::i] = False
        yield i


if __name__ == '__main__':
    print(math.sqrt(600851475143))


