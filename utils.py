
def is_prime(n):

    for i in xrange(2, n - 1):
        if n % i == 0:
            return False
            # Utility file for when problems share the same method

    return True


# A bit ineffecient ...
def factorise(n):

    factors = set()

    while True:

        if is_prime(n):
            factors.add(n)
            return factors

        # Find the next number to divide by
        for i in xrange(2, n - 1):
            if n % i == 0:
                n /= i
                factors.add(i)
                break

    return None

assert factorise(10) == {2, 5}
assert factorise(16) == {2}
assert factorise(27) == {3}
