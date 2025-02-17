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
