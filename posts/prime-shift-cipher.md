---
title: Prime Shift Cipher
subtitle: A unique sequence generator based on prime factorization and a shifting cipher.
tags: [prime numbers, cipher, sequence generation, algorithm]
verified: true
---

## Title: Prime Shift Cipher

## Description:
This algorithm generates a unique sequence by combining prime factorization with a shifting cipher. It takes an integer as input, factors it into prime numbers, and then uses these primes to shift characters in a predefined alphabet.

## Algorithm Explanation:
1.  **Prime Factorization:** The input integer is factorized into its prime factors.
2.  **Alphabet Definition:** A standard alphabet (a-z) is defined.
3.  **Shifting:** Each prime factor is used to shift a character in the alphabet. The first prime shifts the first character, the second prime shifts the second character, and so on. If the prime factor is larger than the alphabet length, the shift is performed modulo the alphabet length.
4.  **Sequence Generation:** The shifted characters are concatenated to form the final sequence.

## The Full Code:
```python
def prime_factorization(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def prime_shift_cipher(input_integer):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    factors = prime_factorization(input_integer)
    sequence = ""
    for i, factor in enumerate(factors):
        shift = factor % len(alphabet)
        char_index = i % len(alphabet)
        shifted_index = (char_index + shift) % len(alphabet)
        sequence += alphabet[shifted_index]
    return sequence

if __name__ == '__main__':
    input_number = 12345
    result = prime_shift_cipher(input_number)
    print(f"The sequence for {input_number} is: {result}")

```

## How to Use:
Simply run the python code. The main block will execute the algorithm with a default input of 12345. You can modify the input_number variable to test with different integers.

## Expected Output:
For the input 12345, the expected output is: `The sequence for 12345 is: dgt`

## Conclusion:
The Prime Shift Cipher algorithm provides a unique way to generate sequences based on prime factorization. The generated sequences are sensitive to the input integer, making it suitable for various applications such as data encoding or unique identifier generation.
