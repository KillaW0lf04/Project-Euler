# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math
import time
import sys


if __name__ == '__main__':
    t0 = time.time()

    a = 0
    b = 0
    c = 0
    while True:
        a = 0
        b += 1

        while a < b:
            a += 1

            c = math.sqrt(a ** 2 + b ** 2)

            if a + b + c == 1000:
                runtime = time.time() - t0

                print '{}, {}, {}'.format(a, b, c)
                print 'Result = {}'.format(a * b * c)
                print 'Runtime = {}'.format(runtime)
                sys.exit(0)
