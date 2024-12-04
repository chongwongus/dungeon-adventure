import tkinter as tk
from tkinter import ttk, messagebox
import random
from dungeon.DFSDungeonFactory import DFSDungeonFactory
from dungeon.EasyDungeonFactory import EasyDungeonFactory
from dungeon.Dungeon import Dungeon
from Adventurer import Adventurer
from dungeon.DungeonFactory import DungeonFactory


class DungeonGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dungeon Adventure")
        self.root.geometry("800x600")

        self.dungeon: Dungeon = None
        self.player = None
        self.show_start_screen()

    def show_start_screen(self):
        '''Show the start screen'''
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create start screen
        start_frame = ttk.Frame(self.root, padding="20")
        start_frame.pack(expand=True)

        ttk.Label(start_frame, text="Dungeon Adventure",
                  font=('Arial', 24, 'bold')).pack(pady=20)

        # Name entry
        ttk.Label(start_frame, text="Enter your name:").pack(pady=10)
        self.name_entry = ttk.Entry(start_frame)
        self.name_entry.pack(pady=10)

        # Maze size entry
        size_frame = ttk.Frame(start_frame)
        size_frame.pack(pady=10)

        ttk.Label(size_frame, text="Maze Size:").pack()
        self.size_entry = ttk.Entry(size_frame, width=10)
        self.size_entry.insert(0, "8")  # Default value
        self.size_entry.pack(pady=5)

        ttk.Button(start_frame, text="Start Game",
                   command=self.validate_and_start).pack(pady=20)

        difficulty_frame = ttk.Frame(start_frame)
        difficulty_frame.pack(pady=10)

        ttk.Label(difficulty_frame, text="Difficulty:").pack()
        self.difficulty_var = tk.StringVar(value="easy")
        ttk.Radiobutton(difficulty_frame, text="Easy (Random Generation)",
                        variable=self.difficulty_var,
                        value="easy").pack()
        ttk.Radiobutton(difficulty_frame, text="Hard (DFS Generation)",
                        variable=self.difficulty_var,
                        value="hard").pack()

    def validate_and_start(self):
        """Validates inputs before starting game"""
        name = self.name_entry.get()
        if not name:
            messagebox.showwarning("Warning", "Please enter a name!")
            return

        try:
            size = int(self.size_entry.get())
            if size > 51:
                messagebox.showwarning("Warning", "Please enter a size below 50!")
                return
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid number!")
            return

        difficulty = self.difficulty_var.get()
        
        dungeonFactory:DungeonFactory = None
        if difficulty == "easy":
            dungeonFactory = EasyDungeonFactory() 
        else:
            dungeonFactory = DFSDungeonFactory()
            
        self.dungeon = dungeonFactory.create((size, size))
        self.player = Adventurer(name)
        self.player.currLocation = self.dungeon.entrance

        self.setup_game_screen()

    def setup_game_screen(self):
        '''Setup the main game screen'''
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create main game layout
        self.cell_size = 50
        self.padding = 5

        # Game area (left side)
        game_frame = ttk.Frame(self.root, padding="10")
        game_frame.grid(row=0, column=0, sticky="nsew")

        # Calculate canvas size for 8x8 maze
        canvas_size = (self.cell_size + self.padding) * 8
        self.canvas = tk.Canvas(game_frame, width=canvas_size,
                                height=canvas_size, bg='grey')
        self.canvas.pack()

        # Control panel (right side)
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.grid(row=0, column=1, sticky="nsew")

        # Player info
        self.player_info = ttk.Label(control_frame, text="")
        self.player_info.pack(pady=10)

        # Action buttons
        ttk.Button(control_frame, text="Use Health Potion",
                   command=self.use_health_potion).pack(pady=5)
        ttk.Button(control_frame, text="Use Vision Potion",
                   command=self.use_vision_potion).pack(pady=5)

        # Add Restart button
        ttk.Button(control_frame, text="Restart Game",
                   command=self.show_start_screen).pack(pady=20)

        # Add event log
        log_frame = ttk.LabelFrame(control_frame, text="Event Log", padding="5")
        log_frame.pack(pady=10, fill="both", expand=True)

        self.event_log = tk.Text(log_frame, width=30, height=10, wrap="word")
        self.event_log.pack(padx=5, pady=5, fill="both", expand=True)

        # Configure grid weights
        self.root.grid_columnconfigure(0, weight=3)
        self.root.grid_columnconfigure(1, weight=1)

        # Bind movement keys
        self.root.bind('<w>', lambda e: self.try_move('N'))
        self.root.bind('<s>', lambda e: self.try_move('S'))
        self.root.bind('<a>', lambda e: self.try_move('W'))
        self.root.bind('<d>', lambda e: self.try_move('E'))
        self.root.bind('<Up>', lambda e: self.try_move('N'))
        self.root.bind('<Down>', lambda e: self.try_move('S'))
        self.root.bind('<Left>', lambda e: self.try_move('W'))
        self.root.bind('<Right>', lambda e: self.try_move('E'))

        # Initial display update
        self.update_display()

    def add_event_message(self, message):
        """Adds a message to the event log"""
        self.event_log.insert("1.0", message + "\n\n")
        self.event_log.see("1.0")  # Scroll to top

    def update_display(self):
        '''Update the game display'''
        self.canvas.delete('all')

        # Draw all rooms
        for y in range(self.dungeon.size[1]):
            for x in range(self.dungeon.size[0]):
                self.draw_room(x, y, self.dungeon.get_room(x, y))

        # Update player info
        self.player_info.config(text=str(self.player))

    def draw_room(self, x, y, room):
        '''Draw a single room on the canvas'''
        # Calculate pixel coordinates
        px = x * (self.cell_size + self.padding)
        py = y * (self.cell_size + self.padding)

        # Draw room background
        if not room.visited:
            color = 'dark grey'
        elif room.isEntrance:
            color = 'green'
        elif room.isExit:
            color = 'red'
        else:
            color = 'white'

        self.canvas.create_rectangle(px, py,
                                     px + self.cell_size,
                                     py + self.cell_size,
                                     fill=color, outline='black')

        # Draw doors
        door_width = 10
        if room.doors['N']:
            self.canvas.create_rectangle(px + self.cell_size / 2 - door_width / 2, py,
                                         px + self.cell_size / 2 + door_width / 2, py + door_width,
                                         fill='brown')
        if room.doors['S']:
            self.canvas.create_rectangle(px + self.cell_size / 2 - door_width / 2,
                                         py + self.cell_size - door_width,
                                         px + self.cell_size / 2 + door_width / 2,
                                         py + self.cell_size,
                                         fill='brown')
        if room.doors['W']:
            self.canvas.create_rectangle(px, py + self.cell_size / 2 - door_width / 2,
                                         px + door_width, py + self.cell_size / 2 + door_width / 2,
                                         fill='brown')
        if room.doors['E']:
            self.canvas.create_rectangle(px + self.cell_size - door_width,
                                         py + self.cell_size / 2 - door_width / 2,
                                         px + self.cell_size, py + self.cell_size / 2 + door_width / 2,
                                         fill='brown')

        # Draw room contents if visited
        if room.visited:
            text = ''
            if room.hasPillar:
                text = room.pillarType
            elif room.hasPit:
                text = 'PIT'
            elif room.hasHealthPot:
                text = 'HP'
            elif room.hasVisionPot:
                text = 'VP'

            if text:
                self.canvas.create_text(px + self.cell_size / 2,
                                        py + self.cell_size / 2,
                                        text=text)

        # Draw player position
        if (x, y) == self.player.currLocation:
            self.canvas.create_oval(px + self.cell_size / 4, py + self.cell_size / 4,
                                    px + 3 * self.cell_size / 4, py + 3 * self.cell_size / 4,
                                    fill='blue')

    def try_move(self, direction):
        '''Try to move player in given direction'''
        if self.dungeon.is_valid_move(self.player.currLocation, direction):
            self.player.move(direction)
            self.process_room()
            self.update_display()
            self.check_game_state()

    def process_room(self):
        '''Process current room's contents'''
        x, y = self.player.currLocation
        current_room = self.dungeon.get_room(x, y)
        current_room.visited = True

        if current_room.hasPit:
            damage = random.randint(1, 20)
            self.player.take_dmg(damage)
            self.add_event_message(f"You fell into a pit! Took {damage} damage!")

        if current_room.hasHealthPot:
            self.player.healingPot += 1
            current_room.hasHealthPot = False
            self.add_event_message("Found a health potion!")

        if current_room.hasVisionPot:
            self.player.visionPot += 1
            current_room.hasVisionPot = False
            self.add_event_message("Found a vision potion!")

        if current_room.hasPillar:
            self.player.add_pillar(current_room.pillarType)
            current_room.hasPillar = False
            self.add_event_message(f"Found the Pillar of {current_room.pillarType}!")

    def use_health_potion(self):
        '''Uses health potion to heal player'''
        if self.player.use_healing_pot():
            self.add_event_message(f"Used healing potion! HP is now {self.player.hp}")
            self.update_display()
        else:
            self.add_event_message("No healing potions available!")

    def use_vision_potion(self):
        '''Uses vision potion to reveal surrounding rooms'''
        if self.player.use_vision_pot():
            x, y = self.player.currLocation
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    room = self.dungeon.get_room(x + dx, y + dy)
                    if room:
                        room.visited = True
            self.add_event_message("Used vision potion! Surrounding rooms revealed.")
            self.update_display()
        else:
            self.add_event_message("No vision potions available!")

    def check_game_state(self):
        '''Check if game is over'''
        if self.player.hp <= 0:
            messagebox.showinfo("Game Over", "You have died!")
            self.show_start_screen()
        elif (self.player.currLocation == self.dungeon.exit and
              len(self.player.pillarsFound) == 4):
            messagebox.showinfo("Congratulations", "You've won the game!")
            self.show_start_screen()


if __name__ == "__main__":
    root = tk.Tk()
    gui = DungeonGUI(root)
    root.mainloop()