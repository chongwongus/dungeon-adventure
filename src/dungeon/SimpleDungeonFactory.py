import random
from dungeon.Dungeon import Dungeon
from dungeon.DungeonFactory import DungeonFactory

class SimpleDungeonFactory(DungeonFactory):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def create(self):
        dungeon = Dungeon((self.width, self.height))
        dungeon.current_room = dungeon.rooms[0][0]
        dungeon.exit = random.randint(0, dungeon.size[0] - 1), random.randint(0, dungeon.size[1] - 1)
        return dungeon