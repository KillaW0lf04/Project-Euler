# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
import time

from utils import sieve_of_eratosthenes


if __name__ == '__main__':
    t0 = time.time()

    results = sieve_of_eratosthenes(2000000)

    runtime = time.time() - t0

    print 'Runtime = {}'.format(runtime)
    print 'Result = {}'.format(sum(results))
