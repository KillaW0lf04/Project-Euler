# ~.~ coding=utf8 ~.~

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

# Because of the hint, you should store results in a set to prevent collisions
# perform sum(result) to find answer

from utils import is_pandigital

if __name__ == '__main__':

    import time

    t0 = time.time()

    # Reasoning:
    # ----------
    # if our equation is x × y = z
    # then then following should hold true:
    #  1.  |x|, |y| <= |z|
    #  2.  x, y <= z
    #  3.  x × y = y × x = z    (Symmetry in multiplication)
    #  4.  x != y != z          (We can never have repeating digits)
    # This further implies (because we are in the range [1, 9]):
    #  5.  |x| + |y| + |z| = 9  (Due to requirements)
    #  6.  |x|, |y| <= 4        (Due to 1 and 5)
    # i.e.
    #    |x| = 3, |y| = 2  |z| = 4
    #    |x| = 4, |y| = 1  |z| = 4
    # Are the possible combinations
    # The following are impossible:
    #    |x| = 2, |y| = 2  |z| = 5
    #    |x| = 1, |y| = 3  |z| = 5
    #    |x| = 2, |y| = 1  |z| = 5
    # You can test this by taking the largest values for x and y in each case
    #    99 x 99 = 9801 |z| < 5
    #    9 x 999 = 8991 |z| < 5
    #    99 x 9 = 891   |z| < 5
    # Case for |x|=3 |y|=3 |z|=3 should also be impossible because
    # 100 * 100 = 10000
    # 999 * 999 = 998001
    # So z can never be of length 3 when x and y are also 3
    # Therefore:
    #  7.  |z| = 4

    # I.e. z = 4 combinations should only be considered

    results = set()

    # Further note that we can skip 100, 1000 etc because these
    # have repeating digits and include 0
    # start from and end at numbers with unique digits

    # Case 1: |x|=3 |y|=2 |z|=4
    for x in xrange(123, 987 + 1):
        for y in xrange(12, 98 + 1):
            z = x * y
            if is_pandigital(x, y, z):
                results.add(z)

    # Case 2: |x|=4 |y|=1 |z|=4
    for x in xrange(1234, 9876 + 1):
        for y in xrange(1, 12 + 1):
            z = x * y
            if is_pandigital(x, y, z):
                results.add(z)

    runtime = time.time() - t0

    print results

    print 'Results = {}'.format(sum(results))
    print 'Runtime = {}'.format(runtime)
