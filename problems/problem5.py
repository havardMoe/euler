"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import numpy as np
import time


# naive solution O(answer_number * max divisor)
def smallest_multiple_v1(divisor_max):
    divisor = 2
    number = 1
    while divisor <= divisor_max:
        if number % divisor == 0:
            divisor += 1
        else:
            number += 1
            divisor = 2
    return number


def sieve_primes(U):
    sieve = np.full(U, True, dtype=bool)
    sieve[0] = sieve[1] = False

    for i in range(U):
        if not sieve[i]: continue
        sieve[i*i::i] = False
        yield i


# def is_multiple(number, divisor_max):
#     for i in range(2, divisor_max+1):
#         if number % i != 0:
#             return False
#     return True

# same as above
def is_multiple(number, divisor_max):
    return all(number % i == 0 for i in range(2, divisor_max+1))


# runtime O(m + k)
# m: number of primes under the given div_max.
# k: number of times you have to add p0 to p.
def smallest_multiple(divisor_max):
    product = 1
    for prime in sieve_primes(divisor_max):  # knowing the lower bound of the answer has to be all the primes multiplied together
        product *= prime
    lower_bound = product

    while not is_multiple(product, divisor_max):
        product += lower_bound
    return product


if __name__ == '__main__':
    n = 20
    t0 = time.time()
    print(f"smallest_multiple_vi({n}): {smallest_multiple(n)}\n time taken for v2: {time.time()-t0}")


