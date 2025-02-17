import random

def cellular_automata(size, generations):
    # Initialize the cells with random states
    cells = [random.randint(0, 1) for _ in range(size)]

    # Generate a random rule set (neighborhood configuration -> new state)
    rules = {}
    for i in range(8):  # 8 possible neighborhood configurations (2^3)
        rules[bin(i)[2:].zfill(3)] = random.randint(0, 1)

    def get_neighborhood(index):
        # Get the states of the cell and its neighbors
        left = cells[index - 1] if index > 0 else cells[-1]  # Wrap around
        right = cells[index + 1] if index < size - 1 else cells[0]  # Wrap around
        center = cells[index]
        return str(left) + str(center) + str(right)

    # Run the simulation for the specified number of generations
    for _ in range(generations):
        new_cells = cells[:]  # Create a copy to store the new generation

        for i in range(size):
            neighborhood = get_neighborhood(i)
            new_cells[i] = rules[neighborhood]

        cells = new_cells
        print("".join(["#" if cell == 1 else " " for cell in cells])) # Display the generation

# Example usage:
# cellular_automata(50, 20)
