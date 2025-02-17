# Title: Interleaved Summation
# Description: This algorithm calculates a sum by interleaving the digits of two numbers.

def interleaved_summation(num1, num2):
    """
    Calculates a sum by interleaving the digits of two numbers.
    """
    str1 = str(num1)
    str2 = str(num2)
    len1 = len(str1)
    len2 = len(str2)
    
    interleaved = ""
    i = 0
    j = 0
    
    while i < len1 and j < len2:
        interleaved += str1[i]
        interleaved += str2[j]
        i += 1
        j += 1
        
    while i < len1:
        interleaved += str1[i]
        i += 1
        
    while j < len2:
        interleaved += str2[j]
        j += 1
        
    sum_of_digits = sum(int(digit) for digit in interleaved)
    return sum_of_digits

# How to Use:
# Call the function interleaved_summation(num1, num2) with two integer arguments.

# Expected Output:
# interleaved_summation(123, 456) == 1+4+2+5+3+6 == 21
# interleaved_summation(12, 3456) == 1+3+2+4+5+6 == 21
# interleaved_summation(12345, 67) == 1+6+2+7+3+4+5 == 28

# Conclusion:
# The algorithm successfully interleaves the digits of two numbers and returns the sum of the interleaved digits.

if __name__ == '__main__':
    print(interleaved_summation(123, 456))
    print(interleaved_summation(12, 3456))
    print(interleaved_summation(12345, 67))
