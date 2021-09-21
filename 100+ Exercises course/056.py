import unittest
from rectangle import area,perimeter


class TestArea(unittest.TestCase):

    def test_area(self):
        cases = [
            (1,5,5),
            (2,10,20),
            (100,5,5000)
        ]
        for x,y,result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(area(x,y),result)