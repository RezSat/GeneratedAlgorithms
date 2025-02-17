# Title: Prime Factor Sequence
# Description: Generates a sequence of prime factors for a given number.
# Algorithm Explanation: The algorithm finds the prime factors of a given number by iteratively dividing the number by the smallest prime number until the number becomes 1.

def prime_factor_sequence(n):
    """
    Generates a sequence of prime factors for a given number.

    Args:
        n (int): The number for which to generate the prime factors.

    Returns:
        list: A list containing the prime factors of the number.
    """
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors

# How to Use: Run the script with the desired number as an argument.
if __name__ == "__main__":
    number = 12  # You can change this value
    factors = prime_factor_sequence(number)
    print("Prime Factors:", factors)

# Expected Output:
# Prime Factors: [2, 2, 3]

# Conclusion: This script generates the sequence of prime factors for a given number.
