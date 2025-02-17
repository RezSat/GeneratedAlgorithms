import random

def recursive_string_scrambler(s):
    if len(s) <= 1:
        return s

    split_point = random.randint(1, len(s) - 1)
    left = s[:split_point]
    right = s[split_point:]

    scrambled_left = recursive_string_scrambler(left)
    scrambled_right = recursive_string_scrambler(right)

    if random.random() < 0.5:
        return scrambled_left + scrambled_right
    else:
        return scrambled_right + scrambled_left

# Example usage:
# string = "abcdefgh"
# scrambled_string = recursive_string_scrambler(string)
# print(f"Original string: {string}")
# print(f"Scrambled string: {scrambled_string}")

if __name__ == "__main__":
    string = "abcdefgh"
    scrambled_string = recursive_string_scrambler(string)
    print(f"Original string: {string}")
    print(f"Scrambled string: {scrambled_string}")
