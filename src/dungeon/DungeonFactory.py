from abc import ABC, abstractmethod

from dungeon.Dungeon import Dungeon

class DungeonFactory(ABC):
    @abstractmethod
    def create(self) -> Dungeon:
        pass