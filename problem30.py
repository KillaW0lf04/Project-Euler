# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import time


def sum_of_digit_powers(value, power):

    str_value = str(value)

    result = 0
    for i in str_value:
        result += int(i) ** power

    return result


if __name__ == '__main__':

    assert sum_of_digit_powers(1634, 4) == 1634
    assert sum_of_digit_powers(8208, 4) == 8208
    assert sum_of_digit_powers(9474, 4) == 9474

    t0 = time.time()

    results = []

    # The trick behind this problem is finding an upperbound
    # Since our upper bound is in the form of powers of 5 we can say
    # x*9^5 is our upper bound
    # First try: 5*9^5 = 295245
    # But this is 6 digits
    # Second try: 6*9^5 = 354294
    # Which is 6 digits, so were good.
    # Rounding up, we get our upper bound below
    for i in xrange(2, 355001):
        if sum_of_digit_powers(i, 5) == i:
            results.append(i)

    runtime = time.time() - t0

    print 'Runtime = {}'.format(runtime)
    print 'Numbers = {}'.format(results)
    print 'Result = {}'.format(sum(results))
