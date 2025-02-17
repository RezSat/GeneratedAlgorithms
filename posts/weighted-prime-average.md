---
title: Weighted Prime Average
subtitle: Calculates the weighted average of prime numbers within a given range.
tags: [prime numbers, average, weighted average, algorithm]
verified: false
---

## Description
This algorithm calculates the weighted average of prime numbers within a specified range. The weight of each prime number is the prime number itself.

## Algorithm Explanation
1.  The algorithm first identifies all prime numbers within the given range.
2.  If no prime numbers are found, it returns 0.
3.  It calculates the total weight by summing all the prime numbers.
4.  It calculates the weighted sum by summing the square of each prime number.
5.  Finally, it returns the weighted average by dividing the weighted sum by the total weight.

## The Full Code
```python
def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def weighted_prime_average(start, end):
    """
    Calculate the weighted average of prime numbers within a given range.
    The weight is the prime number itself.
    """
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    if not primes:
        return 0
    total_weight = sum(primes)
    weighted_sum = sum(prime * prime for prime in primes)
    return weighted_sum / total_weight

if __name__ == "__main__":
    start_range = 1
    end_range = 20
    result = weighted_prime_average(start_range, end_range)
    print(f"The weighted average of prime numbers between {start_range} and {end_range} is: {result}")
```

## Expected Output
```
The weighted average of prime numbers between 1 and 20 is: 13.337662337662337
```

## Conclusion
The Weighted Prime Average algorithm efficiently calculates the weighted average of prime numbers within a given range.
