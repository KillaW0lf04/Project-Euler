# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import time

from utils import sum_of_divisors


if __name__ == '__main__':
    t0 = time.time()

    pairs = []
    cache = set()

    for a in xrange(1, 10001):
        if a % 1000 == 0:
            print '{}%'.format(100 * (a / 10000.0))

        # We already met this one
        if a in cache:
            continue

        b = sum_of_divisors(a)

        if a != b and sum_of_divisors(b) == a:
            cache.add(a)
            cache.add(b)
            pairs.append((a, b))

    # Calculate the result with the pairs obtained
    result = 0
    for (a, b) in pairs:
        result += a
        result += b

    runtime = time.time() - t0

    print 'Amicable Pairs = {}'.format(pairs)
    print 'Result = {}'.format(result)
    print 'Runtime = {}'.format(runtime)
