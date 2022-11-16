from typing import Tuple, Optional


def divisors(n):
    """return divisors of given integer"""
    d = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if i * i == n:
            d.append(i)
            break
        if n % i == 0:
            d.append(i)
            d.append(n // i)
    return sorted(d)


def factorize(n):
    """return prime factors of given integer"""
    f = []
    m = n
    for i in range(2, n + 1):
        if i * i > n:
            break
        while m % i == 0:
            f.append(i)
            m //= i
    if m > 1:
        f.append(m)
    return f


def extgcd(a: int, b: int) -> Tuple[int, int, int]:
    """solve ax + by = gcd(a, b)"""
    x, y, u, v = 1, 0, 0, 1
    while b:
        q, r = divmod(a, b)
        x -= q * u
        y -= q * v
        x, u = u, x
        y, v = v, y
        a, b = b, r
    return a, x, y


def modinv(a: int, m: int) -> Optional[int]:
    """return modular multiplicative inverse if exists otherwise None"""
    g, x, _ = extgcd(a, m)
    return x if g == 1 else None


def solve_ax_b(a: int, b: int, m: int) -> Optional[int]:
    """solve ax ≡ b (mod m)"""
    g, x, _ = extgcd(a, m)
    if b % g > 0:
        return None
    a, b, m = a // g, b // g, m // g
    return x * b % m
