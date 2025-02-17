def sum_even_fibonacci(limit):
    """
    Calculate the sum of even Fibonacci numbers up to a given limit.
    """
    a, b = 1, 1
    total = 0
    while b <= limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total

if __name__ == "__main__":
    limit = 4000000
    result = sum_even_fibonacci(limit)
    print(f"The sum of even Fibonacci numbers up to {limit} is: {result}")
