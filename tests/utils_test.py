from utils import factorise, is_prime


def test_is_prime():
    assert is_prime(5)
    assert is_prime(3)
    assert is_prime(23)
    assert not is_prime(8)
    assert not is_prime(100)
    assert not is_prime(27)


def test_factorise():
    assert factorise(10) == {2, 5}
    assert factorise(16) == {2}
    assert factorise(27) == {3}
