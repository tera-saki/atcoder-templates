from typing import List, Tuple, Optional
import math


def divisors(n) -> List[int]:
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


def factorize(n) -> List[int]:
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


def crt(P: List[Tuple[int, int]]) -> Tuple[int, int]:
    """return the smallest x that satisfies x ≡ a (mod m) for all (a, m) pairs and lcm(M)
    # reference: https://qiita.com/drken/items/ae02240cd1f8edfc86fd
    """
    """
    let g = gcd(m1, m2).
    if there exist x s.t. x ≡ a1 (mod m1) and x ≡ a2 (mod m2),
    since m1 and m2 are multiple of g, x ≡ a1 (mod g) and x ≡ a2 (mod g).
    therefore a1 ≡ a2 (mod g).

    there exist (p, q) s.t. m1 * p + m2 * q = gcd(m1, m2). (this can be obtained by extgcd)
    let s = (a2 - a1) / g
    then m1 * p + m2 * q = g
    <=> m1 * p + m2 * q = (a2 - a1) / s
    <=> s * m1 * p + s * m2 * q = a2 - a1
    <=> a1 + s + m1 + p = a2 - s * m2 * q

    let x = a1 + s * m1 * p (= a2 - s * m2 * q)
    then x ≡ a1 (mod m1), x ≡ a2 (mod m2).
    """
    r = 0
    M = 1
    for a, m in P:
        g, p, q = extgcd(M, m)
        if (a - r) % g != 0:
            return (0, -1)
        s = (a - r) // g
        tmp = s * p % (m // g)
        r += M * tmp
        M *= m // g
    return (r, M)


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


def solve_discrete_logarithm(x: int, y: int, m: int, start: int = 0) -> Optional[int]:
    """return the smallest k that satisfies x^k ≡ y (mod m) if exist, otherwise None
    reference: https://qiita.com/suisen_cp/items/d597c8ec576ae32ee2d7
    """
    if m == 1:
        return start
    x %= m
    y %= m
    """
    suppose x^d * x^t ≡ y (d >= 0)
    let g = gcd(x^d, m)
    <=> x^t ≡ y/g * (x^d / g)^(-1) (mod m/g)
    <=> x^t ≡ y * (x^d)^(-1) (mod m/g)
    <=> x^t ≡ y' (mod m') where y' ≡ y * (x^d)^(-1) and m' = m/g
    """
    d = m.bit_length()
    pow_x = pow(x, start, m)
    for k in range(start, d):
        if pow_x == y:
            return k
        pow_x = pow_x * x % m
    g = math.gcd(pow_x, m)
    if y % g != 0:
        return None
    m //= g
    x %= m
    y = y * modinv(pow_x, m) % m
    if x == 0:
        return d + 1 if y == 0 else d if y == 1 else None

    def ceil_sqrt(n: int) -> int:
        """find sqrt(ceil(n))"""
        l = -1
        r = n
        while r - l > 1:
            c = (l + r) >> 1
            if c * c >= n:
                r = c
            else:
                l = c
        return r

    """
    let p = ceil(sqrt(m)) and k = p * i + q (0 <= q < p)
    x^k ≡ y
    <=> x^(p*i+q) ≡ y
    <=> x^q ≡ y * ((x^(-1))^p)^i
    <=> x^q ≡ y * a^i where a = (x^(-1))^p
    """
    p = ceil_sqrt(m)
    a = pow(modinv(x, m), p, m)

    D = {}
    pow_x = 1
    for i in range(p):
        D.setdefault(pow_x, i)
        pow_x = pow_x * x % m
    pow_a = 1
    for i in range(p):
        val = y * pow_a % m
        q = D.get(val)
        if q is not None:
            k = p * i + q + d
            if k >= start:
                return k
        pow_a = pow_a * a % m
    return None
