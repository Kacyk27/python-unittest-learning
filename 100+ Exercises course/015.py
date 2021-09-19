import unittest


class TestLower(unittest.TestCase):

    def test_lower(self):
        self.assertEqual("Joe.Smith@mail.com".lower(),"joe.smith@mail.com")

    def test_is_lower(self):
        self.assertEqual("joe.smith@mail.com".islower(),True)
        self.assertEqual("Joe.Smith@mail.com".islower(),False)