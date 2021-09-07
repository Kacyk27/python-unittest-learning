import unittest

def area(width,height):

    if not (isinstance(width,(int,float)) and
            isinstance(height, (int,float))):
        raise TypeError("The width and height must be of type int or float.")

    if not (width > 0 and height > 0):
        raise ValueError("The width and height must be positive.")

    return width * height

class TestArea(unittest.TestCase):

    def test_area_1(self):
        self.assertEqual(area(4,5),20)

    def test_area_2(self):
        self.assertEqual(area(4,5),21)

    def test_area_3(self):
        raise AssertionError("Error message.")

    def test_area_4(self):
        raise TypeError("Error message.")
    # def test_area_incorrect_type_should_raise_error(self):
    #     self.assertRaises(TypeError, area, "4",5)
    #     self.assertRaises(TypeError, area, 4,'5')
    #
    # def test_area_negative_value_should_raise_error(self):
    #     self.assertRaises(ValueError, area, -4,5)
    #     self.assertRaises(ValueError, area, 4,-5)

if __name__ == "__main__":
    unittest.main(verbosity=2)