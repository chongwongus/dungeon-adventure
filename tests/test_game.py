import unittest
import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from DungeonAdventure import DungeonAdventure
from Adventurer import Adventurer
from Dungeon import Dungeon

# test/test_DungeonAdventure.py

class TestDungeonAdventure(unittest.TestCase):

    def setUp(self):
        self.adventurer = Adventurer("John", 100, 10)
        self.dungeon = Dungeon("Dark Cave", 5)
        self.dungeon_adventure = DungeonAdventure(self.adventurer, self.dungeon)

    def test_initialization(self):
        self.assertEqual(self.dungeon_adventure.adventurer, self.adventurer)
        self.assertEqual(self.dungeon_adventure.dungeon, self.dungeon)

    def test_start_adventure(self):
        result = self.dungeon_adventure.start_adventure()
        self.assertTrue(result)

    def test_adventurer_survives(self):
        self.dungeon_adventure.start_adventure()
        self.assertTrue(self.adventurer.health > 0)

    def test_adventurer_gains_experience(self):
        initial_experience = self.adventurer.experience
        self.dungeon_adventure.start_adventure()
        self.assertGreater(self.adventurer.experience, initial_experience)

if __name__ == '__main__':
    unittest.main()