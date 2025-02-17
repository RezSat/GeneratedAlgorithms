---
title: Weighted Random Walk on a Grid
subtitle: Simulates a random walk on a grid with weighted probabilities.
tags: [random walk, grid, weighted, simulation]
verified: true
---

# Weighted Random Walk on a Grid

##  Description

This algorithm simulates a random walk on a grid where the probability of moving to a neighboring cell is weighted.

## Algorithm Explanation

The algorithm works as follows:

1.  Initialize a grid of cells.
2.  Start at a random cell in the grid.
3.  Define weights for each possible direction (up, down, left, right).
4.  Iterate for a specified number of steps:
    *   Choose a random direction based on the defined weights.
    *   Move to the neighboring cell in the chosen direction.
    *   If the new cell is outside the grid boundaries, stay in the current cell.
    *   Record the path of the walk.

## The Full Code

```python
import random

def weighted_random_walk(grid_size, steps, weights):
    # Initialize the grid
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    # Start at a random cell
    x = random.randint(0, grid_size - 1)
    y = random.randint(0, grid_size - 1)

    path = [(x, y)]  # Record the starting point

    # Define directions (up, down, left, right)
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for _ in range(steps):
        # Choose a random direction based on the weights
        dx, dy = random.choices(directions, weights)[0]

        # Move to the neighboring cell
        nx, ny = x + dx, y + dy

        # Check if the new cell is within the grid boundaries
        if 0 <= nx < grid_size and 0 <= ny < grid_size:
            x, y = nx, ny
            path.append((x, y))  # Record the new position

    return path

# Example usage:
# grid_size = 10
# steps = 100
# weights = [0.2, 0.3, 0.25, 0.25]  # Up, Down, Left, Right
# path = weighted_random_walk(grid_size, steps, weights)
# print(path)
```

## How to Use

To use the algorithm, call the `weighted_random_walk` function with the desired grid size, the number of steps, and a list of weights for each direction (up, down, left, right). The function returns a list of tuples representing the path of the walk.

## Expected Output

The output will be a list of coordinates representing the path of the random walk on the grid.

## Conclusion

This "Weighted Random Walk on a Grid" algorithm demonstrates how to simulate a random walk with biased probabilities, leading to interesting and predictable patterns.
