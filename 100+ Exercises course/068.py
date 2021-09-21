import unittest
from unittest.mock import Mock,patch
from code_generator import get_code


class TestGetCode(unittest.TestCase):

    @patch("random.randint")
    def test_get_code_mock_should_return_30(self,mock_random):
        mock_random.return_value = "30"
        self.assertEqual(get_code(),"CX-30")