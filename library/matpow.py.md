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
    - https://atcoder.jp/contests/dp/tasks/dp_r
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 97, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\ninput = sys.stdin.readline\n\n\nclass Matpow:\n    def __init__(self,\
    \ A, mod, digit=60):\n        self.A = A\n        self.N = len(A)\n        self.mod\
    \ = mod\n        self.digit = digit\n        self.doubling = [None] * self.digit\n\
    \n        self.doubling[0] = A\n        for i in range(1, self.digit):\n     \
    \       self.doubling[i] = self.mul(self.doubling[i - 1], self.doubling[i - 1])\n\
    \n    def pow(self, n):\n        E = [[1 if i == j else 0 for j in range(self.N)]\
    \ for i in range(self.N)]\n        acc = E\n        for k in range(self.digit):\n\
    \            if n & (1 << k):\n                acc = self.mul(acc, self.doubling[k])\n\
    \        return acc\n\n    def mul(self, A, B):\n        C = [[0 for _ in range(self.N)]\
    \ for _ in range(self.N)]\n        for i in range(self.N):\n            for j\
    \ in range(self.N):\n                for k in range(self.N):\n               \
    \     C[i][j] += A[i][k] * B[k][j]\n                    C[i][j] %= self.mod\n\
    \        return C\n\n\n# https://atcoder.jp/contests/dp/tasks/dp_r\nN, K = map(int,\
    \ input().split())\nA = [list(map(int, input().split())) for _ in range(N)]\n\
    mod = 10 ** 9 + 7\n\nAk = Matpow(A, mod).pow(K)\nans = 0\nfor i in range(N):\n\
    \    for j in range(N):\n        ans += Ak[i][j]\n        ans %= mod\nprint(ans)\n"
  dependsOn: []
  isVerificationFile: false
  path: library/matpow.py
  requiredBy: []
  timestamp: '2022-09-18 13:43:26+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library/matpow.py
layout: document
redirect_from:
- /library/library/matpow.py
- /library/library/matpow.py.html
title: library/matpow.py
---
