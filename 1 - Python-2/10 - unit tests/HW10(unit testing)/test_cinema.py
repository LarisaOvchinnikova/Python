# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()
def cinema(x, y):
    if x > 2 * y or y > 2 * x: return None
    s = ''
    if x >= y:
        trio = x - y
        doubles = y - trio
        s += 'BGB'* trio
        s += "BG" * doubles
    else:
        trio = y - x
        doubles = x - trio
        s += 'GBG' * trio
        s += "GB" * doubles
    return s


def test_cinema():
    assert cinema(1, 1) == "BG"
    assert cinema(2, 1) == "BGB"

 def _():
        try:
            test.expect(cinema)
        except NameError:
            test.fail("cinema function doesn't exist")