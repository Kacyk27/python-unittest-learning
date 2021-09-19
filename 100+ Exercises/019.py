import unittest


def calculate_daily_return(open, close):
    return (close / open - 1) * 100


class TestCalculateDailyReturn(unittest.TestCase):

    def test_positive_return(self):
        self.assertAlmostEqual(calculate_daily_return(349.0,360.0),3.15,2)

    def test_negative_return(self):
        self.assertAlmostEqual(calculate_daily_return(349.0,340.0),-2.58,2)

    def test_zero_return(self):
        self.assertAlmostEqual(calculate_daily_return(349.0,349.0),0.0,2)
