import Room as Room

class Dungeon:
    def __init__(self, size=(8, 8)):
        self.size = size
        self.entrance = None
        self.exit = None
