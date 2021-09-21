import unittest
from notebook import Notebook


class TestNotebook(unittest.TestCase):

    def setUp(self):
        self.notebook = Notebook()
        self.notebook.new_note('Big Data')
        self.notebook.new_note('Data Science')
        self.notebook.new_note('Machine Learning')

    def test_notebook_search_method(self):
        actual = self.notebook.search('data')
        expected = ['Big Data', 'Data Science']
        self.assertEqual(actual, expected)