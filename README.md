# Conway's Game of Life (Pygame)

This project is an implementation of **Conway's Game of Life** built with [Pygame](https://www.pygame.org/).  
It provides an interactive grid where you can toggle cells, generate random patterns, and watch them evolve according to the rules of the Game of Life.

---

## 🎮 Features
- Click on grid cells to toggle them **alive (yellow)** or **dead (grey)**.
- **Spacebar** → Play / Pause the simulation.
- **C** → Clear the grid.
- **G** → Generate a random pattern of live cells.
- Adjustable speed through the code (`update_frequency`).
- Visual grid with cell boundaries.

---

## 🧩 Rules of the Game
1. Any live cell with fewer than 2 live neighbours dies (underpopulation).
2. Any live cell with 2 or 3 live neighbours lives on.
3. Any live cell with more than 3 live neighbours dies (overpopulation).
4. Any dead cell with exactly 3 live neighbours becomes alive (reproduction).

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/conways-game-of-life.git
   cd conways-game-of-life
