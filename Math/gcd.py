"""
Euclidean Algorithm — Greatest Common Divisor (GCD)

Computes the GCD of two integers using the Euclidean algorithm.
Also includes the Extended Euclidean Algorithm which finds
integers x, y such that: ax + by = gcd(a, b)

Time Complexity:  O(log(min(a, b)))
Space Complexity: O(1) iterative / O(log(min(a,b))) recursive
"""


def gcd(a, b):
    """Iterative Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a, b):
    """Recursive Euclidean algorithm."""
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def extended_gcd(a, b):
    """
    Returns (gcd, x, y) such that a*x + b*y = gcd.
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def lcm(a, b):
    """Least Common Multiple using GCD."""
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    a, b = 56, 98
    print(f"GCD({a}, {b}) = {gcd(a, b)}")
    print(f"LCM({a}, {b}) = {lcm(a, b)}")

    g, x, y = extended_gcd(a, b)
    print(f"Extended GCD: {a}*({x}) + {b}*({y}) = {g}")
    assert a * x + b * y == g
