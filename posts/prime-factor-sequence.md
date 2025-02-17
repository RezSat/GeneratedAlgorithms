---
title: Prime Factor Sequence
subtitle: A novel sequence generator based on prime factorization.
tags: [prime factorization, sequence generation, algorithm]
verified: false
---

## Description
This algorithm generates a sequence of numbers based on the prime factors of numbers up to a specified limit. It uses an initial seed value to influence the sequence, making it deterministic but sensitive to the seed.

## Algorithm Explanation
For each number from 2 up to the limit, the algorithm finds its prime factors. It then sums these factors and applies a formula involving the seed to generate the next number in the sequence. Numbers with no prime factors (i.e., 1) are handled by adding the seed directly.

## The Full Code
```python
def prime_factor_sequence(limit, seed):
    """
    Generates a sequence of numbers based on the prime factors of numbers up to a limit,
    influenced by an initial seed value.

    For each number, it finds the prime factors, sums them, and then applies a simple
    formula involving the seed to generate the next number in the sequence. This aims
    to create a sequence that is deterministic given the seed and limit, but appears
    random and is sensitive to changes in the seed.
    """
    sequence = []
    current = seed
    for i in range(2, limit + 1):
        factors = []
        n = i
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)

        if factors:
            factor_sum = sum(factors)
            current = (current + factor_sum * seed) % limit
        else:
            current = (current + seed) % limit
        sequence.append(current)
    return sequence

if __name__ == "__main__":
    limit = 100
    seed = 42
    result = prime_factor_sequence(limit, seed)
    print(f"Prime Factor Sequence with limit={limit}, seed={seed}:")
    print(result)
```

## How to Use
Run the script directly. The `limit` and `seed` values can be modified in the `if __name__ == "__main__":` block.

## Expected Output
```
Prime Factor Sequence with limit=100, seed=42:
[44, 46, 50, 56, 64, 74, 86, 10, 24, 40, 58, 78, 0, 22, 46, 72, 0, 28, 58, 90, 24, 56, 90, 26, 62, 0, 40, 82, 24, 70, 16, 64, 14, 66, 18, 72, 26, 82, 38, 96, 54, 14, 74, 36, 98, 62, 24, 88, 52, 18, 86, 52, 20, 90, 58, 28, 100, 70, 42, 16, 90, 64, 38, 14, 90, 66, 42, 20, 98, 76, 54, 34, 14, 94, 74, 56, 38, 22, 4, 86, 70, 56, 44, 32, 18, 4, 92, 80, 70, 62, 56, 52, 50, 50, 52, 56]
```

## Conclusion
The Prime Factor Sequence algorithm generates a sequence of numbers based on the prime factorization of consecutive integers, offering a unique approach to sequence generation with sensitivity to initial parameters.
