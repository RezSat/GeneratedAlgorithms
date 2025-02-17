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

def weighted_prime_average(limit):
    """
    Calculate the weighted average of prime numbers less than a given number.
    """
    primes = [number for number in range(2, limit) if is_prime(number)]
    if not primes:
        return 0
    total_weight = sum(primes)
    weighted_sum = sum(prime * prime for prime in primes)
    return weighted_sum / total_weight

if __name__ == "__main__":
    limit = 20
    result = weighted_prime_average(limit)
    print(f"The weighted average of prime numbers less than {limit} is: {result}")
