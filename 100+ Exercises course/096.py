import unittest
from solution96 import Pet


class TestPet(unittest.TestCase):

    def test_pet_has_name_property(self):
        msg = 'Klasa Pet nie posiada atrybutu o nazwie name.'
        self.assertTrue(hasattr(Pet, 'name'), msg)
        self.assertIsInstance(Pet.name, property)