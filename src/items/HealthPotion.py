import random
import Adventurer
from items.Potion import Potion

class HealthPotion(Potion):
    
    def __init__(self):
        super().__init__("Health Potion", "A potion that restores health 1-15 points.", "health")
        self.health_value = random.randint(5, 15)
    
    def use(self, adventurer: Adventurer):
        adventurer.hp += self.health_value
