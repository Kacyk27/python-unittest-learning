import unittest
from unittest.mock import patch
from employees import Programmer


class TestProgrammer(unittest.TestCase):

    def setUp(self):
        self.programmer=Programmer()
        self.programmer.add_tech("python")
        self.programmer.add_tech("sql")
        self.programmer.add_tech("java")
        self.programmer.add_tech("c++")
        self.programmer.add_tech("aws")

    @patch.object(Programmer,"get_random_tech")
    def test_get_random_tech_mocked_python(self,mocked_tech):
        mocked_tech.return_value = "python"
        self.assertEqual(self.programmer.get_random_tech(),"python")