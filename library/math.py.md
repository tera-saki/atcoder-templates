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
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, Tuple, Optional\n\n\ndef divisors(n) -> List[int]:\n\
    \    \"\"\"return divisors of given integer\"\"\"\n    d = []\n    for i in range(1,\
    \ n + 1):\n        if i * i > n:\n            break\n        if i * i == n:\n\
    \            d.append(i)\n            break\n        if n % i == 0:\n        \
    \    d.append(i)\n            d.append(n // i)\n    return sorted(d)\n\n\ndef\
    \ factorize(n) -> List[int]:\n    \"\"\"return prime factors of given integer\"\
    \"\"\n    f = []\n    m = n\n    for i in range(2, n + 1):\n        if i * i >\
    \ n:\n            break\n        while m % i == 0:\n            f.append(i)\n\
    \            m //= i\n    if m > 1:\n        f.append(m)\n    return f\n\n\ndef\
    \ extgcd(a: int, b: int) -> Tuple[int, int, int]:\n    \"\"\"solve ax + by = gcd(a,\
    \ b)\"\"\"\n    x, y, u, v = 1, 0, 0, 1\n    while b:\n        q, r = divmod(a,\
    \ b)\n        x -= q * u\n        y -= q * v\n        x, u = u, x\n        y,\
    \ v = v, y\n        a, b = b, r\n    return a, x, y\n\n\ndef modinv(a: int, m:\
    \ int) -> Optional[int]:\n    \"\"\"return modular multiplicative inverse if exists\
    \ otherwise None\"\"\"\n    g, x, _ = extgcd(a, m)\n    return x if g == 1 else\
    \ None\n\n\ndef solve_ax_b(a: int, b: int, m: int) -> Optional[int]:\n    \"\"\
    \"solve ax \u2261 b (mod m)\"\"\"\n    g, x, _ = extgcd(a, m)\n    if b % g >\
    \ 0:\n        return None\n    a, b, m = a // g, b // g, m // g\n    return x\
    \ * b % m\n"
  dependsOn: []
  isVerificationFile: false
  path: library/math.py
  requiredBy: []
  timestamp: '2022-11-18 20:46:41+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/ntl_1_e.test.py
  - tests/aoj/ntl_1_a.test.py
  - tests/aoj/itp1_3_d.test.py
documentation_of: library/math.py
layout: document
redirect_from:
- /library/library/math.py
- /library/library/math.py.html
title: library/math.py
---
