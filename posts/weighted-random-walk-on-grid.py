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

if __name__ == "__main__":
    grid_size = 10
    steps = 100
    weights = [0.2, 0.3, 0.25, 0.25]  # Up, Down, Left, Right
    path = weighted_random_walk(grid_size, steps, weights)
    print(path)
