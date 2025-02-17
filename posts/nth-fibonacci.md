---
title: Nth Fibonacci Number
subtitle: Calculates the nth Fibonacci number.
tags: [fibonacci, sequence, algorithm]
verified: true
---

## Description
This algorithm calculates the nth Fibonacci number in the Fibonacci sequence.

## Algorithm Explanation
1.  If n is less than or equal to 0, return 0.
2.  If n is 1, return 1.
3.  Otherwise, use an iterative approach to calculate the nth Fibonacci number.

## The Full Code
```python
def nth_fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    n = 10
    result = nth_fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")
```

## Expected Output
```
The 10th Fibonacci number is: 55
```

## Conclusion
The Nth Fibonacci Number algorithm efficiently calculates the nth Fibonacci number.
