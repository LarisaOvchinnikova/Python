from prime_numbers import is_prime, fibonacci


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(-1) == False
    assert is_prime(4) == False


def test_fibonacci():
    assert fibonacci(1) == 1
