import unittest
from tax import calc_tax


class TestCalcTax(unittest.TestCase):

    def test_age_is_int(self):
        self.assertRaises(TypeError,calc_tax,1000,0.2,"10")
        self.assertRaises(TypeError,calc_tax,1000,0.2,10.0)

    def test_age_is_positive(self):
        self.assertRaises(ValueError,calc_tax,1000,0.2,-5)

    def test_age_below_18(self):
        self.assertEqual(calc_tax(1000,0.23,15),230)
        self.assertEqual(calc_tax(1000,0.23,18),230)

    def test_age_greater_18_belowEqual_65(self):
        self.assertEqual(calc_tax(10000,0.5,19),5000)
        self.assertEqual(calc_tax(10000,0.5,65),5000)

    def test_age_greater_65(self):
        self.assertEqual(calc_tax(10000,0.9,90),8000)

