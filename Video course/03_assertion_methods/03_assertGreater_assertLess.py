import unittest

class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertGreater(3,4)
        #sprawdza wyższosć pierwszej nad drugą

    def test_case_2(self):
        self.assertGreater(5,4)

    def test_case_3(self):
        self.assertGreaterEqual(4,4)
        #większy równy

    def test_case_4(self):
        self.assertLess(3,4)

    def test_case_5(self):
        self.assertLessEqual(4,4)