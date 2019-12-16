"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import math


def is_prime(num):
    if num < 2: return False  # no number under 2 is a prime
    elif num == 2: return True  # 2 is the only even prime number
    elif num % 2 == 0: return False
    else:
        max_divisor = math.floor(math.sqrt(num))
        return all(num % divisor != 0 for divisor in range(3, max_divisor+1, 2))


def largest_prime_factor(number):
    max_prime_limit = math.floor(math.sqrt(number))
    for i in range(max_prime_limit+1, 2, -1):
        if is_prime(i) and number % i == 0:
            return i
    return False


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
