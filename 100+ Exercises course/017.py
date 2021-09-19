import unittest


class TestLstripMethod(unittest.TestCase):

    def test_lstrip1(self):
        self.assertEqual(" Omae wa mou shindeiru".lstrip(),"Omae wa mou shindeiru")

    def test_lstrip2(self):
        self.assertEqual(" One two three".lstrip(),"One two three")


class TestStripMethod(unittest.TestCase):

    def test_strip1(self):
        self.assertEqual("    Omae wa mou shindeiru   ".strip(),"Omae wa mou shindeiru")

    def test_strip2(self):
        self.assertEqual("    One two three    ".strip(),"One two three")


class TestRstripMethod(unittest.TestCase):

    def test_rstrip1(self):
        self.assertEqual("One two three     ".rstrip(),"One two three")

    def test_rstrip2(self):
        self.assertEqual("Omae wa mou shindeiru   ".strip(), "Omae wa mou shindeiru")