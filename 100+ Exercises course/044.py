import unittest
from emp import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp1 = Employee("John","Smith",40,80000)

        self.assertEqual(emp1.email, "john.smith@mail.com")