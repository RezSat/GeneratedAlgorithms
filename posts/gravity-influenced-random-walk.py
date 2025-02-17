import random

def gravity_influenced_random_walk(grid_size, num_steps):
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    gx = random.uniform(-1, 1)  # Random gravity x component
    gy = random.uniform(-1, 1)  # Random gravity y component

    start_x = random.randint(0, grid_size - 1)
    start_y = random.randint(0, grid_size - 1)
    x, y = start_x, start_y
    grid[x][y] = 1  # Mark starting point as visited

    path = [(x, y)]

    for _ in range(num_steps):
        # Calculate probabilities based on gravity
        up_prob = max(0, -gy)
        down_prob = max(0, gy)
        left_prob = max(0, -gx)
        right_prob = max(0, gx)

        # Normalize probabilities
        total_prob = up_prob + down_prob + left_prob + right_prob
        if total_prob == 0:
            up_prob = down_prob = left_prob = right_prob = 0.25
        else:
            up_prob /= total_prob
            down_prob /= total_prob
            left_prob /= total_prob
            right_prob /= total_prob

        # Choose direction based on probabilities
        rand = random.random()
        if rand < up_prob:
            dx, dy = -1, 0
        elif rand < up_prob + down_prob:
            dx, dy = 1, 0
        elif rand < up_prob + down_prob + left_prob:
            dx, dy = 0, -1
        else:
            dx, dy = 0, 1

        # Move to the next point
        next_x, next_y = x + dx, y + dy

        # Handle boundary conditions (wrap around)
        next_x = next_x % grid_size
        next_y = next_y % grid_size

        x, y = next_x, next_y
        grid[x][y] = 1  # Mark current point as visited
        path.append((x, y))
    return grid, path

if __name__ == "__main__":
    grid_size = 20
    num_steps = 100
    grid, path = gravity_influenced_random_walk(grid_size, num_steps)

    # Print the grid (optional)
    # for row in grid:
    #     print("".join(["*" if cell else "." for cell in row]))

    print("Path:", path)
