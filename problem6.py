# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and
# the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


if __name__ == '__main__':

    UP_TO = 100

    value1 = 0
    for i in xrange(1, UP_TO + 1):
        value1 += i ** 2

    value2 = 0
    for i in xrange(1, UP_TO + 1):
        value2 += i

    value2 **= 2

    print 'Result = {}'.format(value2 - value1)