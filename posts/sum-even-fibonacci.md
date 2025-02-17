---
title: Sum Even Fibonacci
subtitle: Calculates the sum of even Fibonacci numbers up to a given limit.
tags: [fibonacci, even numbers, sum, algorithm]
verified: true
---

## Description
This algorithm calculates the sum of even Fibonacci numbers that do not exceed a specified limit.

## Algorithm Explanation
1.  The algorithm initializes two variables, `a` and `b`, to the first two Fibonacci numbers (1 and 2).
2.  It also initializes a variable `total` to 0, which will store the sum of even Fibonacci numbers.
3.  The algorithm iterates as long as the current Fibonacci number `a` is less than or equal to the given limit.
4.  In each iteration, it checks if `a` is even. If it is, it adds `a` to the `total`.
5.  The algorithm then updates `a` and `b` to the next two Fibonacci numbers.
6.  Finally, it returns the `total`.

## The Full Code
```python
def sum_even_fibonacci(limit):
    """
    Calculate the sum of even Fibonacci numbers up to a given limit.
    """
    a, b = 1, 2
    total = 0
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total

if __name__ == "__main__":
    limit = 4000000
    result = sum_even_fibonacci(limit)
    print(f"The sum of even Fibonacci numbers up to {limit} is: {result}")
```

## Expected Output
```
The sum of even Fibonacci numbers up to 4000000 is: 4613732
```

## Conclusion
The Sum Even Fibonacci algorithm efficiently calculates the sum of even Fibonacci numbers up to a given limit.
