# Maze-Pathfinder
# Maze Generation and Solving with Visualization

## Overview

This project generates a random, solvable maze using **Depth-First Search (DFS)** and solves it using **Breadth-First Search (BFS)**. The process is visualized in real-time using **Matplotlib**.

## Features

- **Maze Generation**: Creates a 21x21 maze using DFS, ensuring it's solvable.
- **Maze Solving**: Uses BFS to find the shortest path from `S` (start) to `X` (end).
- **Real-time Visualization**: Shows the maze-solving process in Matplotlib, with:
  - `#`: Wall (black)
  - ` `: Path (white)
  - `S`: Start (blue)
  - `X`: End (red)
  - `*`: Exploring path (yellow)
  - `+`: Final solution (green)

## Installation

1. **Install Dependencies**:
   Install the required libraries via pip:
   ```bash
   pip install matplotlib numpy

## Run the Project

Execute the script to generate and solve the maze:

```bash
python mazeSolver.py
# How It Works

## 1. Maze Generation

- **Initialization**: The maze is first filled with walls (`#`) in all cells.
- **Depth-First Search (DFS)**: The algorithm starts at the position `(1, 1)` and explores paths by "carving" through walls, ensuring the maze remains solvable.
  - **Random Path Carving**: From each current position, DFS checks all possible directions (up, down, left, right) and picks a random direction to explore further. This helps generate unique maze structures.
  - **Backtracking**: If DFS reaches a dead end, it backtracks to the previous position and tries another direction. This ensures that all possible paths are explored and creates a solvable maze.
- **Start and End Points**: The start point (`S`) is placed at the top-left corner `(1, 1)`, and the end point (`X`) is placed at the bottom-right corner `(height-2, width-2)`. This ensures that there is a clear path from start to finish.

## 2. Maze Solving

- **Breadth-First Search (BFS)**: BFS is used to find the shortest path from the start (`S`) to the end (`X`).
  - **Exploration**: BFS begins at the start point and explores neighboring cells level by level, ensuring the shortest path is found.
  - **Marking the Path**: While BFS explores the maze, it marks the cells it visits with `*`, allowing you to see the progress of the search in real-time.
  - **Solution Path**: Once BFS reaches the end (`X`), it traces back and marks the shortest path with `+` to indicate the solved route.

## 3. Visualization

- **Real-Time Visualization**: The maze generation and solving process are visualized using **Matplotlib**.
  - **Color-Coding**:
    - `#`: Wall (black)
    - ` `: Open path (white)
    - `S`: Start point (blue)
    - `X`: End point (red)
    - `*`: Exploring path (yellow)
    - `+`: Final solution path (green)
  - The visualization updates in real-time, showing how BFS explores the maze and eventually finds the shortest path.

## Example Flow:

1. The maze is initialized with walls.
2. DFS carves out a random, solvable maze.
3. BFS explores the maze, marking its progress.
4. Once BFS reaches the end, it traces back the shortest path and marks it with `+`.



