def generate_fingerprint(input_string):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    fingerprint = 1
    for i, char in enumerate(input_string):
        fingerprint = (fingerprint * prime_numbers[i % len(prime_numbers)] * ord(char)) % 100000
    return fingerprint

if __name__ == "__main__":
    test_string = "example string"
    fingerprint = generate_fingerprint(test_string)
    print(f"The fingerprint for '{test_string}' is: {fingerprint}")