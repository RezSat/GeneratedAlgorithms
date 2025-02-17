---
title: Recursive String Scrambler
subtitle: Scrambles a string using recursion.
tags: [string, recursion, scramble]
verified: true
---

## Small Description

This algorithm recursively scrambles a string by splitting it into two parts, scrambling each part, and then concatenating them back together.

## Algorithm Explanation

The algorithm works as follows:

1.  If the string length is less than or equal to 1, return the string (base case).
2.  Choose a random split point in the string.
3.  Split the string into two parts at the split point.
4.  Recursively call the function on each part.
5.  Randomly decide whether to swap the order of the two scrambled parts before concatenating them.

## The Full Code

```python
import random

def recursive_string_scrambler(s):
    if len(s) <= 1:
        return s

    split_point = random.randint(1, len(s) - 1)
    left = s[:split_point]
    right = s[split_point:]

    scrambled_left = recursive_string_scrambler(left)
    scrambled_right = recursive_string_scrambler(right)

    if random.random() < 0.5:
        return scrambled_left + scrambled_right
    else:
        return scrambled_right + scrambled_left

# Example usage:
# string = "abcdefgh"
# scrambled_string = recursive_string_scrambler(string)
# print(f"Original string: {string}")
# print(f"Scrambled string: {scrambled_string}")
```

## How to Use

To use the algorithm, call the `recursive_string_scrambler` function with the string you want to scramble. The function returns the scrambled string.

## Expected Output

The output will be a scrambled version of the input string. The degree of scrambling will depend on the length of the string and the random choices made during the recursive calls.

## Conclusion

This "Recursive String Scrambler" algorithm provides a fun and simple way to scramble strings using recursion.
