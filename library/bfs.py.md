---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/alds1_11_c.test.py
    title: tests/aoj/alds1_11_c.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, Tuple, Optional\nfrom collections import deque\n\
    \n\nclass BFS:\n    def __init__(self, N: int, E: List[List[int]],\n         \
    \        start: int = 0, inf: int = 1 << 50):\n        self.N = N\n        self.E\
    \ = E\n        self.start = start\n        self.inf = inf\n\n        self.C =\
    \ [self.inf] * N\n        self.prev = [None] * N\n\n        self._search()\n\n\
    \    def get_cost(self, i: int) -> int:\n        return self.C[i]\n\n    def get_path(self,\
    \ i: int) -> Optional[List[int]]:\n        if not self.reachable(i):\n       \
    \     return None\n\n        p = []\n        cur = i\n        while cur is not\
    \ None:\n            p.append(cur)\n            cur = self.prev[cur]\n       \
    \ p.reverse()\n        return p\n\n    def reachable(self, i: int) -> bool:\n\
    \        return self.C[i] < self.inf\n\n    def _search(self) -> None:\n     \
    \   dq = deque([(self.start, -1)])\n        self.C[self.start] = 0\n        while\
    \ dq:\n            v, p = dq.popleft()\n            if p >= 0:\n             \
    \   self.prev[v] = p\n            for d in self.E[v]:\n                if self.C[d]\
    \ > self.C[v] + 1:\n                    self.C[d] = self.C[v] + 1\n          \
    \          dq.append((d, v))\n"
  dependsOn: []
  isVerificationFile: false
  path: library/bfs.py
  requiredBy: []
  timestamp: '2022-11-16 21:06:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/alds1_11_c.test.py
documentation_of: library/bfs.py
layout: document
redirect_from:
- /library/library/bfs.py
- /library/library/bfs.py.html
title: library/bfs.py
---
