import unittest
import math


def perimeter(radius):
    """The function returns the length of the circle."""

    if not (isinstance(radius, (int, float))):
        raise TypeError('The radius must be of type int or float.')

    if not radius > 0:
        raise ValueError('The radius must be positive.')

    return 2 * math.pi * radius


class TestPerimeter(unittest.TestCase):

    def test_radius_less_than_zero(self):
        self.assertRaises(ValueError,perimeter,-2)

    def test_radius_four(self):
        self.assertAlmostEqual(perimeter(5),math.pi*2*5,5)

    def test_radius_str_type(self):
        self.assertRaises(TypeError,perimeter, "120")

    def test_radius_equal_zero(self):
        self.assertRaises(ValueError,perimeter,0)