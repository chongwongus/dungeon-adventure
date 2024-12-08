import unittest
import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from dungeon.Dungeon import Dungeon
from dungeon.Room import Room

class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.dungeon = Dungeon((8, 8))

    def test_initialization(self):
        self.assertEqual(self.dungeon.size, (8, 8))

if __name__ == '__main__':
    unittest.main()