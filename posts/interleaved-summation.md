---
title: Interleaved Summation
subtitle: Summing digits of interleaved numbers.
tags: [math, string, algorithm]
verified: true
---

## Description
This algorithm calculates a sum by interleaving the digits of two numbers.

## Algorithm Explanation
The algorithm takes two integers as input. It converts them into strings, interleaves their digits, and then sums the resulting digits. If one number has more digits than the other, the remaining digits of the longer number are appended to the interleaved sequence.

## The Full Code
```python
def interleaved_summation(num1, num2):
    """
    Calculates a sum by interleaving the digits of two numbers.
    """
    str1 = str(num1)
    str2 = str(num2)
    len1 = len(str1)
    len2 = len(str2)
    
    interleaved = ""
    i = 0
    j = 0
    
    while i < len1 and j < len2:
        interleaved += str1[i]
        interleaved += str2[j]
        i += 1
        j += 1
        
    while i < len1:
        interleaved += str1[i]
        i += 1
        
    while j < len2:
        interleaved += str2[j]
        j += 1
        
    sum_of_digits = sum(int(digit) for digit in interleaved)
    return sum_of_digits

if __name__ == '__main__':
    print(interleaved_summation(123, 456))
    print(interleaved_summation(12, 3456))
    print(interleaved_summation(12345, 67))
```

## How to Use
Call the function `interleaved_summation(num1, num2)` with two integer arguments.

## Expected Output
```
21
21
28
```

## Conclusion
The algorithm successfully interleaves the digits of two numbers and returns the sum of the interleaved digits.
