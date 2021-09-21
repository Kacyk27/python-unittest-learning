import unittest
from unittest.mock import Mock,patch
from message_generator import get_message


class TestGetMessage(unittest.TestCase):

    @patch("message_generator.get_today_name")
    def test_get_message_with_friday(self,mocked_day):
        mocked_day.return_value = "Friday"
        actual = get_message()
        expected = "Hello Friday"
        self.assertEqual(actual,expected)