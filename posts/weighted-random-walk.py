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
