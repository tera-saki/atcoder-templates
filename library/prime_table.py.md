---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/prime_table.test.py
    title: tests/prime_table.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class PrimeTable:\n    def __init__(self, N):\n        self.is_prime = [True]\
    \ * (N + 1)\n\n        self.is_prime[0] = False\n        self.is_prime[1] = False\n\
    \        for i in range(2, N + 1):\n            if i * i > N:\n              \
    \  break\n            if self.is_prime[i] is False:\n                continue\n\
    \            for j in range(2, N + 1):\n                if i * j > N:\n      \
    \              break\n                self.is_prime[i * j] = False\n\n       \
    \ self.primes = [n for n in range(2, N + 1) if self.is_prime[n]]\n"
  dependsOn: []
  isVerificationFile: false
  path: library/prime_table.py
  requiredBy: []
  timestamp: '2022-09-23 21:22:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/prime_table.test.py
documentation_of: library/prime_table.py
layout: document
redirect_from:
- /library/library/prime_table.py
- /library/library/prime_table.py.html
title: library/prime_table.py
---
