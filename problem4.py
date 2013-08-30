# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(n):
    n = str(n)

    for i in xrange(len(n)):
        if n[i] != n[-i - 1]:
            return False

    return True

# Run Test Suite
assert is_palindrome(9009)
assert not is_palindrome(54)


if __name__ == '__main__':
    import sys

    max = 0
    max_i = 0
    max_j = 0

    for i in reversed(xrange(100, 999)):
        for j in reversed(xrange(100, 999)):
            value = i * j

            if is_palindrome(value) and value > max:
                max = value
                max_i = i
                max_j = j

    print 'Found largest palindrome: {} ({} x {})'.format(max, max_i, max_j)
    print 'Finished'
