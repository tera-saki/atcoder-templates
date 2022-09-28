---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/2320.test.py
    title: tests/aoj/2320.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Doubling:\n    def __init__(self, nex, digit=60):\n        self.d =\
    \ [[None for _ in range(len(nex))] for _ in range(digit)]\n        self.digit\
    \ = digit\n\n        self.d[0] = nex\n        for i in range(1, self.digit):\n\
    \            for j in range(len(nex)):\n                self.d[i][j] = self.d[i\
    \ - 1][self.d[i - 1][j]]\n\n    def solve(self, start, k):\n        p = start\n\
    \        for i in range(self.digit):\n            if k & 1:\n                p\
    \ = self.d[i][p]\n            k >>= 1\n        return p\n"
  dependsOn: []
  isVerificationFile: false
  path: library/doubling.py
  requiredBy: []
  timestamp: '2022-09-29 01:54:05+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/2320.test.py
documentation_of: library/doubling.py
layout: document
redirect_from:
- /library/library/doubling.py
- /library/library/doubling.py.html
title: library/doubling.py
---
