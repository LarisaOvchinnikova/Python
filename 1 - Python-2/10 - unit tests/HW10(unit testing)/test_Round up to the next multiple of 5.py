def round_to_next5(n):
    while n % 5 != 0:
        n += 1
    return n


def test_round_to_next5_mult5():
    assert round_to_next5(0) == 0
    assert round_to_next5(10) == 10
    assert round_to_next5(30) == 30
    assert round_to_next5(-5) == -5


def test_round_to_next5_non_mult5():
    assert round_to_next5(2) == 5
    assert round_to_next5(3) == 5
    assert round_to_next5(12) == 15
    assert round_to_next5(21) == 25
    assert round_to_next5(-2) == 0

