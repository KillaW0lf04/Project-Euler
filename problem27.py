# Euler discovered the remarkable quadratic formula:
#
# n^2 + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
# However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly
# when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
#
# The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive
# values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.
#
# Considering quadratics of the form:
#
# n^2 + an + b, where |a| < 1000 and |b| < 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4

# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number
# of primes for consecutive values of n, starting with n = 0.

import time

from utils import sieve_of_eratosthenes


if __name__ == '__main__':
    t0 = time.time()

    primes = set(sieve_of_eratosthenes(100000))

    max_n = 0
    result = (0, 0)

    for a in xrange(-999, 1000):
        if a % 200 == 0:
            print '{}%'.format((100 * (a + 1000)) / 2000.0)

        for b in xrange(-999, 1000):

            n = 0
            while True:
                value = (n**2) + a*n + b
                if value < 2 or value not in primes:
                    break

                n += 1

            if n > max_n:
                max_n = n
                result = (a, b)

    runtime = time.time() - t0

    print 'Max Sequence = {}'.format(max_n)
    print 'a, b = {}'.format(result)
    print 'Result = {}'.format(result[0] * result[1])
    print 'Runtime = {}'.format(runtime)
