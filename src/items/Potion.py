from abc import abstractmethod
import Adventurer
from items.Item import Item

class Potion(Item):
    def __init__(self, name: str, description: str, effect: str):
        self.name = name
        self.description = description
        self.effect = effect
        
    @abstractmethod
    def use():
        pass