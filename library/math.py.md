---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
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
  code: "from typing import Tuple, Optional\n\n\ndef extgcd(a: int, b: int) -> Tuple[int,\
    \ int, int]:\n    \"\"\"solve ax + by = gcd(a, b)\"\"\"\n    x, y, u, v = 1, 0,\
    \ 0, 1\n    while b:\n        q, r = divmod(a, b)\n        x -= q * u\n      \
    \  y -= q * v\n        x, u = u, x\n        y, v = v, y\n        a, b = b, r\n\
    \    return a, x, y\n\n\ndef modinv(a: int, m: int) -> Optional[int]:\n    \"\"\
    \"return modular multiplicative inverse if exists otherwise None\"\"\"\n    g,\
    \ x, _ = extgcd(a, m)\n    return x if g == 1 else None\n\n\ndef solve_ax_b(a:\
    \ int, b: int, m: int) -> Optional[int]:\n    \"\"\"solve ax \u2261 b (mod m)\"\
    \"\"\n    g, x, _ = extgcd(a, m)\n    if b % g > 0:\n        return None\n   \
    \ a, b, m = a // g, b // g, m // g\n    return x * b % m\n"
  dependsOn: []
  isVerificationFile: false
  path: library/math.py
  requiredBy: []
  timestamp: '2022-10-23 14:24:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/ntl_1_e.test.py
documentation_of: library/math.py
layout: document
redirect_from:
- /library/library/math.py
- /library/library/math.py.html
title: library/math.py
---
