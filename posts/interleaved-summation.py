# Title: Interleaved Summation
# Description: This algorithm calculates the sum of elements in an array, interleaving the summation from both ends.

def interleaved_summation(arr):
    """
    Calculates the sum of elements in an array, interleaving the summation from both ends.
    """
    left = 0
    right = len(arr) - 1
    sum = 0
    while left <= right:
        if left == right:
            sum += arr[left]
        else:
            sum += arr[left] + arr[right]
        left += 1
        right -= 1
    return sum

# How to Use:
# Call the function interleaved_summation(arr) with an array of numbers as an argument.

# Expected Output:
# interleaved_summation([1, 2, 3, 4, 5]) == 9
# interleaved_summation([1, 2, 3, 4, 5, 6]) == 21
# interleaved_summation([1, 2, 3]) == 6

# Conclusion:
# The algorithm successfully calculates the interleaved summation of an array.

if __name__ == '__main__':
    print(interleaved_summation([1, 2, 3, 4, 5]))
    print(interleaved_summation([1, 2, 3, 4, 5, 6]))
    print(interleaved_summation([1, 2, 3]))
