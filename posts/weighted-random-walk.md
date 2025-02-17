---
title: Weighted Random Walk
subtitle: Simulates a random walk with weighted probabilities for each direction.
tags: [random walk, weighted, simulation, visualization, algorithm]
verified: false
---

## Title: Weighted Random Walk

## Description:
This algorithm simulates a random walk in two dimensions, where the probability of moving in each direction (North, South, East, West) can be weighted.

## Algorithm Explanation:
The algorithm takes the length of the walk and a dictionary of weights as input. The weights dictionary specifies the probability of moving in each direction. The algorithm then iterates through the specified number of steps, choosing a direction at random based on the weights and updating the current position accordingly.

## The Full Code:
```python
import random

def weighted_random_walk(length, weights):
    """
    Simulates a random walk with weighted probabilities for each direction.

    Args:
        length: The number of steps in the random walk.
        weights: A dictionary mapping directions ('N', 'S', 'E', 'W') to probabilities.
               Probabilities must sum to 1.

    Returns:
        A list of tuples representing the coordinates (x, y) of the walk at each step.
    """
    directions = list(weights.keys())
    probabilities = list(weights.values())

    if sum(probabilities) != 1:
        raise ValueError("Probabilities must sum to 1.")

    x, y = 0, 0
    path = [(x, y)]

    for _ in range(length):
        direction = random.choices(directions, probabilities)[0]

        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1

        path.append((x, y))

    return path


if __name__ == '__main__':
    # Example usage
    weights = {
        'N': 0.25,
        'S': 0.25,
        'E': 0.25,
        'W': 0.25
    }

    length = 100

    path = weighted_random_walk(length, weights)

    print("Random walk path:")
    for point in path:
        print(point)


    # Visualization (requires matplotlib)
    try:
        import matplotlib.pyplot as plt

        x_coords, y_coords = zip(*path)

        plt.plot(x_coords, y_coords)
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.title("Weighted Random Walk")
        plt.grid(True)
        plt.show()

    except ImportError:
        print("Matplotlib is not installed. Please install it to visualize the random walk.")
```

## How to Use:
The code can be run directly from the command line. To visualize the random walk, you need to have the `matplotlib` library installed. If you don't have it installed, you can install it using pip:
```bash
pip install matplotlib
```

## Expected Output:
The code will first print the coordinates of each step in the random walk. If `matplotlib` is installed, it will also display a plot of the random walk.

## Conclusion:
The Weighted Random Walk algorithm provides a way to simulate a random walk with weighted probabilities for each direction. The visualization helps to understand the behavior of the walk.
