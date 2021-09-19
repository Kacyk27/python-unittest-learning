import unittest


class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __lt__(self, other):
        return len(self.string) < len(other.string)

doc1= Doc("Technology")
doc2 = Doc('Online')
doc3 = Doc('Nature')

class TestDoc(unittest.TestCase):

    def test_less_than(self):
        self.assertLess(doc2,doc1)
        self.assertLess(doc3,doc1)

    def test_greater_than(self):
        self.assertGreater(doc1,doc2)
        self.assertGreater(doc1,doc3)