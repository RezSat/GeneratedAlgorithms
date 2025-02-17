---
title: Chromatic Brainwaves
subtitle: Generates a sequence of "brainwaves" represented by a list of colors with a bias towards changes.
tags: [random, colors, sequence, brainwaves, algorithm]
verified: true
---

## Title: Chromatic Brainwaves

## Description:
This algorithm generates a sequence of "brainwaves" represented by a list of colors. The colors are chosen randomly, but with a bias towards changes.

## Algorithm Explanation:
The algorithm takes the length of the sequence and the number of possible colors as input. It starts by choosing a random color for the first brainwave. For each subsequent brainwave, it has a higher probability of choosing a different color than the previous one.

## The Full Code:
```python
import random

def chromatic_brainwaves(length, num_colors):
    """
    Generates a sequence of "brainwaves" represented by a list of colors.
    The colors are chosen randomly, but with a bias towards changes.

    Args:
        length: The length of the brainwave sequence.
        num_colors: The number of possible colors.

    Returns:
        A list of integers representing the brainwave sequence.
    """
    if num_colors <= 0 or length <= 0:
        return []

    brainwaves = []
    previous_color = random.randint(0, num_colors - 1)
    brainwaves.append(previous_color)

    for _ in range(1, length):
        # Bias towards changing colors
        if random.random() < 0.8:  # 80% chance of changing
            available_colors = [c for c in range(num_colors) if c != previous_color]
            if available_colors:
                next_color = random.choice(available_colors)
            else:
                next_color = previous_color #if only one color, stay the same
        else:
            next_color = previous_color  # 20% chance of staying the same

        brainwaves.append(next_color)
        previous_color = next_color

    return brainwaves


if __name__ == '__main__':
    length = 100
    num_colors = 5
    brainwaves = chromatic_brainwaves(length, num_colors)
    print(f"Generated brainwaves: {brainwaves}")
```

## How to Use:
The code can be run directly from the command line. No special instructions are needed.

## Expected Output:
The expected output is a list of integers representing the brainwave sequence. The numbers will be between 0 and num_colors - 1.  You should see that the numbers tend to change frequently.

## Conclusion:
The Chromatic Brainwaves algorithm provides a way to generate a sequence of colors with a bias towards changes. This can be useful in situations where you want to simulate a dynamic system.
