# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
# if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
# of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can
# be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is
# less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import time


from utils import is_abundant_number


if __name__ == '__main__':
    t0 = time.time()

    abundant_numbers = set()

    # We can "quickly" generate a list of abundant numbers
    # Pre-computed for quick set look ups
    for i in xrange(1, 28124):
        if is_abundant_number(i):
            abundant_numbers.add(i)

    # Generate all the numbers which can be represented by the sum of two
    # abundant numbers
    results = {}
    for number in xrange(1, 28124):
        if number % 2000 == 0:
            print '{}%'.format((100 * number) / 28123)

        for i in xrange(1, number + 1):
            if i in abundant_numbers and number - i in abundant_numbers:
                results[number] = (i, number - i)
                break

    # Generate the inverse of above
    inverse_results = set(range(28123)) - set(results.keys())

    runtime = time.time() - t0
    print 'Result = {}'.format(sum(inverse_results))
    print 'Runtime = {}'.format(runtime)
