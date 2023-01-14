---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/2858.test.py
    title: tests/aoj/2858.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List\nimport math\n\n\nclass SegmentSieve:\n    def __init__(self,\
    \ N: int):\n        self.square_n = math.ceil(math.sqrt(N))\n        is_prime\
    \ = [True] * (self.square_n + 1)\n        is_prime[0] = False\n        is_prime[1]\
    \ = False\n\n        for p in range(2, self.square_n + 1):\n            if not\
    \ is_prime[p]:\n                continue\n            for j in range(2, self.square_n\
    \ + 1):\n                if p * j > self.square_n:\n                    break\n\
    \                is_prime[p * j] = False\n\n        # primes smaller than \u221A\
    N\n        self.prime_sqn = [p for p in range(2, self.square_n + 1) if is_prime[p]]\n\
    \n    def get_primes(self, l: int, r: int) -> List[int]:\n        \"\"\"return\
    \ list of primes (l <= p <= r)\"\"\"\n        l = max(l, 2)\n        if l > r:\n\
    \            return []\n        factors = self._do_sieve(l, r)\n        return\
    \ [p for p in range(l, r + 1) if not factors[p - l]]\n\n    def get_factors(self,\
    \ l: int, r: int) -> List[List[int]]:\n        \"\"\"return list of factors of\
    \ n (l <= n <= r)\"\"\"\n        l = max(l, 2)\n        if l > r:\n          \
    \  return []\n        factors = self._do_sieve(l, r)\n        ret = [[] for _\
    \ in range(r - l + 1)]\n        for i, n in enumerate(range(l, r + 1)):\n    \
    \        for f in factors[i]:\n                if n == 1:\n                  \
    \  break\n                while n % f == 0:\n                    ret[i].append(f)\n\
    \                    n //= f\n            if n > 1:\n                ret[i].append(n)\n\
    \        return ret\n\n    def _do_sieve(self, l: int, r: int) -> List[int]:\n\
    \        is_prime = [True] * (r - l + 1)\n        factors = [[] for _ in range(l,\
    \ r + 1)]\n        for p in self.prime_sqn:\n            start = l + (-l) % p\n\
    \            if start == p:\n                start *= 2\n            for i in\
    \ range(start, r + 1, p):\n                factors[i - l].append(p)\n        return\
    \ factors\n"
  dependsOn: []
  isVerificationFile: false
  path: library/segment_sieve.py
  requiredBy: []
  timestamp: '2023-01-14 13:08:15+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/2858.test.py
documentation_of: library/segment_sieve.py
layout: document
redirect_from:
- /library/library/segment_sieve.py
- /library/library/segment_sieve.py.html
title: library/segment_sieve.py
---
