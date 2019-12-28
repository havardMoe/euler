"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_of_squares(num_max):
    return sum([i**2 for i in range(1, max_num+1)])


def square_of_sum(num_max):
    return sum([i for i in range(1, max_num+1)])**2


if __name__ == "__main__":
    max_num = 2
    sum_squares = sum_of_squares(max_num)
    squared_sum = square_of_sum(max_num)

    print("max_num = {max_num}")
    print(f"sum of squares: {sum_squares}\nsquare of sum: {squared_sum}")
    print(f"\ndifference = {abs(sum_squares - squared_sum)}")
