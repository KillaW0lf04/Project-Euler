# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?

import time

from utils import triangle_number, number_of_divisors

# Properties of triangular numbers
#
#  * triangle(n) = triangle(n - 1) + n
#  * triangle(n - 1) + triangle(n) = n^2
#  * triangle(n) = n * (n + 1) / 2


if __name__ == '__main__':
    t0 = time.time()

    n = 1
    triangle = 0
    d = 0

    while True:

        triangle = triangle_number(n)
        n += 1

        d = number_of_divisors(triangle)

        if d > 500:
            break

    runtime = time.time() - t0
    print 'Result = {} (Divisors = {})'.format(triangle, d)
    print 'Runtime = {}'.format(runtime)
