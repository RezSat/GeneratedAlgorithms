---
title: Nth Palindrome
subtitle: Finds the nth palindrome number.
tags: [math, algorithm]
verified: true
---

## Description
This algorithm finds the nth palindrome number.

## Algorithm Explanation
The algorithm takes an integer n as input. It generates palindrome numbers starting from 1 and continues until it finds the nth palindrome number.

## The Full Code
```python
def is_palindrome(n):
    """
    Checks if a number is a palindrome.
    """
    return str(n) == str(n)[::-1]

def nth_palindrome(n):
    """
    Finds the nth palindrome number.
    """
    count = 0
    num = 0
    while count &lt; n:
        num += 1
        if is_palindrome(num):
            count += 1
    return num

if __name__ == '__main__':
    print(nth_palindrome(1))
    print(nth_palindrome(2))
    print(nth_palindrome(10))
```

## How to Use
Call the function `nth_palindrome(n)` with an integer argument.

## Expected Output
```
1
2
11
```

## Conclusion
The algorithm successfully finds the nth palindrome number.
