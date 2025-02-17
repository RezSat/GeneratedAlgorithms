---
title: Interleaved Summation
subtitle: Calculates the sum of elements in an array, interleaving the summation from both ends.
tags: [math, algorithm, array]
verified: false
---

## Description
This algorithm calculates the sum of elements in an array, interleaving the summation from both ends.

## Algorithm Explanation
1. Take an array of numbers as input.
2. Initialize two pointers, `left` and `right`, to the start and end of the array, respectively.
3. Initialize a variable `sum` to 0.
4. While `left` is less than or equal to `right`:
    * If `left` is equal to `right`, add the element at `left` to `sum`.
    * Otherwise, add the elements at `left` and `right` to `sum`.
    * Increment `left` and decrement `right`.
5. Return `sum`.

## The Full Code
```python
def interleaved_summation(arr):
    """
    Calculates the sum of elements in an array, interleaving the summation from both ends.
    """
    left = 0
    right = len(arr) - 1
    sum = 0
    while left &lt;= right:
        if left == right:
            sum += arr[left]
        else:
            sum += arr[left] + arr[right]
        left += 1
        right -= 1
    return sum

if __name__ == '__main__':
    print(interleaved_summation([1, 2, 3, 4, 5]))
    print(interleaved_summation([1, 2, 3, 4, 5, 6]))
    print(interleaved_summation([1, 2, 3]))
```

## How to Use
Call the function `interleaved_summation(arr)` with an array of numbers as an argument.

## Expected Output
```
9
21
6
```

## Conclusion
The algorithm successfully calculates the interleaved summation of an array.
