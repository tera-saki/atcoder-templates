---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/shortest_path.test.py
    title: tests/yosupo/shortest_path.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, Tuple, Optional\nimport heapq\n\n\nclass Dijkstra:\n\
    \    def __init__(self, N: int, E: List[List[Tuple[int, int]]],\n            \
    \     start: int = 0, inf: int = 1 << 50):\n        self.N = N\n        self.E\
    \ = E\n        self.start = start\n        self.inf = inf\n\n        self.C =\
    \ [self.inf] * N\n        self.prev = [None] * N\n        self._calculate()\n\n\
    \    def get_cost(self, i: int) -> int:\n        \"\"\"return cost to i-th vertex.\
    \ return inf if the vertex is unreachable.\"\"\"\n        return self.C[i]\n\n\
    \    def get_path(self, i) -> Optional[List[int]]:\n        \"\"\"return shortest\
    \ path to i-th vertex if reachable otherwise None\"\"\"\n        if not self.reachable(i):\n\
    \            return None\n\n        p = []\n        cur = i\n        while cur\
    \ is not None:\n            p.append(cur)\n            cur = self.prev[cur]\n\
    \        p.reverse()\n        return p\n\n    def reachable(self, i) -> bool:\n\
    \        \"\"\"return whether i-th vertex is reachable from start\"\"\"\n    \
    \    return self.C[i] < self.inf\n\n    def _calculate(self) -> None:\n      \
    \  h = [(0, self.start)]\n        self.C[self.start] = 0\n        visited = [False]\
    \ * self.N\n\n        while h:\n            _, v = heapq.heappop(h)\n        \
    \    if visited[v]:\n                continue\n            visited[v] = True\n\
    \n            for c, d in self.E[v]:\n                if self.C[d] > self.C[v]\
    \ + c:\n                    self.C[d] = self.C[v] + c\n                    self.prev[d]\
    \ = v\n                    heapq.heappush(h, (self.C[d], d))\n"
  dependsOn: []
  isVerificationFile: false
  path: library/dijkstra.py
  requiredBy: []
  timestamp: '2022-12-08 23:20:27+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/yosupo/shortest_path.test.py
documentation_of: library/dijkstra.py
layout: document
redirect_from:
- /library/library/dijkstra.py
- /library/library/dijkstra.py.html
title: library/dijkstra.py
---
