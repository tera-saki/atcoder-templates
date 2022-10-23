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
  code: "from typing import List, Tuple, Optional\n\n\nclass BellmanFord:\n    def\
    \ __init__(self, N: int, E: List[List[Tuple[int, int]]],\n                 start:\
    \ int = 0, inf: int = 1 << 60):\n        self.N = N\n        self.E = E\n    \
    \    self.start = start\n        self.inf = inf\n        self.C = [self.inf] *\
    \ N\n\n        self._calculate()\n\n    def get_cost(self, i: int) -> int:\n \
    \       \"\"\"\n        return the cost to i-th vertex from start.\n        If\
    \ the return value is inf, the vertex is unreachable.\n        If the return value\
    \ is -inf, the path to the vertex includes negative cycle.\n        \"\"\"\n \
    \       return self.C[i]\n\n    def _calculate(self):\n        self.C[self.start]\
    \ = 0\n        for _ in range(self.N - 1):\n            update = False\n     \
    \       for u in range(self.N):\n                if self.C[u] == self.inf:\n \
    \                   continue\n                for c, v in self.E[u]:\n       \
    \             if self.C[v] > self.C[u] + c:\n                        self.C[v]\
    \ = self.C[u] + c\n                        update = True\n            if not update:\n\
    \                break\n\n        nc = [False] * self.N\n        for _ in range(self.N):\n\
    \            for u in range(self.N):\n                if self.C[u] == self.inf:\n\
    \                    continue\n                for c, v in self.E[u]:\n      \
    \              if self.C[v] > self.C[u] + c:\n                        self.C[v]\
    \ = self.C[u] + c\n                        nc[v] = True\n                    if\
    \ nc[u]:\n                        nc[v] = True\n\n        for u in range(self.N):\n\
    \            if nc[u]:\n                self.C[u] = -self.inf\n"
  dependsOn: []
  isVerificationFile: false
  path: library/bellman_ford.py
  requiredBy: []
  timestamp: '2022-10-23 16:02:40+09:00'
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
