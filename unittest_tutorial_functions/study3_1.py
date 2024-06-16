import unittest


def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


class LeapYearTest(unittest.TestCase):
    def test_leap_year(self):
        self.assertTrue(leap_year(0))
        self.assertFalse(leap_year(1))
        self.assertTrue(leap_year(4))
        self.assertTrue(leap_year(1200))
        self.assertFalse(leap_year(700))


if __name__ == '__main__':
    unittest.main()