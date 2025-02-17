---
title: Simulated Annealing for Random String Optimization
subtitle: Uses simulated annealing to find a string close to a random target.
tags: [simulated annealing, optimization, string, random]
verified: true
---

# Simulated Annealing for Random String Optimization

## Description

This algorithm uses simulated annealing to find a string that is as close as possible to a randomly generated target string. Closeness is defined by the number of matching characters.

## Algorithm Explanation

The algorithm works as follows:

1.  Generate a random target string of a specified length.
2.  Generate a random initial string of the same length.
3.  Define a "temperature" parameter that controls the probability of accepting worse solutions.
4.  Iterate for a specified number of steps:
    *   Generate a random neighbor of the current string by randomly changing one character.
    *   Calculate the "energy" of the current string and the neighbor string. Energy is defined as the negative of the number of matching characters with the target string (so higher matching characters means lower energy).
    *   If the neighbor string has lower energy (better match), accept it.
    *   If the neighbor string has higher energy (worse match), accept it with a probability that depends on the temperature and the energy difference.
    *   Decrease the temperature.

## The Full Code

```python
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
```

## How to Use

To use the algorithm, call the `simulated_annealing_string` function with the desired string length and the number of iterations. The function returns the best string found and the target string.

## Expected Output

The output will be the target string and the best string found by the simulated annealing algorithm. The best string should be relatively close to the target string, with a significant number of matching characters.

## Conclusion

This "Simulated Annealing for Random String Optimization" algorithm demonstrates how simulated annealing can be used to find approximate solutions to complex optimization problems, even when the search space is large and random.
