---
title: Prime Factorization
subtitle: Finds the prime factors of a given number.
tags: [math, algorithm, prime]
verified: true
---

## Description
This algorithm finds the prime factors of a given number.

## Algorithm Explanation
1. Take an integer as input.
2. Create an empty list to store the prime factors.
3. While the number is divisible by 2, add 2 to the list of prime factors and divide the number by 2.
4. Iterate from 3 to the square root of the number, incrementing by 2.
    * While the number is divisible by the current iterator, add the iterator to the list of prime factors and divide the number by the iterator.
5. If the number is greater than 2, add the number to the list of prime factors.
6. Return the list of prime factors.

## The Full Code
```python
import math

def prime_factorization(n):
    """
    Finds the prime factors of a given number.
    """
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n = n // i
    if n > 2:
        prime_factors.append(n)
    return prime_factors

if __name__ == '__main__':
    print(prime_factorization(12))
    print(prime_factorization(13))
    print(prime_factorization(315))
```

## How to Use
Call the function `prime_factorization(n)` with an integer argument.

## Expected Output
```
[2, 2, 3]
[13]
[3, 3, 5, 7]
```

## Conclusion
The algorithm successfully finds the prime factors of a given number.
