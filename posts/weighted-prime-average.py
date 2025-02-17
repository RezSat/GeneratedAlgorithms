def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def weighted_prime_average(start, end):
    """
    Calculate the weighted average of prime numbers within a given range.
    The weight is the prime number itself.
    """
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    if not primes:
        return 0
    total_weight = sum(primes)
    weighted_sum = sum(prime * prime for prime in primes)
    return weighted_sum / total_weight

if __name__ == "__main__":
    start_range = 1
    end_range = 20
    result = weighted_prime_average(start_range, end_range)
    print(f"The weighted average of prime numbers between {start_range} and {end_range} is: {result}")
