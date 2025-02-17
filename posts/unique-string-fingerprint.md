---
title: Unique String Fingerprint
subtitle: Generate a unique fingerprint for a given string.
tags: [string, fingerprint, hashing, unique]
verified: false
---

## Title: Unique String Fingerprint

## Description
This algorithm generates a unique fingerprint for a given string using prime numbers and modulo operation.

## Algorithm Explanation
The algorithm assigns a prime number to each character of the string based on its index. It then multiplies the ASCII value of the character with the corresponding prime number and a running fingerprint value. Finally, it applies a modulo operation to keep the fingerprint within a manageable range.

## The Full Code
```python
def generate_fingerprint(input_string):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    fingerprint = 1
    for i, char in enumerate(input_string):
        fingerprint = (fingerprint * prime_numbers[i % len(prime_numbers)] * ord(char)) % 100000
    return fingerprint

if __name__ == "__main__":
    test_string = "example string"
    fingerprint = generate_fingerprint(test_string)
    print(f"The fingerprint for '{test_string}' is: {fingerprint}")
```

## How to Use
No special instructions are needed. Just run the python code.

## Expected Output
```
The fingerprint for 'example string' is: [some number]
```

## Conclusion
This algorithm provides a simple way to generate a fingerprint for a string. The uniqueness depends on the length of the string and the distribution of characters.

