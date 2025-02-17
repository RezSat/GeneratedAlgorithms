import random

def chaotic_collatz(n, max_steps=100):
    steps = 0
    while n != 1 and steps < max_steps:
        if n % 2 == 0:
            divisor = random.randint(2, 5)
            n = n // divisor
        else:
            multiplier = random.randint(3, 7)
            adder = random.randint(1, 5)
            n = n * multiplier + adder
        steps += 1
        print(n)  # Print each step to observe the sequence

    if n == 1:
        return True
    else:
        return False

# Example usage:
# result = chaotic_collatz(10)
# print(f"Reaches 1: {result}")

if __name__ == "__main__":
    result = chaotic_collatz(10)
    print(f"Reaches 1: {result}")
