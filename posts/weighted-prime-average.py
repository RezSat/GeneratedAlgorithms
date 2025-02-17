def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def weighted_prime_average(numbers):
    """
    Calculate the weighted average of a list of numbers,
    where the weights are determined by the primality of their indices.
    """
    if not numbers:
        return 0

    total_weight = 0
    weighted_sum = 0

    for i, num in enumerate(numbers):
        if is_prime(i):
            weight = 2  # Prime indices have a weight of 2
        else:
            weight = 1  # Non-prime indices have a weight of 1

        total_weight += weight
        weighted_sum += num * weight

    return weighted_sum / total_weight

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    average = weighted_prime_average(data)
    print(f"The weighted prime average is: {average}")
