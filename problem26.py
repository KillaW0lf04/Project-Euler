# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions
# with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has
# a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import time


# Taken from:
# http://www.mathblog.dk/project-euler-26-find-the-value-of-d-1000-for-which-1d-contains-the-longest-recurring-cycle/
# How does this work? This is the same process as a long division
def cycle_length(number):
    remainders = set()
    i = 0
    prev = 0

    while i <= number:

        remainder = max(10*prev, 1) % number
        prev = remainder

        if remainder in remainders:
            return i
        else:
            remainders.add(remainder)

        i += 1

    return -1


if __name__ == '__main__':
    assert cycle_length(3) == 1
    assert cycle_length(7) == 6
    assert cycle_length(9) == 1
    assert cycle_length(19) == 18

    t0 = time.time()

    result = 0
    max_cycle_length = 0

    for number in xrange(1, 1001):

        value = cycle_length(number)
        if value > max_cycle_length:
            max_cycle_length = value
            result = number

    runtime = time.time() - t0

    print 'Result = {}'.format(result)
    print 'Runtime = {}'.format(runtime)
