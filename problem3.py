# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import time

from utils import factorise

if __name__ == '__main__':
    value = 600851475143

    t0 = time.time()
    factors = factorise(value)
    runtime = time.time() - t0

    print 'Result = {}'.format(max(factors))
    print 'Runtime = {}'.format(runtime)
