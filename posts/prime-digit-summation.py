# Title: Prime Digit Summation
# Description: This algorithm calculates the sum of the digits of a number, only adding the digits that are prime numbers.

def is_prime_digit(digit):
    """
    Checks if a digit is a prime number.
    """
    return digit in [2, 3, 5, 7]

def prime_digit_summation(n):
    """
    Calculates the sum of the digits of a number, only adding the digits that are prime numbers.
    """
    sum_of_primes = 0
    for digit in str(n):
        digit = int(digit)
        if is_prime_digit(digit):
            sum_of_primes += digit
    return sum_of_primes

# How to Use:
# Call the function prime_digit_summation(n) with an integer argument.

# Expected Output:
# prime_digit_summation(1234567) == 17
# prime_digit_summation(222) == 6
# prime_digit_summation(111) == 0

# Conclusion:
# The algorithm successfully calculates the sum of the prime digits of a number.

if __name__ == '__main__':
    print(prime_digit_summation(1234567))
    print(prime_digit_summation(222))
    print(prime_digit_summation(111))
