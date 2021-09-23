import unittest
from unittest.mock import patch
from employees import Programmer


class TestProgrammer(unittest.TestCase):

    def setUp(self):
        print('setting up')
        self.programmer = Programmer()
        self.programmer.add_tech('python') \
            .add_tech('sql') \
            .add_tech('java') \
            .add_tech('c++') \
            .add_tech('aws')

    @patch.object(Programmer,"display_random_tech")
    def test_display_random_tech_mocked_python(self,mocked_tech):
        mocked_tech.return_value = "python"
        self.assertEqual(self.programmer.display_random_tech(),"python")

    @patch.object(Programmer,"display_random_tech")
    def test_display_random_tech_mocked_cpp(self,mocked_tech):
        mocked_tech.return_value = "c++"
        self.assertEqual(self.programmer.display_random_tech(),"c++")