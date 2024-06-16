import unittest


def leap_year(year):
    if year == 0:
        return True


class LeapYearTest(unittest.TestCase):
    def test_leap_year(self):
        self.assertTrue(leap_year(0))


if __name__ == '__main__':
    unittest.main()