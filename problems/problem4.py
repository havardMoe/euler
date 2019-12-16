"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
from itertools import product


def is_palindrome(n):
    num = n
    rev_num = 0
    while n > 0:
        last_digit = n % 10
        rev_num = 10*rev_num + last_digit
        n = n//10  # removing last digit from n
    if num == rev_num:
        return True
    else:
        return False


if __name__ == '__main__':
    largest = -1
    fac1 = -1
    fac2 = -1
    for x in range(100, 999+1):
        for y in range(x, 999+1):
            if is_palindrome(x*y):
                if x*y > largest:
                    largest = x*y
                    fac1 = x
                    fac2 = y
    print(f"largest pali: {largest}\nfactor1: {fac1}\nfactor2: {fac2}")
