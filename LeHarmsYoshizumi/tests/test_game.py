import unittest
import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from DungeonAdventure import DungeonAdventure
from Adventurer import Adventurer
from dungeon.Dungeon import Dungeon

# test/test_DungeonAdventure.py

class TestDungeonAdventure(unittest.TestCase):

    def setUp(self):
        self.adventurer = Adventurer("John")
        self.dungeon = Dungeon((8,8))
        self.dungeon_adventure = DungeonAdventure()

if __name__ == '__main__':
    unittest.main()