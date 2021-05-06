# Double number

# You need to double the integer and return it.

# Initial solution
def double(i):
  pass


# Completed solution
def double(i):
    return i * 2

#Open test
from random import randint

def _double(i):
    return i * 2

class TestClass(object):

    def test_1(self):
        """Function double called with argument (2) should be equal to 4"""
        actual = double(2)
        expected = _double(2)
        assert actual == expected, f"expected {expected}, got {actual}"

    def test_2(self):
        """Function double called with argument (5) should be equal to 10"""
        actual = double(5)
        expected = _double(5)
        assert actual == expected, f"expected {expected}, got {actual}"

    def test_3(self):
        "Function double called with argument (-10) should be equal to -20"
        actual = double(-10)
        expected = _double(-10)
        assert actual == expected, f"expected {expected}, got {actual}"

    def test_random(x):
        """Function should work for random tests"""
        for i in range(10):
            x = randint(-100, 100)
            actual = double(x)
            expected = _double(x)
            assert actual == expected, f"Function should work for argument ({x}): expected {expected}, got {actual}"