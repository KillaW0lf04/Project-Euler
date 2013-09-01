# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

from utils import is_prime

if __name__ == '__main__':

    counter = 1
    n = 0

    while True:
        counter += 1

        if is_prime(counter):
            n += 1

        if n % 100 == 0:
            print n

        if n == 10001:
            break

    print 'Result = {}'.format(counter)