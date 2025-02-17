---
title: Prime Digit Summation
subtitle: Calculates the sum of the digits of a number, only adding the digits that are prime numbers.
tags: [math, algorithm, number]
verified: true
---

## Description
This algorithm calculates the sum of the digits of a number, only adding the digits that are prime numbers.

## Algorithm Explanation
The algorithm takes an integer as input. It iterates through the digits of the number. For each digit, it checks if the digit is a prime number (2, 3, 5, or 7). If the digit is prime, it adds the digit to a running sum. Finally, it returns the sum of the prime digits.

## The Full Code
```python
def is_prime_digit(digit):
    """
    Checks if a digit is a prime number.
    """
    return digit in [2, 3, 5, 7]

def prime_digit_summation(n):
    """
    Calculates the sum of the digits of a number, only adding the digits that are prime numbers.
    """
    sum_of_primes = 0
    for digit in str(n):
        digit = int(digit)
        if is_prime_digit(digit):
            sum_of_primes += digit
    return sum_of_primes

if __name__ == '__main__':
    print(prime_digit_summation(1234567))
    print(prime_digit_summation(222))
    print(prime_digit_summation(111))
```

## How to Use
Call the function `prime_digit_summation(n)` with an integer argument.

## Expected Output
```
17
6
0
```

## Conclusion
The algorithm successfully calculates the sum of the prime digits of a number.
