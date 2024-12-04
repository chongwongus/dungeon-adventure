import random
from dungeon.Room import Room
from dungeon.Dungeon import Dungeon
from dungeon.DungeonFactory import DungeonFactory


class DFSDungeonFactory(DungeonFactory):
    
    def create(self, size=(8, 8)):
        '''Create a Dungeon object'''
        self.dungeon = Dungeon(size)
        self.generate_maze_dfs()
        return self.dungeon
        
    def generate_maze_dfs(self):
        """
        Generates maze structure using DFS algorithm to ensure a fully connected maze
        """
        # Initialize the maze grid
        self.dungeon.maze = []
        for y in range(self.dungeon.size[1]):
            row = []
            for x in range(self.dungeon.size[0]):
                row.append(Room())
            self.dungeon.maze.append(row)

        # Set entrance and exit
        self.dungeon.entrance = (0, 0)
        self.dungeon.exit = (self.dungeon.size[0] - 1, self.dungeon.size[1] - 1)
        self.dungeon.maze[0][0].isEntrance = True
        self.dungeon.maze[self.dungeon.size[1] - 1][self.dungeon.size[0] - 1].isExit = True

        # Use DFS to generate paths
        visited = set()
        stack = [self.dungeon.entrance]

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
                if (0 <= nx < self.dungeon.size[0] and
                        0 <= ny < self.dungeon.size[1] and
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
                self.dungeon.maze[ny][nx].doors[opposite[direction]] = True

                stack.append(next_cell)
            else:
                # No unvisited neighbors, backtrack
                stack.pop()

        # Add a few random connections to make it more interesting
        self.add_random_connections()
        self.place_items(self.dungeon)

    def add_random_connections(self):
        """Add some random connections to make maze more interesting"""
        for y in range(self.dungeon.size[1]):
            for x in range(self.dungeon.size[0]):
                # Try to add random east and south connections
                if x < self.dungeon.size[0] - 1:
                    if random.random() < 0.15:  # 15% chance for extra connections
                        self.dungeon.maze[y][x].doors['E'] = True
                        self.dungeon.maze[y][x + 1].doors['W'] = True

                if y < self.size[1] - 1:
                    if random.random() < 0.15:
                        self.dungeon.maze[y][x].doors['S'] = True
                        self.dungeon.maze[y + 1][x].doors['N'] = True