import unittest
from solution99 import Vector


class TestVector(unittest.TestCase):

    def setUp(self):
        self.v = Vector(-3, 4, 2)

    def test_vector_repr_method(self):
        msg = 'Popraw implementację metody __repr__().'
        actual = repr(self.v)
        expected = "Vector(-3, 4, 2)"
        self.assertEqual(actual, expected, msg)