"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def fibo_even_sum(stop_cond=4000000):
    prev, curr, even_sum, temp = 1, 1, 0, 0
    while curr < stop_cond:
        temp = curr
        curr += prev
        prev = temp

        if curr % 2 == 0:
            even_sum += curr
    return even_sum


if __name__ == '__main__':
    even_fibo_sum = fibo_even_sum()
    print(even_fibo_sum)

