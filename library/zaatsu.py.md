---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/dsl_4_a.test.py
    title: tests/aoj/dsl_4_a.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Zaatsu:\n    def __init__(self, A):\n        self.A = sorted(set(A))\n\
    \        self.N = len(self.A)\n        self.D = {a: i for i, a in enumerate(self.A)}\n\
    \n    def id(self, a):\n        return self.D[a]\n\n    def value(self, i):\n\
    \        return self.A[i]\n"
  dependsOn: []
  isVerificationFile: false
  path: library/zaatsu.py
  requiredBy: []
  timestamp: '2023-01-07 00:50:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/dsl_4_a.test.py
documentation_of: library/zaatsu.py
layout: document
redirect_from:
- /library/library/zaatsu.py
- /library/library/zaatsu.py.html
title: library/zaatsu.py
---
