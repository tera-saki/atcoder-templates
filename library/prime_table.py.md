---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://onlinejudge.u-aizu.ac.jp/status/users/terasa/submissions/1/0053/judge/6971267/Python3
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://onlinejudge.u-aizu.ac.jp/status/users/terasa/submissions/1/0053/judge/6971267/Python3\n\
    import sys\ninput = sys.stdin.readline\n\n\nclass PrimeTable:\n    def __init__(self,\
    \ N):\n        self.is_prime = [True] * (N + 1)\n\n        self.is_prime[0] =\
    \ False\n        self.is_prime[1] = False\n        for i in range(2, N + 1):\n\
    \            if i * i > N:\n                break\n            if self.is_prime[i]\
    \ is False:\n                continue\n            for j in range(2, N + 1):\n\
    \                if i * j > N:\n                    break\n                self.is_prime[i\
    \ * j] = False\n\n        self.primes = [n for n in range(2, N + 1) if self.is_prime[n]]\n\
    \n    def is_prime(self, n):\n        return self.is_prime[n]\n\n\nprimes = PrimeTable(10\
    \ ** 6).primes\nS = [0]\nfor p in primes:\n    S.append(S[-1] + p)\nwhile True:\n\
    \    n = int(input())\n    if n == 0:\n        break\n    print(S[n])\n"
  dependsOn: []
  isVerificationFile: false
  path: library/prime_table.py
  requiredBy: []
  timestamp: '2022-09-19 00:58:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library/prime_table.py
layout: document
redirect_from:
- /library/library/prime_table.py
- /library/library/prime_table.py.html
title: library/prime_table.py
---
