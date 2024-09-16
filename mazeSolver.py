from queue import Queue
import matplotlib.pyplot as plt
import numpy as np
import random


# Maze size
MAZE_HEIGHT = 21
MAZE_WIDTH = 21

# Directions (Down, Up, Right, Left)
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def generate_maze(height, width):
    """Generates a random solvable maze using an iterative DFS (stack-based)."""
    # Initialize the maze filled with walls
    maze = []
    for row in range(height):
        maze.append(["#"] * width)  # Fill each row with walls ('#')
    
    # Stack to store cells for backtracking
    stack = []
    
    # Starting point
    start_x = 1
    start_y = 1
    maze[start_x][start_y] = " "  # Mark the start as a path
    stack.append((start_x, start_y))  # Push the start cell onto the stack
    
    # While there are cells to explore
    while len(stack) > 0:
        # Pop the last cell from the stack (DFS)
        x, y = stack.pop()
        
        # Find all valid unvisited neighbors (2 steps away)
        neighbors = []
        for direction in DIRECTIONS:
            dx, dy = direction
            nx = x + dx * 2  # Neighbor's x-coordinate
            ny = y + dy * 2  # Neighbor's y-coordinate
            
            # Ensure the neighbor is within bounds and not yet visited
            if 0 <= nx < height and 0 <= ny < width and maze[nx][ny] == "#":
                neighbors.append((nx, ny, dx, dy))  # Store the neighbor and direction
        
        # If there are valid neighbors
        if len(neighbors) > 0:
            # Push the current cell back onto the stack (for backtracking)
            stack.append((x, y))
            
            # Randomly choose one of the neighbors
            chosen_neighbor = random.choice(neighbors)
            nx, ny, dx, dy = chosen_neighbor
            
            # Remove the wall between the current cell and the chosen neighbor
            maze[x + dx][y + dy] = " "  # Remove the wall
            maze[nx][ny] = " "  # Mark the neighbor as a path
            
            # Push the neighbor onto the stack to continue exploring
            stack.append((nx, ny))
    
    # Mark the start and end points
    maze[1][1] = "S"  # Start point
    maze[height - 2][width - 2] = "X"  # End point
    
    return maze


# Function to display the maze
def display_maze(maze):
    maze_row = ''  # Initialize an empty string to construct each row of the maze
    
    # Outer loop: Iterate through each row in the maze
    for row in maze:
        # Inner loop: Iterate through each character in the current row (each cell)
        for index in row:
            maze_row += ' ' + index  # Add a space and the current character (cell) to the row string
        
        print(maze_row)  # Print the constructed row
        maze_row = ' '  # Reset the maze_row string for the next row

# Function to find a node in the maze
def find_node(maze, node):
    numRows = len(maze)  # Get the number of rows
    numCols = len(maze[0])  # Get the number of columns
    for row in range(numRows):  # Iterate over each row
        for col in range(numCols):  # Iterate over each column
            if maze[row][col] == node:  # Check if the cell is the node
                return (row, col)  # Return the coordinates if node is found

# Function to transform the maze into a graph
def transform_to_graph(maze):
    graph = {}  # Initialize an empty dictionary to store the graph
    numRows = len(maze)  # Get the number of rows
    numCols = len(maze[0])  # Get the number of columns
    
    # Outer loop: Iterate over each row
    for row in range(numRows):
        # Inner loop: Iterate over each column
        for col in range(numCols):
            if maze[row][col] != "#":  # If the cell is not a wall
                available_nodes = []
                
                # Check DOWN direction
                if row + 1 < numRows and maze[row + 1][col] != '#':
                    available_nodes.append((row + 1, col))
                
                # Check UP direction
                if row - 1 >= 0 and maze[row - 1][col] != '#':
                    available_nodes.append((row - 1, col))
                
                # Check RIGHT direction
                if col + 1 < numCols and maze[row][col + 1] != '#':
                    available_nodes.append((row, col + 1))
                
                # Check LEFT direction
                if col - 1 >= 0 and maze[row][col - 1] != '#':
                    available_nodes.append((row, col - 1))
                
                # Add the current cell and its neighbors to the graph
                graph[(row, col)] = available_nodes
    
    return graph  # Return the graph

