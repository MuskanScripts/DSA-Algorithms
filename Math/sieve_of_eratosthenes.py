"""
Sieve of Eratosthenes

Find all prime numbers up to a given limit n.

Time Complexity:  O(n log log n)
Space Complexity: O(n)
"""


def sieve_of_eratosthenes(n):
    """Returns a list of all prime numbers up to n (inclusive)."""
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    return [i for i, prime in enumerate(is_prime) if prime]


def segmented_sieve(low, high):
    """
    Find primes in the range [low, high] using the segmented sieve.
    More memory efficient for large ranges.
    """
    import math
    limit = int(math.sqrt(high)) + 1
    base_primes = sieve_of_eratosthenes(limit)

    size = high - low + 1
    is_prime = [True] * size

    for p in base_primes:
        # Find the smallest multiple of p >= low
        start = max(p * p, ((low + p - 1) // p) * p)
        for j in range(start, high + 1, p):
            is_prime[j - low] = False

    if low == 1:
        is_prime[0] = False

    return [low + i for i, v in enumerate(is_prime) if v]


if __name__ == "__main__":
    n = 50
    primes = sieve_of_eratosthenes(n)
    print(f"Primes up to {n}: {primes}")
    print(f"Count: {len(primes)}")

    low, high = 50, 100
    seg_primes = segmented_sieve(low, high)
    print(f"\nPrimes between {low} and {high}: {seg_primes}")
