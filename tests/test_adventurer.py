import unittest
import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from Adventurer import Adventurer

# test/test_Adventurer.py

class TestAdventurer(unittest.TestCase):

    def setUp(self):
        self.adventurer = Adventurer("John")

    def test_initialization(self):
        self.assertEqual(self.adventurer.name, "John")
        self.assertLessEqual(self.adventurer.hp, 100)
        self.assertGreaterEqual(self.adventurer.hp, 50)
        self.assertEqual(self.adventurer.healingPot, 0)
        self.assertEqual(self.adventurer.visionPot, 0)

    def test_take_damage(self):
        starting_hp = self.adventurer.hp
        self.adventurer.take_dmg(20)
        self.assertEqual(self.adventurer.hp, starting_hp-20)

    def test_heal(self):
        starting_hp = self.adventurer.hp
        self.adventurer.heal(20)
        self.assertGreaterEqual(starting_hp+20, self.adventurer.hp)

if __name__ == '__main__':
    unittest.main()