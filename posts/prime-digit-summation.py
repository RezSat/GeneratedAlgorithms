# Title: Prime Digit Summation
# Description: This algorithm calculates the sum of prime digits in a given number.

def prime_digit_summation(number):
    """
    Calculates the sum of prime digits in a given number.
    """
    prime_digits = [2, 3, 5, 7]
    sum_of_primes = 0
    
    for digit in str(number):
        digit = int(digit)
        if digit in prime_digits:
            sum_of_primes += digit
            
    return sum_of_primes

# How to Use:
# Call the function prime_digit_summation(number) with an integer argument.

# Expected Output:
# prime_digit_summation(1234567) == 2 + 3 + 5 + 7 == 17
# prime_digit_summation(222) == 2 + 2 + 2 == 6
# prime_digit_summation(1468) == 0

# Conclusion:
# The algorithm successfully calculates the sum of prime digits in a number.

if __name__ == '__main__':
    print(prime_digit_summation(1234567))
    print(prime_digit_summation(222))
    print(prime_digit_summation(1468))
