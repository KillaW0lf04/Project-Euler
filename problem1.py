# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
import time


if __name__ == '__main__':
    t0 = time.time()

    valid_numbers = []

    # Find all multiples of 3 and 5
    for i in xrange(1000):
        if i % 3 == 0 or i % 5 == 0:
            valid_numbers.append(i)

    result = sum(valid_numbers)

    runtime = time.time() - t0

    print 'Result = {}'.format(result)
    print 'Runtime = {}'.format(runtime)
