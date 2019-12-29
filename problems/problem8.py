"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""

if __name__ == '__main__':

    filename = "assets/p8_numbers.txt"
    numbers = []
    with open(filename, mode="r") as f:
        for line in f:
            for number in line.rstrip('\n'):
                numbers.append(int(number))

    print(numbers)
