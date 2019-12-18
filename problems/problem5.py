"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


# bad solution O(answer_number * max divisor)
def smallest_multiple_v1(divisor_max, divisor_min=1):
    if divisor_min > divisor_max:
        return "Max has to be equal or larger than min"
    divisor = divisor_min
    number = 1
    while divisor <= divisor_max:
        if number % divisor == 0:
            divisor += 1
        else:
            number += 1
            divisor = divisor_min
    return number


def smallest_multiple(divisor_max, divisor_min):
    pass 


if __name__ == '__main__':
    n = 16
    print(smallest_multiple_v1(n))
