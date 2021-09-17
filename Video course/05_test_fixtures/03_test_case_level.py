import unittest

def setUpModule():
    print("Setting up module...")


def tearDownModule():
    print("tearing down module...")


class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f"setting up class1 {cls.__name__}...")

    @classmethod
    def tearDownClass(cls):
        print(f"tearing down class1 {cls.__name__}...")

    def setUp(self):
        print(f"Setting up from case lvl 123...")

    def tearDown(self):
        print(f"Tearing ddown from case lvl 123...")

    def test_case_1(self):
        self.assertEqual("John Smith".split(), ["John","Smith"])

    def test_case_2(self):
        self.assertEqual("John Smith".split(), ["John","Smith"])


class TestClass2(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual("3.9".split("."),["3","9"])


class TestClass3(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual("#".join(["sport","gym"]),"sport#gym")
