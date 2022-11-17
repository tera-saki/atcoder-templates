---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/static_range_inversions_query.test.py
    title: tests/yosupo/static_range_inversions_query.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Mo:\n    def __init__(self, N, Q, A, query):\n        # divide queries\
    \ into \u221AQ buckets\n        # thus the size of each bucket is N/\u221AQ\n\
    \        self.N = N\n        self.Q = Q\n        self.A = A\n        self.query\
    \ = query\n        self.b_num = int(Q ** .5)\n\n        self.ans = [None] * Q\n\
    \        self.acc = 0\n        self.cnt = 0\n        self.L = 0\n        self.R\
    \ = 0\n\n        # decide which bucket the query is placed to by left-end value\n\
    \        # sort queries by bucket number, and sort queries in a bucket by right-end\
    \ value\n        # in asc order if bucket's index is even otherwise in desc order\n\
    \        # (the constant factor will be smaller)\n\n        def cmp(i):\n    \
    \        l, r = self.query[i]\n            b = l * self.b_num // N\n         \
    \   return (b << 32) + (~r if b & 1 else r)\n\n        C = [cmp(i) for i in range(Q)]\n\
    \        self.order = sorted(range(Q), key=lambda i: C[i])\n\n    def solve(self):\n\
    \        for i in self.order:\n            l, r = self.query[i]\n            #\
    \ extend left-end\n            # decrement at first since current A[L] is already\
    \ included ([L:R))\n            while l < self.L:\n                self.L -= 1\n\
    \                self.extend_left(self.L)\n            # extend right-end\n  \
    \          # increment at last since current A[R] is not included yet ([L:R))\n\
    \            while self.R < r:\n                self.extend_right(self.R)\n  \
    \              self.R += 1\n            # shrink left-end\n            # increment\
    \ at last since current A[L] is included ([L:R))\n            while self.L < l:\n\
    \                self.shrink_left(self.L)\n                self.L += 1\n     \
    \       # shrink right-end\n            # decrement at first since current A[R]\
    \ is not included ([L:R))\n            while r < self.R:\n                self.R\
    \ -= 1\n                self.shrink_right(self.R)\n            self.ans[i] = self.acc\n\
    \        return self.ans\n\n    def extend_left(self, i):\n        raise NotImplementedError()\n\
    \n    def extend_right(self, i):\n        raise NotImplementedError()\n\n    def\
    \ shrink_left(self, i):\n        raise NotImplementedError()\n\n    def shrink_right(self,\
    \ i):\n        raise NotImplementedError()\n"
  dependsOn: []
  isVerificationFile: false
  path: library/mo.py
  requiredBy: []
  timestamp: '2022-11-17 21:56:10+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/yosupo/static_range_inversions_query.test.py
documentation_of: library/mo.py
layout: document
redirect_from:
- /library/library/mo.py
- /library/library/mo.py.html
title: library/mo.py
---
