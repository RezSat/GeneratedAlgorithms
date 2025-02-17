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