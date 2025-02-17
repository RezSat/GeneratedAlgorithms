# Title: Nth Palindrome
# Description: This algorithm finds the nth palindrome number.

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
    while count < n:
        num += 1
        if is_palindrome(num):
            count += 1
    return num

# How to Use:
# Call the function nth_palindrome(n) with an integer argument.

# Expected Output:
# nth_palindrome(1) == 1
# nth_palindrome(2) == 2
# nth_palindrome(10) == 11

# Conclusion:
# The algorithm successfully finds the nth palindrome number.

if __name__ == '__main__':
    print(nth_palindrome(1))
    print(nth_palindrome(2))
    print(nth_palindrome(10))
