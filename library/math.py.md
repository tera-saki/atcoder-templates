---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/itp1_3_d.test.py
    title: tests/aoj/itp1_3_d.test.py
  - icon: ':heavy_check_mark:'
    path: tests/aoj/ntl_1_a.test.py
    title: tests/aoj/ntl_1_a.test.py
  - icon: ':heavy_check_mark:'
    path: tests/aoj/ntl_1_e.test.py
    title: tests/aoj/ntl_1_e.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/discrete_logarithm_mod.test.py
    title: tests/yosupo/discrete_logarithm_mod.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yuki/186.test.py
    title: tests/yuki/186.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://qiita.com/drken/items/ae02240cd1f8edfc86fd
    - https://qiita.com/suisen_cp/items/d597c8ec576ae32ee2d7
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, Tuple, Optional\nimport math\n\n\ndef divisors(n)\
    \ -> List[int]:\n    \"\"\"return divisors of given integer\"\"\"\n    d = []\n\
    \    for i in range(1, n + 1):\n        if i * i > n:\n            break\n   \
    \     if i * i == n:\n            d.append(i)\n            break\n        if n\
    \ % i == 0:\n            d.append(i)\n            d.append(n // i)\n    return\
    \ sorted(d)\n\n\ndef factorize(n) -> List[int]:\n    \"\"\"return prime factors\
    \ of given integer\"\"\"\n    f = []\n    m = n\n    for i in range(2, n + 1):\n\
    \        if i * i > n:\n            break\n        while m % i == 0:\n       \
    \     f.append(i)\n            m //= i\n    if m > 1:\n        f.append(m)\n \
    \   return f\n\n\ndef extgcd(a: int, b: int) -> Tuple[int, int, int]:\n    \"\"\
    \"solve ax + by = gcd(a, b)\"\"\"\n    x, y, u, v = 1, 0, 0, 1\n    while b:\n\
    \        q, r = divmod(a, b)\n        x -= q * u\n        y -= q * v\n       \
    \ x, u = u, x\n        y, v = v, y\n        a, b = b, r\n    return a, x, y\n\n\
    \ndef crt(P: List[Tuple[int, int]]) -> Tuple[int, int]:\n    \"\"\"return the\
    \ smallest x that satisfies x \u2261 a (mod m) for all (a, m) pairs and lcm(M)\n\
    \    # reference: https://qiita.com/drken/items/ae02240cd1f8edfc86fd\n    \"\"\
    \"\n    \"\"\"\n    let g = gcd(m1, m2).\n    if there exist x s.t. x \u2261 a1\
    \ (mod m1) and x \u2261 a2 (mod m2),\n    since m1 and m2 are multiple of g, x\
    \ \u2261 a1 (mod g) and x \u2261 a2 (mod g).\n    therefore a1 \u2261 a2 (mod\
    \ g).\n\n    there exist (p, q) s.t. m1 * p + m2 * q = gcd(m1, m2). (this can\
    \ be obtained by extgcd)\n    let s = (a2 - a1) / g\n    then m1 * p + m2 * q\
    \ = g\n    <=> m1 * p + m2 * q = (a2 - a1) / s\n    <=> s * m1 * p + s * m2 *\
    \ q = a2 - a1\n    <=> a1 + s + m1 + p = a2 - s * m2 * q\n\n    let x = a1 + s\
    \ * m1 * p (= a2 - s * m2 * q)\n    then x \u2261 a1 (mod m1), x \u2261 a2 (mod\
    \ m2).\n    \"\"\"\n    r = 0\n    M = 1\n    for a, m in P:\n        g, p, q\
    \ = extgcd(M, m)\n        if (a - r) % g != 0:\n            return (0, -1)\n \
    \       s = (a - r) // g\n        tmp = s * p % (m // g)\n        r += M * tmp\n\
    \        M *= m // g\n    return (r, M)\n\n\ndef modinv(a: int, m: int) -> Optional[int]:\n\
    \    \"\"\"return modular multiplicative inverse if exists otherwise None\"\"\"\
    \n    g, x, _ = extgcd(a, m)\n    return x if g == 1 else None\n\n\ndef solve_ax_b(a:\
    \ int, b: int, m: int) -> Optional[int]:\n    \"\"\"solve ax \u2261 b (mod m)\"\
    \"\"\n    g, x, _ = extgcd(a, m)\n    if b % g > 0:\n        return None\n   \
    \ a, b, m = a // g, b // g, m // g\n    return x * b % m\n\n\ndef solve_discrete_logarithm(x:\
    \ int, y: int, m: int, start: int = 0) -> Optional[int]:\n    \"\"\"return the\
    \ smallest k that satisfies x^k \u2261 y (mod m) if exist, otherwise None\n  \
    \  reference: https://qiita.com/suisen_cp/items/d597c8ec576ae32ee2d7\n    \"\"\
    \"\n    if m == 1:\n        return start\n    x %= m\n    y %= m\n    \"\"\"\n\
    \    suppose x^d * x^t \u2261 y (d >= 0)\n    let g = gcd(x^d, m)\n    <=> x^t\
    \ \u2261 y/g * (x^d / g)^(-1) (mod m/g)\n    <=> x^t \u2261 y * (x^d)^(-1) (mod\
    \ m/g)\n    <=> x^t \u2261 y' (mod m') where y' \u2261 y * (x^d)^(-1) and m' =\
    \ m/g\n    \"\"\"\n    d = m.bit_length()\n    pow_x = pow(x, start, m)\n    for\
    \ k in range(start, d):\n        if pow_x == y:\n            return k\n      \
    \  pow_x = pow_x * x % m\n    g = math.gcd(pow_x, m)\n    if y % g != 0:\n   \
    \     return None\n    m //= g\n    x %= m\n    y = y * modinv(pow_x, m) % m\n\
    \    if x == 0:\n        return d + 1 if y == 0 else d if y == 1 else None\n\n\
    \    def ceil_sqrt(n: int) -> int:\n        \"\"\"find sqrt(ceil(n))\"\"\"\n \
    \       l = -1\n        r = n\n        while r - l > 1:\n            c = (l +\
    \ r) >> 1\n            if c * c >= n:\n                r = c\n            else:\n\
    \                l = c\n        return r\n\n    \"\"\"\n    let p = ceil(sqrt(m))\
    \ and k = p * i + q (0 <= q < p)\n    x^k \u2261 y\n    <=> x^(p*i+q) \u2261 y\n\
    \    <=> x^q \u2261 y * ((x^(-1))^p)^i\n    <=> x^q \u2261 y * a^i where a = (x^(-1))^p\n\
    \    \"\"\"\n    p = ceil_sqrt(m)\n    a = pow(modinv(x, m), p, m)\n\n    D =\
    \ {}\n    pow_x = 1\n    for i in range(p):\n        D.setdefault(pow_x, i)\n\
    \        pow_x = pow_x * x % m\n    pow_a = 1\n    for i in range(p):\n      \
    \  val = y * pow_a % m\n        q = D.get(val)\n        if q is not None:\n  \
    \          k = p * i + q + d\n            if k >= start:\n                return\
    \ k\n        pow_a = pow_a * a % m\n    return None\n"
  dependsOn: []
  isVerificationFile: false
  path: library/math.py
  requiredBy: []
  timestamp: '2022-12-24 12:53:33+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/ntl_1_a.test.py
  - tests/aoj/ntl_1_e.test.py
  - tests/aoj/itp1_3_d.test.py
  - tests/yuki/186.test.py
  - tests/yosupo/discrete_logarithm_mod.test.py
documentation_of: library/math.py
layout: document
redirect_from:
- /library/library/math.py
- /library/library/math.py.html
title: library/math.py
---
