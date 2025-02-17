---
title: Recursive Maze Generator
subtitle: Generates a maze using recursive backtracking.
tags: [maze, generator, recursion, backtracking]
verified: true
---

## Small Description

This algorithm generates a maze using the recursive backtracking algorithm.

## Algorithm Explanation

The algorithm works as follows:

1.  Start with a grid of cells, all initially marked as walls.
2.  Choose a random starting cell and mark it as visited.
3.  While there are unvisited neighbors of the current cell:
    *   Choose a random unvisited neighbor.
    *   Remove the wall between the current cell and the chosen neighbor.
    *   Recursively call the algorithm on the chosen neighbor.

## The Full Code

```python
import random

def recursive_maze(width, height):
    # Initialize the grid with all walls
    maze = [["#" for _ in range(width)] for _ in range(height)]

    def carve_path(x, y):
        maze[y][x] = " "  # Mark current cell as visited

        # Define possible directions (up, down, left, right)
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)  # Randomize the directions

        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # Calculate the coordinates of the neighbor

            # Check if the neighbor is within the grid bounds and is a wall
            if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == "#":
                # Carve a path to the neighbor
                maze[y + dy // 2][x + dx // 2] = " "
                carve_path(nx, ny)  # Recursive call

    # Start carving the path from a random cell
    start_x = random.randint(1, width // 2 - 1) * 2
    start_y = random.randint(1, height // 2 - 1) * 2
    carve_path(start_x, start_y)

    return maze

# Example usage:
# maze = recursive_maze(21, 15)
# for row in maze:
#     print("".join(row))
```

## How to Use

To use the algorithm, call the `recursive_maze` function with the desired width and height of the maze. The function returns a 2D list representing the maze, where "#" represents a wall and " " represents a path.

## Expected Output

The output will be a text-based representation of a maze.

## Conclusion

This "Recursive Maze Generator" algorithm provides a simple and effective way to generate mazes with a recursive backtracking approach.
