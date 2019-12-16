"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(num):
    return num == reverse_number(num)


def reverse_number(input_number):
    reversed_number = 0
    while input_number > 0:
        last_digit = input_number % 10
        reversed_number = 10 * reversed_number + last_digit
        input_number = input_number//10
    return reversed_number


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
    print(f"largest palindrome: {largest}\nfactor1: {fac1}\nfactor2: {fac2}")

