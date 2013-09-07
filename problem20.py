# n! means n x (n - 1) x ... x 3 x 2 x 1
#
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

import time

from utils import factorial


if __name__ == '__main__':
    t0 = time.time()

    value = str(factorial(100))
    result = 0

    for c in value:
        result += int(c)

    runtime = time.time() - t0

    print 'Result = {}'.format(result)
    print 'Runtime = {}'.format(runtime)
