---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/cumulative_sum.test.py
    title: tests/cumulative_sum.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class CumulativeSum2D:\n    def __init__(self, A):\n        self.A = A\n\
    \        self.H = len(A)\n        self.W = len(A[0])\n        self.S = [[0 for\
    \ _ in range(self.W + 1)] for _ in range(self.H + 1)]\n\n        for i in range(self.H):\n\
    \            for j in range(self.W):\n                self.S[i + 1][j + 1] = self.S[i\
    \ + 1][j] + self.S[i][j + 1] - self.S[i][j] + self.A[i][j]\n\n    def sum(self,\
    \ lx, ly, rx, ry):\n        \"\"\"return sum of area s.t. lx <= x <= rx and ly\
    \ <= y <= ry (0-indexed)\"\"\"\n        return self.S[rx + 1][ry + 1] - self.S[lx][ry\
    \ + 1] - self.S[rx + 1][ly] + self.S[lx][ly]\n"
  dependsOn: []
  isVerificationFile: false
  path: library/cumulative_sum.py
  requiredBy: []
  timestamp: '2022-09-19 11:29:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/cumulative_sum.test.py
documentation_of: library/cumulative_sum.py
layout: document
redirect_from:
- /library/library/cumulative_sum.py
- /library/library/cumulative_sum.py.html
title: library/cumulative_sum.py
---
