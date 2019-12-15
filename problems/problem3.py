"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
from itertools import product


def get_primes(max_number=100):
    primes = []
    for i in range(2, max_number):
        prime = True
        for j in range(2, i//2):
            if i != j and i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    return primes


def largest_prime_factor():
    pass


if __name__ == '__main__':
    primes = get_primes(600851475143)
    print(primes)