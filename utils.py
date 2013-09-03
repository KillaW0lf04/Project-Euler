import math


# Can also be performed recursively
# triangle(n) = triangle(n-1) + n
def triangle_number(n):
    return sum(xrange(1, n + 1))


def is_palindrome(n):
    n = str(n)

    for i in xrange(len(n)):
        if n[i] != n[-i - 1]:
            return False

    return True


def is_prime(n):

    if n <= 1:
        return False

    # You can stop at
    # the square root, since all other combinations of factors would
    # include one number larger than the square root, and one smaller.
    # Once you have gone through the smaller numbers it would be
    # redundant to check the larger halves as well.
    end = math.sqrt(n)

    for i in xrange(2, int(end) + 1):
        if n % i == 0:
            return False

    return True


# A bit inefficient ... but it works
def factorise(n):

    factors = []
    end = math.sqrt(n)

    while True:

        if is_prime(n):
            factors.append(n)
            return factors

        # Find the next number to divide by
        # This approach is guaranteed to give us a prime factor
        for i in xrange(2, int(end) + 1):
            if n % i == 0:
                n /= i
                factors.append(i)
                break

    return None
