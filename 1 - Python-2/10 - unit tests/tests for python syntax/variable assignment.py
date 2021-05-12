# Name of challenger
# Variable assignment


# Create a variable with the name `number` and assign it a value `10`.

#Open test
class TestClass1(object):
    def test_1(self):
        """Variable created"""
        assert number == "a", f"expected value equal to 'a'"


class TestClass2(object):
    def test_1(self):
        """Variable created"""
        assert a == 10, f"expected value equal to 'a'"

    def test_2(self):
        """Variable created"""
        assert type(a) == int, f"expected type of value equal to int"


class TestClass3(object):
    def test_1(self):
        """Variable created"""
        assert b == 6, f"expected value equal to 6"

    def test_2(self):
        """Variable created"""
        assert type(b) == int, f"expected type of value equal to int"


class TestClass4(object):
    def test_1(self):
        """Variable created"""
        assert c == 1, f"expected value equal to 1"

    def test_2(self):
        """Variable created"""
        assert type(c) == int, f"expected type of value equal to int"


# Completed solution
number = "a"
a = 10
b = 6
c = a // b
print(type(c))