# Function to solve the maze using Breadth-First Search (BFS)
def solve_maze(maze, graph, start_node, end_node, ax):
    visited = []  # List to keep track of visited nodes (cells that have already been explored)
    start_path = [start_node]  # Initialize the first path with just the start node
    q = Queue()  # Initialize the queue (FIFO) to store paths for BFS
    q.put(start_path)  # Add the initial path (start node) to the queue
    
    # While there are paths to explore in the queue
    while not q.empty():
        path = q.get()  # Dequeue the next path (this shrinks the queue)
        
        # Get the current node (the last node in the path)
        current_node = path[-1]
        
        # Get the neighbors of the current node from the graph
        neighbours = graph[current_node]
        
        # Mark the cells in the current path with '*' to show exploration
        for coord in path:
            row, col = coord
            if maze[row][col] not in ['S', 'X', '+']:  # Don't overwrite start, end, or final path
                maze[row][col] = '*'
        
        # Visualize current exploration
        visualize_maze(maze, ax, title="Solving Maze")
        
        # If the neighbor is the end node (we found the solution)
        if current_node == end_node:
            for coord in path:
                row, col = coord
                maze[row][col] = '+'  # Mark the solution path with '+'
            return maze  # Return the solved maze with the path marked
            
        # Explore each neighbor of the current node
        for n in neighbours:
            if n not in visited:  # If the neighbor has not been visited yet
                visited.append(n)  # Mark the neighbor as visited
                new_path = path + [n]  # Create a new path that includes this neighbor
                q.put(new_path)  # Add the new path to the queue for further exploration
    # If no path is found, return the maze as-is and print a message
    print("No path found from start point to endpoint.")
    return maze
# Function to display the maze graphically
def visualize_maze(maze, ax, title="Maze"):
    """
    This function converts the maze into a color-coded format and visualizes it using matplotlib.
    It updates the plot in real-time during exploration.
    """
    # Create a dictionary that maps characters to colors
    cmap = {'#': 'black',  # Walls are represented by black
            ' ': 'white',  # Open paths are represented by white
            'S': 'blue',   # Start point is represented by blue
            'X': 'red',    # End point is represented by red
            '+': 'green',  # Solution path is represented by green
            '*': 'yellow'}  # Cells being explored are represented by yellow

    # Clear previous plot
    ax.clear()

    # Set the title of the plot
    ax.set_title(title)

    # Loop through each row in the maze
    for r in range(len(maze)):
        # Loop through each cell in the row
        for c in range(len(maze[r])):
            # Get the color for the current cell from the colormap (cmap)
            face_color = cmap[maze[r][c]]
            
            # Define the position and size of the rectangle
            # c = column index (x-axis)
            # len(maze) - r - 1 = row index, flipped (y-axis)
            x_position = c  # The horizontal position of the cell
            y_position = len(maze) - r - 1  # The vertical position, flipped to draw from top to bottom
            rectangle_width = 1  # Each rectangle (cell) has a width of 1
            rectangle_height = 1  # Each rectangle (cell) has a height of 1
            
            # Create the rectangle object
            rect = plt.Rectangle(
                (x_position, y_position),  # Position (x, y) of the rectangle
                rectangle_width,  # Width of the rectangle
                rectangle_height,  # Height of the rectangle
                facecolor=face_color  # Set the color of the rectangle
            )
            
            # Add the rectangle to the plot
            ax.add_patch(rect)  # Place the rectangle on the current axes (ax) for visualization

    # Set plot limits to match maze dimensions
    plt.xlim([0, len(maze[0])])
    plt.ylim([0, len(maze)])

    # Ensure aspect ratio remains equal (square cells)
    ax.set_aspect('equal', adjustable='box')

    # Remove axis ticks and labels
    plt.axis('off')

    # Pause to allow updates to be seen during exploration
    plt.pause(0.0000000000000001)

# Generate a random solvable maze
maze = generate_maze(MAZE_HEIGHT, MAZE_WIDTH)

# Display the generated maze in the console
print("Generated Maze:")
display_maze(maze)
# Find the start node ('S') and the end node ('X') in the maze
start_node = find_node(maze, 'S')
end_node = find_node(maze, 'X')

# Transform the maze into a graph (adjacency list)
graph = transform_to_graph(maze)

# Set up the matplotlib figure and axis for real-time visualization
fig, ax = plt.subplots(figsize=(6, 6))

# Solve the maze using BFS, with real-time visualization
solved_maze = solve_maze(maze, graph, start_node, end_node, ax)

# Show the final solved maze
visualize_maze(solved_maze, ax, title="Solved Maze")

# Keep the plot window open after solving
plt.show()
