import unittest


class StringListOnly(list):

    def append(self, string):
        if not isinstance(string, str):
            raise TypeError('Only object of type str can be added to the list.')
        super().append(string)


class TestStringListOnly(unittest.TestCase):

    def test_append_string(self):
        x = StringListOnly()
        mess = "abc"
        x.append(mess)
        self.assertIn(mess,x)

    def test_append_not_string_should_raise_error(self):
        x=StringListOnly()
        self.assertRaises(TypeError,x.append,["a","b"])
        self.assertRaises(TypeError,x.append,False)