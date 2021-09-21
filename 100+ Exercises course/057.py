import unittest
from rectangle import area, perimeter


class TestArea(unittest.TestCase):

    def test_area(self):
        cases = [
            (1, 5, 5),
            (2, 10, 20),
            (100, 50, 5000)
        ]
        for width, height, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(area(width, height), result)

    def test_area_incorrect_type_should_raise_type_error(self):
        cases = [
            (1,"5",TypeError),
            ("2",10,TypeError),
            ("two","four",TypeError)
        ]
        for x,y,result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(area(x,y),result)