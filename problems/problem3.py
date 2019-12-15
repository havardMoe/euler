"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import math

def finding_primes():
    pass


def is_prime(num):
    if num < 2: return False  # no number under 2 is a prime

    elif num == 2: return True  # 2 is the only even prime number

    elif num % 2 == 0: return False

    max_divisor = math.floor(math.sqrt(num))
    return all(num % divisor != 0 for divisor in range(3, max_divisor+1, 2))


if __name__ == '__main__':
    print(is_prime(97))
