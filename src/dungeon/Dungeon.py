import random
from dungeon.Room import Room

class Dungeon:
    def __init__(self, size=(8, 8)):
        self.size = size
        self.maze = [[]]
        self.entrance = None
        self.exit = None

    def is_room_reachable(self, start, target):
        """Checks if there is a path between start and target positions"""
        visited = set()
        stack = [start]

        while stack:
            current = stack.pop()
            if current == target:
                return True

            if current not in visited:
                visited.add(current)
                x, y = current

                # Check all possible moves from current position
                if self.maze[y][x].doors['N'] and y > 0:
                    stack.append((x, y - 1))
                if self.maze[y][x].doors['S'] and y < self.size[1] - 1:
                    stack.append((x, y + 1))
                if self.maze[y][x].doors['E'] and x < self.size[0] - 1:
                    stack.append((x + 1, y))
                if self.maze[y][x].doors['W'] and x > 0:
                    stack.append((x - 1, y))

        return False

    def get_room(self, x, y):
        if 0 <= x < self.size[0] and 0 <= y < self.size[1]:
            return self.maze[y][x]
        return None

    def __str__(self):
        result = []
        for row in self.maze:
            # Split each room into its three lines
            room_lines = [str(room).split('\n') for room in row]

            # Add empty line between rows of rooms
            if result:  # If not the first row
                result.append('     ' * len(row))  # Add spacing between rows

            # Combine rooms horizontally for each line
            for i in range(3):  # Each room has 3 lines
                result.append('  '.join(room[i] for room in room_lines))

        return '\n'.join(result)

    def is_valid_move(self, current_pos, direction):
        """Checks if move from current position in given direction is valid"""
        x, y = current_pos
        current_room = self.get_room(x, y)

        # First check if there's a door in that direction
        if not current_room or not current_room.doors[direction]:
            return False

        # Then check if the destination is within bounds
        new_x, new_y = x, y
        if direction == 'N':
            new_y -= 1
        elif direction == 'S':
            new_y += 1
        elif direction == 'E':
            new_x += 1
        elif direction == 'W':
            new_x -= 1

        # Check if new position is within bounds
        if not (0 <= new_x < self.size[0] and 0 <= new_y < self.size[1]):
            return False

        # Check if destination room has corresponding door
        dest_room = self.get_room(new_x, new_y)
        opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
        if not dest_room.doors[opposite[direction]]:
            return False

        return True

    def print_debug(self):
        """Prints detailed info about dungeon state"""
        print(f"Dungeon size: {self.size}")
        print(f"Entrance: {self.entrance}")
        print(f"Exit: {self.exit}")

        # Print room contents
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                room = self.maze[y][x]
                print(f"\nRoom ({x},{y}):")
                print(f"Doors: {room.doors}")
                if room.isEntrance: print("ENTRANCE")
                if room.isExit: print("EXIT")
                if room.hasPillar: print(f"Pillar: {room.pillarType}")
                if room.hasHealthPot: print("Health Potion")
                if room.hasVisionPot: print("Vision Potion")
                if room.hasPit: print("Pit")


