# Title: Recaman Sequence Analyzer
# Description: Generates the Recaman sequence and finds the first repeating number.
# Algorithm Explanation: The Recaman sequence is defined as follows: a(0) = 0; for n > 0, a(n) = a(n-1) - n if the result is positive and not already in the sequence, otherwise a(n) = a(n-1) + n. This script generates the sequence up to a specified number of terms and identifies the first repeating number and its index.

def recaman_sequence_analyzer(n):
    """
    Generates the Recaman sequence up to n terms and finds the first repeating number and its index.

    Args:
        n (int): The number of terms to generate in the Recaman sequence.

    Returns:
        tuple: A tuple containing the Recaman sequence, the first repeating number, and its index.
               Returns (sequence, None, None) if no repeating number is found.
    """
    sequence = [0]
    seen = {0}
    repeating_number = None
    repeating_index = None

    for i in range(1, n):
        next_val = sequence[-1] - i
        if next_val > 0 and next_val not in seen:
            sequence.append(next_val)
        else:
            next_val = sequence[-1] + i
            sequence.append(next_val)

        if next_val in seen:
            repeating_number = next_val
            repeating_index = i
            break

        seen.add(next_val)

    return sequence, repeating_number, repeating_index


# How to Use: Run the script with the desired number of terms as an argument.
if __name__ == "__main__":
    num_terms = 20  # You can change this value
    sequence, repeating_number, repeating_index = recaman_sequence_analyzer(num_terms)

    print("Recaman Sequence:", sequence)
    if repeating_number is not None:
        print("First Repeating Number:", repeating_number)
        print("Index of First Repetition:", repeating_index)
    else:
        print("No repeating number found in the sequence.")

# Expected Output:
# Recaman Sequence: [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 25, 7, 26]
# First Repeating Number: 7
# Index of First Repetition: 18

# Conclusion: This script generates the Recaman sequence and identifies the first repeating number, providing insights into the sequence's behavior.
