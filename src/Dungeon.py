import random
from Room import Room

class Dungeon:
    def __init__(self, size=(8, 8), difficulty="easy"):
        self.size = size
        self.maze = [[]]
        self.entrance = None
        self.exit = None
        if difficulty == "easy":
            self.generate_maze_random()
        else:
            self.generate_maze_dfs()
        self.place_items()

    def generate_maze_random(self):
        """Generates maze structure and ensures a path exists to exit and all pillars"""
        # Initialize the maze grid
        self.maze = []
        for y in range(self.size[1]):
            row = []
            for x in range(self.size[0]):
                row.append(Room())
            self.maze.append(row)

        # Set entrance and exit
        self.entrance = (0, 0)
        self.exit = (self.size[0] - 1, self.size[1] - 1)
        self.maze[0][0].isEntrance = True
        self.maze[self.size[1] - 1][self.size[0] - 1].isExit = True

        # First, create paths that connect the whole maze
        self.create_connected_maze()

        # Then place items, ensuring pillars are reachable
        self.place_items()



    def generate_maze_dfs(self):
        """
        Generates maze structure using DFS algorithm to ensure a fully connected maze
        """
        # Initialize the maze grid
        self.maze = []
        for y in range(self.size[1]):
            row = []
            for x in range(self.size[0]):
                row.append(Room())
            self.maze.append(row)

        # Set entrance and exit
        self.entrance = (0, 0)
        self.exit = (self.size[0] - 1, self.size[1] - 1)
        self.maze[0][0].isEntrance = True
        self.maze[self.size[1] - 1][self.size[0] - 1].isExit = True

        # Use DFS to generate paths
        visited = set()
        stack = [self.entrance]

        while stack:
            current = stack[-1]  # Look at current cell
            x, y = current
            visited.add(current)

            # Get all unvisited neighbors
            neighbors = []
            # Check all possible directions: N, S, E, W
            possible_moves = [
                ('N', (x, y - 1)),
                ('S', (x, y + 1)),
                ('E', (x + 1, y)),
                ('W', (x - 1, y))
            ]

            for direction, (nx, ny) in possible_moves:
                if (0 <= nx < self.size[0] and
                        0 <= ny < self.size[1] and
                        (nx, ny) not in visited):
                    neighbors.append((direction, (nx, ny)))

            if neighbors:
                # Randomly choose a neighbor
                direction, next_cell = random.choice(neighbors)
                nx, ny = next_cell

                # Create path between cells (add doors)
                self.maze[y][x].doors[direction] = True
                # Add opposite door to neighbor
                opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
                self.maze[ny][nx].doors[opposite[direction]] = True

                stack.append(next_cell)
            else:
                # No unvisited neighbors, backtrack
                stack.pop()

        # Add a few random connections to make it more interesting
        self.add_random_connections()

    def add_random_connections(self):
        """Add some random connections to make maze more interesting"""
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                # Try to add random east and south connections
                if x < self.size[0] - 1:
                    if random.random() < 0.15:  # 15% chance for extra connections
                        self.maze[y][x].doors['E'] = True
                        self.maze[y][x + 1].doors['W'] = True

                if y < self.size[1] - 1:
                    if random.random() < 0.15:
                        self.maze[y][x].doors['S'] = True
                        self.maze[y + 1][x].doors['N'] = True

    def create_connected_maze(self):
        """Creates a maze where every room is reachable"""
        # Create a path to exit first
        current_x, current_y = 0, 0

        # Move right until near exit
        while current_x < self.size[0] - 1:
            self.maze[current_y][current_x].doors['E'] = True
            self.maze[current_y][current_x + 1].doors['W'] = True
            current_x += 1

        # Move down to exit
        while current_y < self.size[1] - 1:
            self.maze[current_y][current_x].doors['S'] = True
            self.maze[current_y + 1][current_x].doors['N'] = True
            current_y += 1

        # Add some vertical connections for accessibility
        for x in range(self.size[0]):
            for y in range(self.size[1] - 1):
                if random.random() < 0.4:  # 40% chance
                    self.maze[y][x].doors['S'] = True
                    self.maze[y + 1][x].doors['N'] = True

        # Add some horizontal connections for accessibility
        for y in range(self.size[1]):
            for x in range(self.size[0] - 1):
                if random.random() < 0.4:  # 40% chance
                    self.maze[y][x].doors['E'] = True
                    self.maze[y][x + 1].doors['W'] = True

    def place_items(self):
        """Places items ensuring pillars are reachable"""
        # Get all rooms except entrance and exit
        available_rooms = [(x, y) for x in range(self.size[0]) for y in range(self.size[1])
                           if (x, y) != self.entrance and (x, y) != self.exit]

        # Place pillars at rooms that are connected to the main path
        pillar_rooms = []
        pillars = list(Room.PILLARS)

        while len(pillar_rooms) < 4:
            room_pos = random.choice(available_rooms)
            x, y = room_pos

            # Check if this room can be reached from entrance
            if self.is_room_reachable(self.entrance, room_pos):
                pillar_rooms.append(room_pos)
                available_rooms.remove(room_pos)
                self.maze[y][x].hasPillar = True
                self.maze[y][x].pillarType = pillars[len(pillar_rooms) - 1]

        # Place other items
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if (x, y) not in [self.entrance, self.exit] and (x, y) not in pillar_rooms:
                    if random.random() < 0.1:  # 10% chance
                        self.maze[y][x].hasHealthPot = True
                    if random.random() < 0.1:  # 10% chance
                        self.maze[y][x].hasVisionPot = True
                    if random.random() < 0.1:  # 10% chance
                        self.maze[y][x].hasPit = True

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


