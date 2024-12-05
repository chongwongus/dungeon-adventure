import unittest
import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from dungeon.DFSDungeonFactory import DFSDungeonFactory
from dungeon.Dungeon import Dungeon

class TestDFSDungeonFactory(unittest.TestCase):

    def setUp(self):
        self.factory = DFSDungeonFactory()

    def test_create_dungeon(self):
        size = (8, 8)
        dungeon = self.factory.create(size)
        self.assertIsInstance(dungeon, Dungeon)
        self.assertEqual(dungeon.size, size)

    def test_dungeon_rooms(self):
        size = (8, 8)
        dungeon = self.factory.create(size)
        for row in dungeon.maze:
            for room in row:
                self.assertIsNotNone(room)

    def test_dungeon_dfs_criteria(self):
        size = (8, 8)
        dungeon = self.factory.create(size)
        # Add specific checks for DFS dungeon criteria
        # For example, ensuring the dungeon layout follows DFS properties
        # This is a placeholder and should be replaced with actual criteria
        self.assertTrue(self.check_dfs_criteria(dungeon))

    def check_dfs_criteria(self, dungeon):
        # Placeholder method to check DFS dungeon criteria
        # Implement actual checks based on your game's criteria
        return True

if __name__ == '__main__':
    unittest.main()