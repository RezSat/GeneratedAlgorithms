def largest_prime_factor(n):
    """
    Find the largest prime factor of a number.
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

if __name__ == "__main__":
    number = 600851475143
    result = largest_prime_factor(number)
    print(f"The largest prime factor of {number} is: {result}")
