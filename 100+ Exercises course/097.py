import unittest
from solution97 import Pet


class TestPet(unittest.TestCase):

    def test_pet_has_name_property(self):
        msg = 'Klasa Pet nie posiada atrybutu o nazwie name.'
        self.assertTrue(hasattr(Pet, 'name'), msg)
        self.assertIsInstance(Pet.name, property)

    def test_pet_has_age_property(self):
        msg = 'Klasa Pet nie posiada atrybutu o nazwie age.'
        self.assertTrue(hasattr(Pet, 'age'), msg)
        self.assertIsInstance(Pet.age, property)