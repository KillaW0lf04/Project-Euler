# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


def is_prime(n):

    for i in xrange(2, n - 1):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':
    value = 600851475143
    sub_value = value

    while True:

        if is_prime(sub_value):
            print sub_value, '... True'   # We have our result
            break
        else:
            print sub_value, '.... False'

        # Find the next number to divide by
        for i in xrange(2, sub_value - 1):
            if sub_value % i == 0:

                print 'Dividing by %s' % i
                sub_value /= i
                break

    print 'Finished'

