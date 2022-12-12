---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/0560.test.py
    title: tests/aoj/0560.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class CumulativeSum2D:\n    def __init__(self, A):\n        self.A = A\n\
    \        self.H = len(A)\n        self.W = len(A[0])\n        self.S = [0] * ((self.W\
    \ + 1) * (self.H + 1))\n\n        for i in range(self.H):\n            for j in\
    \ range(self.W):\n                self.S[self.id(i + 1, j + 1)] = self.S[self.id(i\
    \ + 1, j)] + self.S[(self.id(i, j + 1))] - self.S[(self.id(i, j))] + self.A[i][j]\n\
    \n    def sum(self, lx, ly, rx, ry):\n        \"\"\"return sum of area s.t. lx\
    \ <= x < rx and ly <= y < ry (0-indexed)\"\"\"\n        return self.S[self.id(rx,\
    \ ry)] - self.S[self.id(lx, ry)] - self.S[self.id(rx, ly)] + self.S[self.id(lx,\
    \ ly)]\n\n    def id(self, x, y):\n        return x * self.W + y\n"
  dependsOn: []
  isVerificationFile: false
  path: library/cumulative_sum_2d.py
  requiredBy: []
  timestamp: '2022-12-12 21:09:36+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/0560.test.py
documentation_of: library/cumulative_sum_2d.py
layout: document
redirect_from:
- /library/library/cumulative_sum_2d.py
- /library/library/cumulative_sum_2d.py.html
title: library/cumulative_sum_2d.py
---
