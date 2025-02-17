# Title: Prime Factorization
# Description: This algorithm finds the prime factors of a given number.

import math

def prime_factorization(n):
    """
    Finds the prime factors of a given number.
    """
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n = n // i
    if n > 2:
        prime_factors.append(n)
    return prime_factors

# How to Use:
# Call the function prime_factorization(n) with an integer argument.

# Expected Output:
# prime_factorization(12) == [2, 2, 3]
# prime_factorization(13) == [13]
# prime_factorization(315) == [3, 3, 5, 7]

# Conclusion:
# The algorithm successfully finds the prime factors of a given number.

if __name__ == '__main__':
    print(prime_factorization(12))
    print(prime_factorization(13))
    print(prime_factorization(315))
