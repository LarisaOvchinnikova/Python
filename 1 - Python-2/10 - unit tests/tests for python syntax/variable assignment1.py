# Name of challenger
# Variable assignment


# Create a variable with the name `pos_num` and assign it the value of any integer positive number in the range from 10 to 200, both inclusive.

#Open test
class TestClass(object):
    def test_1(self):
        """Type of variable is int"""
        assert type(pos_num) == int, f'expected type of value should be int'
    def test_2(self):
        """Variable is positive number"""
        assert pos_num > 0, f'expected value should be positive'
    def test_3(self):
        """Variable is in valid range"""
        assert 10 <= pos_num <= 200, f'expected value should be in the range from 10 to 200'

#Completed solution
pos_num = 100