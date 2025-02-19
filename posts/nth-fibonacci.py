def nth_fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    n = 10
    result = nth_fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")
