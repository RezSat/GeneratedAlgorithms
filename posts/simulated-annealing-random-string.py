import random
import math

def simulated_annealing_string(length, iterations):
    # Generate a random target string
    target = "".join([chr(random.randint(ord('a'), ord('z'))) for _ in range(length)])

    # Generate a random initial string
    current = "".join([chr(random.randint(ord('a'), ord('z'))) for _ in range(length)])

    def calculate_energy(s):
        # Energy is the negative of the number of matching characters
        energy = 0
        for i in range(length):
            if s[i] == target[i]:
                energy -= 1
        return energy

    temperature = 1.0
    cooling_rate = 0.003

    for i in range(iterations):
        # Generate a random neighbor
        index = random.randint(0, length - 1)
        neighbor = list(current)
        neighbor[index] = chr(random.randint(ord('a'), ord('z')))
        neighbor = "".join(neighbor)

        # Calculate energy
        current_energy = calculate_energy(current)
        neighbor_energy = calculate_energy(neighbor)

        # Accept the neighbor based on the Metropolis criterion
        if neighbor_energy < current_energy:
            current = neighbor
        else:
            probability = math.exp((current_energy - neighbor_energy) / temperature)
            if random.random() < probability:
                current = neighbor

        # Cool down the temperature
        temperature *= (1 - cooling_rate)

    return current, target

# Example usage:
# best_string, target_string = simulated_annealing_string(10, 10000)
# print(f"Target string: {target_string}")
# print(f"Best string found: {best_string}")
