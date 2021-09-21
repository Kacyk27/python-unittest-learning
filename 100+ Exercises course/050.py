import unittest
from notebook import Note


class TestNote(unittest.TestCase):

    def test_note_has_category_class_attr(self):
        note=Note("abc")
        self.assertTrue(note.category,"Klasa Note nie posiada atrybutu category.")