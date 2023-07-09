import unittest
from Test1 import get_full_name

class NamesTestCase(unittest.TestCase):
    def test_first_last(self):
        full_name = get_full_name('janis', 'joplin')
        self.assertEqual(full_name, 'Janis Joplin')

unittest.main()