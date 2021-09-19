import unittest


class TestStartswithMethod(unittest.TestCase):

    def test_startswith_one_letter(self):
        self.assertEqual("unittest".startswith("u"),True)
        self.assertEqual("unittest".startswith("U"),False)

    def test_startswith_four_letters(self):
        self.assertTrue('http://www.e-smartdata.org/'.startswith('http'))
        self.assertFalse('www.e-smartdata.org/'.startswith('http'))


class TestEndswithMethod(unittest.TestCase):

    def test_endswith_three_letter(self):
        self.assertEqual('e-smartdata.org'.endswith("org"),True)
        self.assertEqual('e-smartdata.org'.endswith("com"),False)
