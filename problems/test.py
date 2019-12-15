import math
import numpy as np

def is_prime(num):
    if num < 2: return False
    max_divisor = int(math.sqrt(num))

    return all(num % i != 0 for i in range(2, max_divisor+1))

def primes(U):
    sieve = np.full(U, True, dtype=bool)
    sieve[0] = sieve[1] = False

    for i in range(U):
        if not sieve[i]: continue
        sieve[i*i::i] = False
        yield i

if __name__ == '__main__':
    print(math.sqrt(600851475143))


