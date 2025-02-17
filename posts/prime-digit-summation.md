---
title: Prime Digit Summation
subtitle: Summing the prime digits of a number.
tags: [math, prime, algorithm]
verified: true
---

## Description
This algorithm calculates the sum of prime digits in a given number.

## Algorithm Explanation
The algorithm takes an integer as input. It converts the number into a string, iterates through each digit, checks if the digit is a prime number (2, 3, 5, or 7), and if it is, adds it to the sum.

## The Full Code
```python
def prime_digit_summation(number):
    """
    Calculates the sum of prime digits in a given number.
    """
    prime_digits = [2, 3, 5, 7]
    sum_of_primes = 0
    
    for digit in str(number):
        digit = int(digit)
        if digit in prime_digits:
            sum_of_primes += digit
            
    return sum_of_primes

if __name__ == '__main__':
    print(prime_digit_summation(1234567))
    print(prime_digit_summation(222))
    print(prime_digit_summation(1468))
```

## How to Use
Call the function `prime_digit_summation(number)` with an integer argument.

## Expected Output
```
17
6
0
```

## Conclusion
The algorithm successfully calculates the sum of prime digits in a number.
