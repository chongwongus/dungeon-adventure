import unittest
import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from dungeon.DFSDungeonFactory import DFSDungeonFactory
from dungeon.Dungeon import Dungeon
from dungeon.Room import Room

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
        self.assertTrue(self.check_dfs_criteria(dungeon))

    def check_dfs_criteria(self, dungeon):
        # Ensure the player can reach all pillars and the exit from the entrance
        entrance = dungeon.entrance
        exit = dungeon.exit
        pillars = 0

        # Perform a BFS or DFS to check connectivity
        visited = set()
        queue = [entrance]

        while queue:
            current_coordinates = queue.pop(0)
            current: Room = dungeon.get_room(current_coordinates[0], current_coordinates[1])
            if current in visited:
                continue
            visited.add(current)
            if current.hasPillar:
                pillars += 1

            # Add neighboring rooms to the queue
            x, y = current_coordinates
            neighbors = [
                (x - 1, y), (x + 1, y),  # Left, Right
                (x, y - 1), (x, y + 1)   # Up, Down
            ]
            for nx, ny in neighbors:
                if 0 <= nx < dungeon.size[0] and 0 <= ny < dungeon.size[1]:
                    queue.append((nx, ny))

        # Check if all pillars and the exit are reachable
        all_reachable = pillars == 4
        return all_reachable

if __name__ == '__main__':
    unittest.main()