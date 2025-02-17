---
title: Reverse and Add
subtitle: Takes an integer, reverses it, and adds the reversed number to the original until a palindrome is found.
tags: [math, algorithm, palindrome]
verified: true
---

## Description
This algorithm takes an integer as input, reverses it, and adds the reversed number to the original number. If the result is not a palindrome, repeat the process until it becomes a palindrome or a maximum number of iterations is reached.

## Algorithm Explanation
1. Take an integer as input.
2. Reverse the digits of the number.
3. Add the reversed number to the original number.
4. Check if the result is a palindrome.
    * If it is a palindrome, return the result.
    * If it is not a palindrome, repeat steps 2-4 until a palindrome is found or a maximum number of iterations is reached.
5. If a palindrome is not found within the maximum number of iterations, return -1.

## The Full Code
```python
def reverse_and_add(n, max_iterations=1000):
    """
    Takes an integer as input, reverses it, and adds the reversed number to the original number.
    If the result is not a palindrome, repeat the process until it becomes a palindrome
    or a maximum number of iterations is reached.
    """
    if str(n) == str(n)[::-1]:
        return n
    for i in range(max_iterations):
        reversed_n = int(str(n)[::-1])
        sum_n = n + reversed_n
        if str(sum_n) == str(sum_n)[::-1]:
            return sum_n
        n = sum_n
    return -1

if __name__ == '__main__':
    print(reverse_and_add(121))
    print(reverse_and_add(123))
    print(reverse_and_add(195))
```

## How to Use
Call the function `reverse_and_add(n)` with an integer argument.

## Expected Output
```
121
444
9339
```

## Conclusion
The algorithm successfully finds a palindrome by reversing and adding a number to itself.
