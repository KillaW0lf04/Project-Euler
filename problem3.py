# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


# Effecient squaring algorithm
def exp(x, e):
    if e == 0:
        return 1
    elif e == 1:
        return x
    elif e % 2 == 0:
        return exp(x * x, e / 2)
    elif e % 2 == 1:
        return x * exp(x * x, (e - 1)/2)


# Fermat's last theorem
# This is actually really ineffecient :(
def is_prime(n):

    a = (n - 2) / 2

    # Needs to be an effecient exp function
    return exp(a, n) % n == a % n


def is_prime2(n):

    for i in xrange(2, n - 1):
        if n % i == 0:
            return False

    return True


# Run test suite
assert exp(2, 2) == 2 ** 2
assert exp(102, 32) == 102 ** 32

assert is_prime(3)
assert is_prime2(3)

assert is_prime(5)
assert is_prime2(5)

assert is_prime(53)
assert is_prime2(53)

assert not is_prime(20)
assert not is_prime2(20)


if __name__ == '__main__':
    value = 600851475143
    sub_value = value

    while True:

        if is_prime2(sub_value):
            print sub_value, '... True'   # We have our result
            break
        else:
            print sub_value, '.... False'

        primes = [2, 3, 5, 7, 11, 17, 23]

        for p in primes:
            if sub_value % p == 0:
                sub_value /= p
                break

        assert False, "This should not have reached here!"

    print 'Finished'

