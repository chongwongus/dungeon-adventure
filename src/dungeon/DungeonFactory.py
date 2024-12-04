from abc import ABC, abstractmethod
import random
from dungeon.Room import Room
from dungeon.Dungeon import Dungeon


class DungeonFactory(ABC):
    """Factory class for creating Dungeon objects"""

    @abstractmethod
    def create(self, size=(8, 8)):
        """Create a Dungeon object"""
        pass
    
    def place_items(self, dungeon: Dungeon):
        """Places items ensuring pillars are reachable"""
        # Get all rooms except entrance and exit
        available_rooms = [(x, y) for x in range(dungeon.size[0]) for y in range(dungeon.size[1])
                           if (x, y) != dungeon.entrance and (x, y) != dungeon.exit]

        # Place pillars at rooms that are connected to the main path
        pillar_rooms = []
        pillars = list(Room.PILLARS)

        while len(pillar_rooms) < 4:
            room_pos = random.choice(available_rooms)
            x, y = room_pos

            # Check if this room can be reached from entrance
            if dungeon.is_room_reachable(dungeon.entrance, room_pos):
                pillar_rooms.append(room_pos)
                available_rooms.remove(room_pos)
                dungeon.maze[y][x].hasPillar = True
                dungeon.maze[y][x].pillarType = pillars[len(pillar_rooms) - 1]

        # Place other items
        for y in range(dungeon.size[1]):
            for x in range(dungeon.size[0]):
                if (x, y) not in [dungeon.entrance, dungeon.exit] and (x, y) not in pillar_rooms:
                    if random.random() < 0.1:  # 10% chance
                        dungeon.maze[y][x].hasHealthPot = True
                    if random.random() < 0.1:  # 10% chance
                        dungeon.maze[y][x].hasVisionPot = True
                    if random.random() < 0.1:  # 10% chance
                        dungeon.maze[y][x].hasPit = True