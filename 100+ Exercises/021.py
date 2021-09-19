import unittest


class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __eq__(self, other):
        return len(self.string) == len(other.string)


doc1= Doc("Online")
doc2 = Doc('Nature')
doc3 = Doc('Technology')

class TestDoc(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(doc2,doc1)

    def test_not_equal(self):
        self.assertNotEqual(doc3,doc1)
        self.assertNotEqual(doc3,doc2)
