---
title: Sum of Digits
subtitle: Calculates the sum of the digits of a number.
tags: [sum, digits, algorithm]
verified: true
---

## Description
This algorithm calculates the sum of the digits of a given number.

## Algorithm Explanation
1.  Initialize a variable `sum` to 0.
2.  While the number is not 0:
    *   Extract the last digit of the number using the modulo operator (`%`).
    *   Add the last digit to the `sum`.
    *   Remove the last digit from the number using integer division (`//`).
3.  Return the `sum`.

## The Full Code
```python
def sum_digits(n):
    """
    Calculate the sum of digits of a number.
    """
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n // 10
    return sum

if __name__ == "__main__":
    number = 12345
    result = sum_digits(number)
    print(f"The sum of digits of {number} is: {result}")
```

## Expected Output
```
The sum of digits of 12345 is: 15
```

## Conclusion
The Sum of Digits algorithm efficiently calculates the sum of the digits of a number.
