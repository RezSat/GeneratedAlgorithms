---
title: Weighted Prime Average
subtitle: Calculates the weighted average of prime numbers less than a given number.
tags: [prime, average, algorithm]
verified: true
---

## Description
This algorithm calculates the weighted average of prime numbers less than a given number. The weight of each prime number is the prime number itself.

## Algorithm Explanation
1.  Generate a list of prime numbers less than the given number.
2.  If the list of prime numbers is empty, return 0.
3.  Calculate the total weight, which is the sum of all prime numbers.
4.  Calculate the weighted sum, which is the sum of each prime number multiplied by its weight (which is the prime number itself).
5.  Calculate the weighted average by dividing the weighted sum by the total weight.

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

def weighted_prime_average(limit):
    """
    Calculate the weighted average of prime numbers less than a given number.
    """
    primes = [number for number in range(2, limit) if is_prime(number)]
    if not primes:
        return 0
    total_weight = sum(primes)
    weighted_sum = sum(prime * prime for prime in primes)
    return weighted_sum / total_weight

if __name__ == "__main__":
    limit = 20
    result = weighted_prime_average(limit)
    print(f"The weighted average of prime numbers less than {limit} is: {result}")
```

## Expected Output
```
The weighted average of prime numbers less than 20 is: 13.337662337662337
```

## Conclusion
The Weighted Prime Average algorithm efficiently calculates the weighted average of prime numbers less than a given number.
