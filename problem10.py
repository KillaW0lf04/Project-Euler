# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from utils import is_prime


if __name__ == '__main__':

    value = 0
    for i in xrange(2, 2 * (10 ** 6)):

        if i % 100000 == 0:
            print i

        if is_prime(i):
            value += i

    print 'Result = {}'.format(value)
