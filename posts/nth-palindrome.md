---
title: Nth Palindrome Number
subtitle: Finds the nth palindrome number.
tags: [palindrome, algorithm]
verified: false
---

## Description
This algorithm finds the nth palindrome number. A palindrome number is a number that remains the same when its digits are reversed.

## Algorithm Explanation
1.  Start with the number 0.
2.  Increment the number until a palindrome is found.
3.  Repeat step 2 until the nth palindrome number is found.

## The Full Code
```python
def is_palindrome(n):
    """
    Check if a number is a palindrome.
    """
    return str(n) == str(n)[::-1]

def nth_palindrome(n):
    """
    Find the nth palindrome number.
    """
    count = 0
    num = 0
    while count &lt; n:
        num += 1
        if is_palindrome(num):
            count += 1
    return num

if __name__ == "__main__":
    n = 10
    result = nth_palindrome(n)
    print(f"The {n}th palindrome number is: {result}")
```

## Expected Output
```
The 10th palindrome number is: 11
```

## Conclusion
The Nth Palindrome Number algorithm efficiently finds the nth palindrome number.
