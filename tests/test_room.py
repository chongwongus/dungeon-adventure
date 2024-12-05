import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from Adventurer import Adventurer
from dungeon.Room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room()

    def test_initialization(self):
        self.assertFalse(self.room.hasHealthPot)
        self.assertFalse(self.room.hasPillar)
        self.assertFalse(self.room.hasPit)
        self.assertFalse(self.room.hasVisionPot)

    def test_add_doors(self):
        self.assertTrue(not self.room.doors['N'])
        self.assertTrue(not self.room.doors['S'])
        self.assertTrue(not self.room.doors['E'])
        self.assertTrue(not self.room.doors['W'])
        self.room.doors= {
            'N': True,
            'S': True,
            'E': True,
            'W': True
        }
        self.assertTrue(self.room.doors['N'])
        self.assertTrue(self.room.doors['S'])
        self.assertTrue(self.room.doors['E'])
        self.assertTrue(self.room.doors['W'])

    def test_room_description(self):
        self.assertEqual(self.room.get_room_display(), " ")
        self.room.hasHealthPot = True
        self.assertEqual(self.room.get_room_display(), "H")
        self.room.hasHealthPot = False
        self.room.hasPit = True
        self.assertEqual(self.room.get_room_display(), "X")

if __name__ == '__main__':
    unittest.main()