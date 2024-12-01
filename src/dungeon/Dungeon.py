from dungeon.Room import Room
from events.Events import PLAYER_EVENTS
from events.Observer import Observer

class Dungeon(Observer):
    rooms = [[]]
    current_room: Room = None
    
    def __init__(self, size=(8, 8)):
        self.size = size
        self.rooms = [[Room() for y in range(size[1])] for x in range(size[0])]
        self.current_room = self.rooms[0][0]
        self.entrance = None
        self.exit = None

    def __str__(self):
        """
        :return: ASCII representation of dungeon
        """
        result = ""
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                result += str(self.rooms[x][y])
            result += "\n"
        return result
    
    def get_room(self, x, y):
        """
        Get the room at the given coordinates
        :param x: x coordinate
        :param y: y coordinate
        :return: Room
        """
        return self.rooms[x][y]
    
    def set_room(self, x, y, room):
        """
        Set the room at the given coordinates
        :param x: x coordinate
        :param y: y coordinate
        :param room: Room
        :return: None
        """
        self.rooms[x][y] = room
    
    def update(self, data):
        if data == PLAYER_EVENTS.vision:
            self.print_vision()
            
    def print_vision(self):
        """
        Print 8 rooms around the player
        """
        x, y = self.current_room
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < self.size[0] and 0 <= y + j < self.size[1]:
                    print(self.rooms[x + i][y + j])
                else:
                    print(" ")
            print("\n")
            
    def notify(self, message):
        return super().notify(message)