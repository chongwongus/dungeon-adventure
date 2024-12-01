from Adventurer import Adventurer
from dungeon.Dungeon import Dungeon
from dungeon.SimpleDungeonFactory import SimpleDungeonFactory
from dungeon.Room import Room


class DungeonAdventure:
    
    dungeon: Dungeon
    
    directions = []
    
    def run(self):
        self.dungeon = SimpleDungeonFactory(32, 32).create()
        print("Welcome to Dungeon Adventure!")
        print("You are in a dark dungeon, and you must find your way out.")
        print("Your goal is to find all four treasures of OOP and make it to the exit.")
        print("Type 'quit' to end the game.")
        adventurer_name = input("What is your name adventurer? ")
        adventurer = Adventurer(adventurer_name)
        print(f"Good luck {adventurer_name}!")

        while True:
            curr_room = self.dungeon.current_room
            for item in curr_room.items:
                adventurer.collect_item(item)
            print(adventurer)
            curr_room.describe()
            options = self.get_options()
            for option in options:
                print(f"< > {option}")
            if curr_room == self.dungeon.exit and len(adventurer.pillarsFound) == 4:
                print("You have found all four treasures of OOP and made it to the exit!")
                break
            command = input("Enter your command: ")
            if command in self.directions:
                self.dungeon.move(command)
            elif command == "quit":
                break
            else:
                print("You can't do that in the Dungeon.")
        print("Game over!")
    
    def get_options(self):
        options = []
        self.directions = []
        if self.dungeon.current_room.North:
            options.append("move north")
            self.directions.append("north")
        if self.dungeon.current_room.South:
            options.append("move south")
            self.directions.append("south")
        if self.dungeon.current_room.East:
            options.append("move east")
            self.directions.append("east")
        if self.dungeon.current_room.West:
            options.append("move  west")
            self.directions.append("west")
        return options