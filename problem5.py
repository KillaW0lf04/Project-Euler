# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# NOTE: Remember xrange is exclusive of the last value passed
import operator
import time

from collections import Counter
from utils import factorise

# assert we are understanding the concept of evenly divisible correctly
value = 2520
for i in xrange(2, 11):
    assert value % i == 0, 'fails for {}'.format(i)


if __name__ == '__main__':
    t0 = time.time()

    # Use the counter class for performing list operations
    primes = Counter()

    # Method used to generate 2520 in the question
    value = 1
    for i in reversed(xrange(2, 21)):
        if value % i != 0:
            print '{} does not divide {} evenly...'.format(i, value)
            factors = factorise(i)

            print 'Appending missing factors: {}'.format(factors)
            primes += (Counter(factors) - primes)

            value = reduce(operator.mul, primes.elements(), 1)
            print value

    runtime = time.time() - t0

    print
    print 'Finished!'
    print 'Result = {}, Factors = {}'.format(value, list(primes.elements()))
    print 'Runtime = {}'.format(runtime)
