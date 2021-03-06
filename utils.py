import math
import operator

from collections import Counter


def is_pandigital(x, y, z):
    # Note this isnt a true pandigital function check
    # It performs a 1-9 pandigital check for an equation
    c = [0] * 10

    def parse_no(no):
        while no != 0:
            c[no % 10] += 1
            no /= 10

    parse_no(x)
    parse_no(y)
    parse_no(z)

    is_pd = True

    for i in xrange(1, 10):
        is_pd &= c[i] == 1

    # Make sure to exclude 0!
    is_pd &= c[0] == 0

    return is_pd


# Generate primes up the given limit
def sieve_of_eratosthenes(limit):

    sieve = [True] * (limit + 1)
    sieve[0] = False
    sieve[1] = False

    for n, flag in enumerate(sieve):

        # If still marked as a prime
        if flag:
            i = n
            while n * i < limit + 1:
                sieve[n * i] = False
                i += 1

    return [n for n, flag in enumerate(sieve) if flag]


def fibonacci(n, _cache={0: 1, 1: 1, 2: 1}):
    if n not in _cache:
        _cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return _cache[n]


def is_deficient_number(n):
    return sum_of_divisors(n) < n


def is_abundant_number(n):
    return sum_of_divisors(n) > n


def is_perfect_number(n):
    return n == sum_of_divisors(n)


def sum_of_divisors(n):
    result = set()  # Use a set to prevent multiples
    result.add(1)  # Always include 1

    # We only need to check till sqrt(n)
    limit = int(math.sqrt(n))

    for i in xrange(2, limit + 1):
        if n % i == 0:
            result.add(i)
            result.add(n / i)   # Pair above sqrt(n)

    return sum(result)


# Return a true value if the given year (represented by an int) is a leap year
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# n Choose k. Also known as the binomial coefficient.
# I.e. number of possible sets we can choose k items from n choices
# When the order is not important and repetition is not allowed
def nCk(n, k):
    return nPk(n, k) / factorial(k)


# n Permute k.
# I.e. number of ways we can choose k items from n choices
# When the order is important and repetition is not allowed
# Equal to n!/(n-1)!
def nPk(n, k):
    return reduce(operator.mul, [n - i for i in xrange(k)])


def factorial(n, _cache={0: 1, 1: 1}):
    if n not in _cache:
       _cache[n] = n * factorial(n - 1)

    return _cache[n]


# Calculates the number of divisors using the divisor theorem
# http://en.wikipedia.org/wiki/Divisor_function
def number_of_divisors(n):
    primes = factorise(n)
    exponents = Counter(primes)   # Count the exponents for each prime

    result = 1

    for value in exponents.values():
        result *= value + 1

    return result


# Can also be performed recursively
# triangle(n) = triangle(n-1) + n
def triangle_number(n):
    return n * (n + 1) / 2


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
    limit = int(math.sqrt(n))

    for i in xrange(2, limit + 1):
        if n % i == 0:
            return False

    return True


# A bit inefficient ... but it works
def factorise(n):

    if n <= 1:
        return []

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
