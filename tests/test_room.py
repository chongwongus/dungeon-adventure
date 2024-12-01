import unittest
import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from dungeon.Room import Room
from Adventurer import Adventurer

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room()

    def test_initialization(self):
        self.assertEqual(self.room.name, "Treasure Room")
        self.assertEqual(self.room.description, "A room filled with gold and jewels.")
        self.assertEqual(self.room.adventurers, [])

    def test_add_adventurer(self):
        adventurer = Adventurer("John", 100, 10)
        self.room.add_adventurer(adventurer)
        self.assertIn(adventurer, self.room.adventurers)

    def test_remove_adventurer(self):
        adventurer = Adventurer("John", 100, 10)
        self.room.add_adventurer(adventurer)
        self.room.remove_adventurer(adventurer)
        self.assertNotIn(adventurer, self.room.adventurers)

    def test_room_description(self):
        self.assertEqual(self.room.get_description(), "A room filled with gold and jewels.")

if __name__ == '__main__':
    unittest.main()