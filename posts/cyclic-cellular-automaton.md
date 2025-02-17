---
title: Cyclic Cellular Automaton
subtitle: Implements a cyclic cellular automaton.
tags: [cellular automaton, cyclic, simulation, algorithm]
verified: true
---

## Title: Cyclic Cellular Automaton

## Description:
This algorithm implements a cyclic cellular automaton.  Each cell in the automaton has a state, and the state of each cell is updated based on the states of its neighbors. The update rule is that if the left neighbor has the same state as the current cell, the current cell's state increments to the next state (wrapping around).

## Algorithm Explanation:
The algorithm takes the size of the automaton, the number of states each cell can have, and the number of iterations to run as input. It initializes the automaton with a random state, and then iterates through the specified number of iterations, updating the state of each cell at each iteration.  Cyclic boundary conditions are used, meaning the left-most cell is a neighbor of the right-most cell and vice versa.

## The Full Code:
```python
import random

def cyclic_cellular_automaton(size, num_states, iterations, initial_state=None):
    """
    Implements a cyclic cellular automaton.

    Args:
        size: The size of the automaton (number of cells).
        num_states: The number of states each cell can have. States are integers from 0 to num_states - 1.
        iterations: The number of iterations to run the automaton.
        initial_state: (optional) A list representing the initial state of the automaton.
                       If None, a random initial state is generated.

    Returns:
        A list of lists, where each inner list represents the state of the automaton at a given iteration.
    """

    if initial_state is None:
        # Generate a random initial state
        current_state = [random.randint(0, num_states - 1) for _ in range(size)]
    else:
        if len(initial_state) != size:
            raise ValueError("Initial state size does not match the specified size.")
        current_state = initial_state

    history = [current_state.copy()]  # Store the initial state

    for _ in range(iterations):
        next_state = []
        for i in range(size):
            # Determine neighbors (cyclic boundary conditions)
            left_neighbor = current_state[(i - 1) % size]
            right_neighbor = current_state[(i + 1) % size]

            # Update rule: If the left neighbor is the current state, increment the current state (modulo num_states)
            if left_neighbor == current_state[i]:
                next_state.append((current_state[i] + 1) % num_states)
            else:
                next_state.append(current_state[i])

        current_state = next_state
        history.append(current_state.copy())  # Store the current state

    return history


if __name__ == '__main__':
    size = 20
    num_states = 3
    iterations = 10

    history = cyclic_cellular_automaton(size, num_states, iterations)

    # Print the history (optional)
    for i, state in enumerate(history):
        print(f"Iteration {i}: {state}")
```

## How to Use:
The code can be run directly from the command line. No special instructions are needed.

## Expected Output:
The expected output is a series of lists, each representing the state of the cellular automaton at a given iteration. The numbers in the lists will be between 0 and num_states - 1. The output will vary due to the random initial state.

## Conclusion:
The Cyclic Cellular Automaton algorithm provides a simple way to simulate a dynamic system with local interactions.
