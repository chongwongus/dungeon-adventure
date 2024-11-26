import unittest
import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from Adventurer import Adventurer

# test/test_Adventurer.py

class TestAdventurer(unittest.TestCase):

    def setUp(self):
        self.adventurer = Adventurer("John", 100, 10)

    def test_initialization(self):
        self.assertEqual(self.adventurer.name, "John")
        self.assertEqual(self.adventurer.health, 100)
        self.assertEqual(self.adventurer.strength, 10)

    def test_take_damage(self):
        self.adventurer.take_damage(20)
        self.assertEqual(self.adventurer.health, 80)

    def test_heal(self):
        self.adventurer.take_damage(20)
        self.adventurer.heal(10)
        self.assertEqual(self.adventurer.health, 90)

    def test_attack(self):
        enemy = Adventurer("Enemy", 100, 5)
        self.adventurer.attack(enemy)
        self.assertEqual(enemy.health, 90)

if __name__ == '__main__':
    unittest.main()