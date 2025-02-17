---
title: Sum Even Fibonacci
subtitle: Calculates the sum of even Fibonacci numbers up to a given limit.
tags: [Fibonacci, even numbers, sum, algorithm]
verified: true
---

## Description
This algorithm calculates the sum of even-valued Fibonacci numbers whose values do not exceed a specified limit.

## Algorithm Explanation
1.  The algorithm initializes two variables, `a` and `b`, to 1, representing the first two Fibonacci numbers.
2.  It also initializes a variable `total` to 0, which will store the sum of even Fibonacci numbers.
3.  The algorithm then enters a `while` loop that continues as long as the current Fibonacci number `b` is less than or equal to the given limit.
4.  Inside the loop, it checks if `b` is even. If it is, `b` is added to the `total`.
5.  The algorithm then updates `a` and `b` to calculate the next Fibonacci number.
6.  Finally, the algorithm returns the `total`, which is the sum of even Fibonacci numbers up to the limit.

## The Full Code
```python
def sum_even_fibonacci(limit):
    """
    Calculate the sum of even Fibonacci numbers up to a given limit.
    """
    a, b = 1, 1
    total = 0
    while b <= limit:
        if b % 2 == 0:
            total += b
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
The Sum Even Fibonacci algorithm efficiently calculates the sum of even Fibonacci numbers within a specified range.
