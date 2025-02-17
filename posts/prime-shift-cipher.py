# Prime Shift Cipher

def prime_factorization(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def prime_shift_cipher(input_integer):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    factors = prime_factorization(input_integer)
    sequence = ""
    for i, factor in enumerate(factors):
        shift = factor % len(alphabet)
        char_index = i % len(alphabet)
        shifted_index = (char_index + shift) % len(alphabet)
        sequence += alphabet[shifted_index]
    return sequence

if __name__ == '__main__':
    input_number = 12345
    result = prime_shift_cipher(input_number)
    print(f"The sequence for {input_number} is: {result}")
