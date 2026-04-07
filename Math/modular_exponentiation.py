"""
Modular Exponentiation

Compute (base ^ exponent) % modulus efficiently using
repeated squaring (binary exponentiation).

Time Complexity:  O(log exponent)
Space Complexity: O(1) iterative / O(log exponent) recursive
"""


def mod_exp_iterative(base, exp, mod):
    """Iterative binary exponentiation."""
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result


def mod_exp_recursive(base, exp, mod):
    """Recursive binary exponentiation."""
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = mod_exp_recursive(base, exp // 2, mod)
        return (half * half) % mod
    return (base * mod_exp_recursive(base, exp - 1, mod)) % mod


if __name__ == "__main__":
    test_cases = [
        (2, 10, 1000),
        (3, 200, 1000000007),
        (5, 0, 13),
        (7, 1, 13),
    ]
    for base, exp, mod in test_cases:
        result = mod_exp_iterative(base, exp, mod)
        print(f"{base}^{exp} mod {mod} = {result}")
        assert result == pow(base, exp, mod), "Mismatch with built-in pow"
    print("All assertions passed.")
