import unittest
import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/items')))

from Adventurer import Adventurer
from items.HealthPotion import HealthPotion

# test/test_Adventurer.py

class TestAdventurer(unittest.TestCase):

    def setUp(self):
        self.adventurer = Adventurer("John")

    def test_initialization(self):
        self.assertEqual(self.adventurer.name, "John")
        self.assertLessEqual(self.adventurer.hp, 100)
        self.assertGreaterEqual(self.adventurer.hp, 50)
        self.assertEqual(self.adventurer.healingPot, [])
        self.assertEqual(self.adventurer.visionPot, [])

    def test_take_damage(self):
        starting_hp = self.adventurer.hp
        self.adventurer.take_dmg(20)
        self.assertEqual(self.adventurer.hp, starting_hp-20)
    
    def test_use_healing_pot(self):
        # Test when healing potions are available
        self.adventurer.healingPot = [HealthPotion()]
        result = self.adventurer.use_healing_pot()
        self.assertTrue(result)
        
        # Test when no healing potions are available
        self.adventurer.healingPot = []
        result = self.adventurer.use_healing_pot()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()