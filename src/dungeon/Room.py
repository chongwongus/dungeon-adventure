from items.Item import Item


class Room:
    EMPTY = ' '
    PIT = 'X'
    ENTRANCE = 'i'
    EXIT = 'o'
    VISION_POT = 'V'
    HEALTH_POT = 'H'
    MULTIPLE_ITEMS = 'M'    
    
    North = None
    East = None
    South = None
    West = None
    
    items = []
    
    def __init__(self):
        self.hasPit = False
        self.isEntrance = False
        self.isExit = False
        self.items: list[Item] = []


    def __str__(self):
        """
        :return: ASCII representation of room
        """
        top = '*' + ('-' if self.North else '*') + '\n'
        mid = (('|' if self.West else '*') +
               self.get_room_display() +
               ('|' if self.East else '*') + '\n')
        bot = '*' + ('-' if self.South else '*') + '*'
        return top + mid + bot

    def get_room_display(self):
        """

        :return: char representing room contents
        """
        if self.isEntrance:
            return self.ENTRANCE
        if self.isExit:
            return self.EXIT

        items = sum([self.hasPit, self.hasHealthPot, self.hasVisionPot, self.hasPillar])

        if items > 1:
            return self.MULTIPLE_ITEMS
        elif self.hasPit:
            return self.PIT
        else:
            return self.EMPTY
        
    def describe(self):
        """
        Describe the room
        """
        if self.hasPit:
            print("You see a pit in the room.")
        for item in self.items:
            print(f"You see a {item.name} in the room.")
        if self.isEntrance:
            print("You are at the entrance to the dungeon.")
        if self.isExit:
            print("You are at the exit to the dungeon.")
        if not any([self.hasPit, self.items, self.isEntrance, self.isExit]):
            print("The room is empty.")
        if self.North:
            print("There is a door to the North.")
        if self.East:
            print("There is a door to the East.")
        if self.South:
            print("There is a door to the South.")
        if self.West:
            print("There is a door to the West.")