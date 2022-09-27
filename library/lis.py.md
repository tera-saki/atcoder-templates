---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/lis.test.py
    title: tests/lis.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from operator import lt, le\n\n\nclass LIS:\n    def __init__(self, A):\n\
    \        self.A = A\n        self.N = len(A)\n\n    def solve(self, strict=True):\n\
    \        S = [self.A[0]]\n        cmp = lt if strict else le\n        for i in\
    \ range(1, self.N):\n            if cmp(S[-1], self.A[i]):\n                S.append(self.A[i])\n\
    \            else:\n                l = -1\n                r = len(S)\n     \
    \           while r - l > 1:\n                    c = (l + r) // 2\n         \
    \           if cmp(S[c], self.A[i]):\n                        l = c\n        \
    \            else:\n                        r = c\n                S[r] = self.A[i]\n\
    \        return len(S)\n"
  dependsOn: []
  isVerificationFile: false
  path: library/lis.py
  requiredBy: []
  timestamp: '2022-09-27 23:13:15+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/lis.test.py
documentation_of: library/lis.py
layout: document
redirect_from:
- /library/library/lis.py
- /library/library/lis.py.html
title: library/lis.py
---
