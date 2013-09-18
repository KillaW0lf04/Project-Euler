# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import time

# It is also possible to calculate this problem by observing that the
# negative diagonal is the square of numbers.
# 25 = 5^2  9 = 3^2   1 = 1 ^ 2
# 5 = 2^2 + 1  17 = 4^2 + 1

# The other diagonal can then be easily calculate by subtracting appropriately


def sum_of_diagonals(spiral):
    result = 0
    size = len(spiral)

    for i in xrange(size):
        result += spiral[i][i]

        # Prevent overlapping
        if size - i - 1 != i:
            result += spiral[i][size - i - 1]

    return result


# Generates a spiral according to the specification
def create_spiral(size):

    result = []

    for _ in xrange(size):
        result.append([0] * size)

    center = size/2

    result[center][center] = 1

    counter = 2
    for i in xrange(1, center + 1):

        for j in xrange(1, 2 * i):
            result[center + j - i][center + i] = counter
            counter += 1

        for j in xrange(2 * i):
            result[center + i][center + i - j] = counter
            counter += 1

        for j in xrange(2 * i):
            result[center + i - j][center - i] = counter
            counter += 1

        for j in xrange(2 * i + 1):
            result[center - i][center - i + j] = counter
            counter += 1

    return result


if __name__ == '__main__':

    spiral = create_spiral(5)

    # 21 22 23 24 25
    # 20  7  8  9 10
    # 19  6  1  2 11
    # 18  5  4  3 12
    # 17 16 15 14 13
    assert spiral == [
        [21, 22, 23, 24, 25],
        [20, 7,  8,  9,  10],
        [19, 6,  1,  2,  11],
        [18, 5,  4,  3,  12],
        [17, 16, 15, 14, 13]
    ]

    assert sum_of_diagonals(spiral) == 101

    t0 = time.time()

    spiral = create_spiral(1001)
    result = sum_of_diagonals(spiral)

    runtime = time.time() - t0

    print 'Runtime = {}'.format(runtime)
    print 'Result = {}'.format(result)
