def prime_factor_sequence(limit, seed):
    """
    Generates a sequence of numbers based on the prime factors of numbers up to a limit,
    influenced by an initial seed value.

    For each number, it finds the prime factors, sums them, and then applies a simple
    formula involving the seed to generate the next number in the sequence. This aims
    to create a sequence that is deterministic given the seed and limit, but appears
    random and is sensitive to changes in the seed.
    """
    sequence = []
    current = seed
    for i in range(2, limit + 1):
        factors = []
        n = i
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)

        if factors:
            factor_sum = sum(factors)
            current = (current + factor_sum * seed) % limit
        else:
            current = (current + seed) % limit
        sequence.append(current)
    return sequence

if __name__ == "__main__":
    limit = 100
    seed = 42
    result = prime_factor_sequence(limit, seed)
    print(f"Prime Factor Sequence with limit={limit}, seed={seed}:")
    print(result)
