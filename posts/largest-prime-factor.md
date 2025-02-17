---
title: Largest Prime Factor
subtitle: Finds the largest prime factor of a given number.
tags: [prime factor, prime, factor, algorithm]
verified: false
---

## Description
This algorithm finds the largest prime factor of a given number.

## Algorithm Explanation
1.  The algorithm starts with the smallest prime number, 2.
2.  It repeatedly divides the number by the smallest prime factor until the number is no longer divisible by it.
3.  Then, it increments the prime factor and repeats the process.
4.  The largest prime factor is the last remaining value of the number.

## The Full Code
```python
def largest_prime_factor(n):
    """
    Find the largest prime factor of a number.
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

if __name__ == "__main__":
    number = 600851475143
    result = largest_prime_factor(number)
    print(f"The largest prime factor of {number} is: {result}")
```

## Expected Output
```
The largest prime factor of 600851475143 is: 6857
```

## Conclusion
The Largest Prime Factor algorithm efficiently calculates the largest prime factor of a given number.
