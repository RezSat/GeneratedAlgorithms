---
title: Reverse and Add
subtitle: Reverses a number and adds it to the original.
tags: [math, algorithm]
verified: false
---

## Description
This algorithm takes an integer as input, reverses it, adds the reversed number to the original number, and returns the result.

## Algorithm Explanation
The algorithm takes an integer as input. It converts the number into a string, reverses the string, converts the reversed string back to an integer, adds the reversed integer to the original integer, and returns the sum.

## The Full Code
```python
def reverse_and_add(number):
    """
    Reverses a number, adds it to the original number, and returns the result.
    """
    reversed_number = int(str(number)[::-1])
    return number + reversed_number

if __name__ == '__main__':
    print(reverse_and_add(123))
    print(reverse_and_add(10))
    print(reverse_and_add(5))
```

## How to Use
Call the function `reverse_and_add(number)` with an integer argument.

## Expected Output
```
444
11
10
```

## Conclusion
The algorithm successfully reverses a number, adds it to the original number, and returns the result.
