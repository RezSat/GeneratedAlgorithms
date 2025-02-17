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
