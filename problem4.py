# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
import time

from utils import is_palindrome


if __name__ == '__main__':
    t0 = time.time()

    max = 0
    max_i = 0
    max_j = 0

    for i in reversed(xrange(100, 999)):
        for j in reversed(xrange(100, 999)):
            value = i * j

            if is_palindrome(value) and value > max:
                max = value
                max_i = i
                max_j = j

    runtime = time.time() - t0

    print 'Found largest palindrome: {} ({} x {})'.format(max, max_i, max_j)
    print 'Runtime = {}'.format(runtime)
