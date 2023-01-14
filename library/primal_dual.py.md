---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/grl_6_b.test.py
    title: tests/aoj/grl_6_b.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Tuple\nimport heapq\n\n\nclass PrimalDual:\n    def __init__(self,\
    \ N: int, inf: int = 1 << 50):\n        self.N = N\n        self.G = [[] for _\
    \ in range(N)]\n        self.inf = inf\n\n    def add_edge(self, u: int, v: int,\
    \ cap: int, cost: int) -> None:\n        assert cap >= 0 and cost >= 0\n     \
    \   forward = [cap, v, cost, None]\n        backward = [0, u, -cost, None]\n \
    \       forward[3] = backward\n        backward[3] = forward\n        self.G[u].append(forward)\n\
    \        self.G[v].append(backward)\n\n    def flow(self, s: int, t: int, f: int)\
    \ -> Tuple[int, int]:\n        retf = 0\n        retc = 0\n        H = [0] * self.N\n\
    \        prev = [None] * self.N\n\n        while f:\n            C = [self.inf]\
    \ * self.N\n            visited = [False] * self.N\n            C[s] = 0\n   \
    \         h = [(0, s)]\n\n            while h:\n                _, v = heapq.heappop(h)\n\
    \                if visited[v]:\n                    continue\n              \
    \  visited[v] = True\n\n                for e in self.G[v]:\n                \
    \    cap, d, cost, _ = e\n                    if cap <= 0:\n                 \
    \       continue\n                    nc = C[v] + cost + H[v] - H[d]\n       \
    \             if C[d] > nc:\n                        C[d] = nc\n             \
    \           prev[d] = (v, e)\n                        heapq.heappush(h, (C[d],\
    \ d))\n\n            if not visited[t]:\n                return retf, retc\n\n\
    \            for i in range(self.N):\n                H[i] += C[i]\n\n       \
    \     min_cap = f\n            cur = t\n            while cur != s:\n        \
    \        pv, pe = prev[cur]\n                min_cap = min(min_cap, pe[0])\n \
    \               cur = pv\n            f -= min_cap\n            retf += min_cap\n\
    \            retc += min_cap * H[t]\n\n            cur = t\n            while\
    \ cur != s:\n                pv, pe = prev[cur]\n                pe[0] -= min_cap\n\
    \                pe[3][0] += min_cap\n                cur = pv\n        return\
    \ retf, retc\n\n    def edges(self):\n        E = []\n        for i in range(self.N):\n\
    \            for cap, j, _, _ in solver.G[i]:\n                E.append((i, j,\
    \ cap))\n        return E\n"
  dependsOn: []
  isVerificationFile: false
  path: library/primal_dual.py
  requiredBy: []
  timestamp: '2023-01-14 22:09:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/grl_6_b.test.py
documentation_of: library/primal_dual.py
layout: document
redirect_from:
- /library/library/primal_dual.py
- /library/library/primal_dual.py.html
title: library/primal_dual.py
---
