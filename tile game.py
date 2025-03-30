import tkinter as tk
import random
import time

TILE_SIZE = 300  
GRID_SIZE = 3  
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'] * 2  # Duplicate letters for matching

class LargeTileGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Large Tile Matching Game")
        self.root.geometry(f"{TILE_SIZE * GRID_SIZE}x{TILE_SIZE * GRID_SIZE}")

        # Shuffle and assign letters to tiles
        self.letters = random.sample(LETTERS, GRID_SIZE**2)
        self.buttons = []
        self.selected = []
        self.matched = set()
        
        self.create_tiles()

    def create_tiles(self):
        """Create the grid of tiles."""
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                btn = tk.Button(
                    self.root,
                    text="?",
                    font=("Arial", 50, "bold"),
                    width=5,
                    height=3,
                    bg="black",
                    fg="white",
                    command=lambda r=i, c=j: self.reveal_tile(r, c)
                )
                btn.grid(row=i, column=j, sticky="nsew")
                row.append(btn)
            self.buttons.append(row)

    def reveal_tile(self, row, col):
        """Reveal a tile when clicked."""
        if (row, col) in self.matched or len(self.selected) == 2:
            return  # Ignore clicks if already matched or two tiles are selected

        self.buttons[row][col].config(text=self.letters[row * GRID_SIZE + col], bg="gray")
        self.selected.append((row, col))

        if len(self.selected) == 2:
            self.root.after(1000, self.check_match)

    def check_match(self):
        """Check if two selected tiles match."""
        r1, c1 = self.selected[0]
        r2, c2 = self.selected[1]

        if self.letters[r1 * GRID_SIZE + c1] == self.letters[r2 * GRID_SIZE + c2]:
            self.matched.add((r1, c1))
            self.matched.add((r2, c2))
        else:
            self.buttons[r1][c1].config(text="?", bg="black")
            self.buttons[r2][c2].config(text="?", bg="black")

        self.selected.clear()

if __name__ == "__main__":
    root = tk.Tk()
    game = LargeTileGame(root)
    root.mainloop()
