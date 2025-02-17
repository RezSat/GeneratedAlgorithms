---
title: Weighted Prime Average
subtitle: Calculates a weighted average based on prime number indices.
tags: [weighted average, prime numbers, algorithm]
verified: false
---

## Description
This algorithm calculates the weighted average of a list of numbers. The weight of each number is determined by whether its index is a prime number. Prime indices have a weight of 2, while non-prime indices have a weight of 1.

## Algorithm Explanation
1.  The algorithm iterates through the input list of numbers.
2.  For each number, it checks if its index is a prime number using the `is_prime()` function.
3.  If the index is prime, the number is assigned a weight of 2; otherwise, it's assigned a weight of 1.
4.  The weighted sum and total weight are calculated.
5.  The weighted average is computed by dividing the weighted sum by the total weight.

## The Full Code
```python
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def weighted_prime_average(numbers):
    """
    Calculate the weighted average of a list of numbers,
    where the weights are determined by the primality of their indices.
    """
    if not numbers:
        return 0

    total_weight = 0
    weighted_sum = 0

    for i, num in enumerate(numbers):
        if is_prime(i):
            weight = 2  # Prime indices have a weight of 2
        else:
            weight = 1  # Non-prime indices have a weight of 1

        total_weight += weight
        weighted_sum += num * weight

    return weighted_sum / total_weight

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    average = weighted_prime_average(data)
    print(f"The weighted prime average is: {average}")
```

## Expected Output
```
The weighted prime average is: 5.428571428571429
```

## Conclusion
The Weighted Prime Average algorithm calculates the average of a list of numbers, giving higher importance to numbers at prime indices.
