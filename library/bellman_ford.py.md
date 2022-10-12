---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/grl_1_b.test.py
    title: tests/aoj/grl_1_b.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BellmanFord:\n    def __init__(self, N, E, start=0, inf=1 << 50):\n\
    \        self.N = N\n        self.E = E\n        self.start = start\n        self.inf\
    \ = inf\n        self.C = [self.inf] * N\n\n        self.negative_cycle = False\n\
    \        self._calculate()\n\n    def get_cost(self, i):\n        return self.C[i]\
    \ if not self.negative_cycle else None\n\n    def _calculate(self):\n        self.C[self.start]\
    \ = 0\n        for cnt in range(self.N):\n            update = False\n       \
    \     for u in range(self.N):\n                if self.C[u] == self.inf:\n   \
    \                 continue\n                for c, v in self.E[u]:\n         \
    \           if self.C[v] > self.C[u] + c:\n                        self.C[v] =\
    \ self.C[u] + c\n                        update = True\n            if not update:\n\
    \                return\n        self.negative_cycle = True\n"
  dependsOn: []
  isVerificationFile: false
  path: library/bellman_ford.py
  requiredBy: []
  timestamp: '2022-10-12 22:37:07+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/grl_1_b.test.py
documentation_of: library/bellman_ford.py
layout: document
redirect_from:
- /library/library/bellman_ford.py
- /library/library/bellman_ford.py.html
title: library/bellman_ford.py
---
