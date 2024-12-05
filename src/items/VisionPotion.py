from events.Observable import Observable
from items.Potion import Potion

class VisionPotion(Potion, Observable):
    def __init__(self):
        super().__init__("Vision Potion", "A potion that allows you to see the location of the pillars.")
    
    def use(self, dungeon, adventurer):
        """
        Use the vision potion
        :param adventurer: the adventurer using the potion
        :return: None
        """
        adventurer.visionPot += 1
        self.notify(VISION_POTION_USED)
        