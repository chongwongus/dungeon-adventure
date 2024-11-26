import unittest
import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from Dungeon import Dungeon

# test/test_Dungeon.test.py


class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.dungeon = Dungeon("Dark Cave", 5)

    def test_initialization(self):
        self.assertEqual(self.dungeon.name, "Dark Cave")
        self.assertEqual(self.dungeon.level, 5)

    def test_add_adventurer(self):
        adventurer = Adventurer("John", 100, 10)
        self.dungeon.add_adventurer(adventurer)
        self.assertIn(adventurer, self.dungeon.adventurers)

    def test_remove_adventurer(self):
        adventurer = Adventurer("John", 100, 10)
        self.dungeon.add_adventurer(adventurer)
        self.dungeon.remove_adventurer(adventurer)
        self.assertNotIn(adventurer, self.dungeon.adventurers)

    def test_start_adventure(self):
        adventurer = Adventurer("John", 100, 10)
        self.dungeon.add_adventurer(adventurer)
        result = self.dungeon.start_adventure()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
