from utils import is_palindrome, is_prime, factorise, triangle_number
from utils import divisor_function, nCk, nPk, factorial, is_leap_year


def test_is_leap_year():

    # Years evenly divisible by 4 are leap years
    assert is_leap_year(2072)
    assert is_leap_year(2400)
    assert is_leap_year(2060)

    # Years which are centuries are not leap years
    assert not is_leap_year(1900)

    # Years which are centuries but evenly divisible by 400
    assert is_leap_year(2000)


def test_nCk():
    assert nCk(1, 1) == 1
    assert nCk(2, 1) == 2
    assert nCk(8, 4) == 70


def test_nPk():
    assert nPk(20, 2) == 20 * 19
    assert nPk(12, 5) == 12 * 11 * 10 * 9 * 8
    assert nPk(19, 3) == 19 * 18 * 17
    assert nPk(19, 19) == factorial(19)


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 5 * 4 * 3 * 2 * 1
    assert factorial(7) == 7 * 6 * 5 * 4 * 3 * 2 * 1


def test_divisors():
    assert divisor_function(1) == 1
    assert divisor_function(28) == 6
    assert divisor_function(76576500) == 576


def test_triangle_number():
    assert triangle_number(1) == 1
    assert triangle_number(2) == 3
    assert triangle_number(5) == 15
    assert triangle_number(7) == 28


def test_is_palindrome():
    assert is_palindrome(9009)
    assert is_palindrome(5)
    assert is_palindrome(525)
    assert not is_palindrome(54)


def test_is_prime():
    assert is_prime(2)
    assert is_prime(5)
    assert is_prime(3)
    assert is_prime(23)
    assert is_prime(311)
    assert is_prime(313)
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(8)
    assert not is_prime(16)
    assert not is_prime(100)
    assert not is_prime(27)


def test_factorise():
    # Result will always be sorted in ascending order
    assert factorise(0) == []
    assert factorise(1) == []
    assert factorise(10) == [2, 5]
    assert factorise(16) == [2, 2, 2, 2]
    assert factorise(27) == [3, 3, 3]
    assert factorise(35) == [5, 7]
