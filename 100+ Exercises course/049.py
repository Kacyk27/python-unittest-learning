import unittest
from notebook import Note


class TestNote(unittest.TestCase):

    def setUp(self):
        self.note = Note('Simple note.')

    def test_note_has_content_instance_attr(self):
        self.assertTrue(self.note.content,"Instancja klasy Note nie posiada atrybutu content.")
