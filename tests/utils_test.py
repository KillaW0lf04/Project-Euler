from utils import is_palindrome, is_prime, factorise, triangle_number, divisor_function


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
