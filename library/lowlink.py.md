---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/grl_3_a.test.py
    title: tests/aoj/grl_3_a.test.py
  - icon: ':heavy_check_mark:'
    path: tests/aoj/grl_3_b.test.py
    title: tests/aoj/grl_3_b.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://codeforces.com/blog/entry/68138
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Lowlink:\n    # cf: https://codeforces.com/blog/entry/68138\n    def\
    \ __init__(self, N, E):\n        self.N = N\n        self.E = E\n        # span-edge\
    \ and back-edge (directed)\n        self.span = [[] for _ in range(self.N)]\n\
    \        self.back = [[] for _ in range(self.N)]\n\n        self.ord = [None]\
    \ * self.N\n        self.low = [None] * self.N\n        self.par = [None] * self.N\n\
    \n        self._build()\n\n    def _build(self):\n        visited = [False] *\
    \ self.N\n        cnt = 0\n        for i in range(self.N):\n            if visited[i]:\n\
    \                continue\n            stack = [(i, -1)]\n            while stack:\n\
    \                v, p = stack.pop()\n\n                if v < 0:\n           \
    \         v = ~v\n                    for d in self.span[v]:\n               \
    \         if d == p:\n                            continue\n                 \
    \       self.low[v] = min(self.low[v], self.low[d])\n                    continue\n\
    \n                if visited[v]:\n                    continue\n             \
    \   visited[v] = True\n                self.ord[v] = cnt\n                self.low[v]\
    \ = cnt\n                cnt += 1\n                # p -> v is span-edge.\n  \
    \              self.par[v] = p\n                if p >= 0:\n                 \
    \   self.span[p].append(v)\n                stack.append((~v, p))\n\n        \
    \        for d in self.E[v][::-1]:\n                    if d == p:\n         \
    \               continue\n                    if visited[d]:\n               \
    \         # v -> d is back-edge since v is already visited.\n                \
    \        self.back[v].append(d)\n                        self.low[v] = min(self.low[v],\
    \ self.ord[d])\n                        continue\n                    stack.append((d,\
    \ v))\n\n    def bridges(self):\n        \"\"\"return list of edges that are bridges\"\
    \"\"\n        bridges = []\n        for u in range(self.N):\n            for v\
    \ in self.span[u]:\n                # vertex u has child v that does not have\
    \ lowlink to pass over its parent\n                if self.ord[u] < self.low[v]:\n\
    \                    bridges.append((u, v))\n        return bridges\n\n    def\
    \ articulation_points(self):\n        \"\"\"return list of vertices that are articulation\
    \ points\"\"\"\n        points = []\n        for u in range(self.N):\n       \
    \     if self.par[u] < 0:\n                if len(self.span[u]) >= 2:\n      \
    \              points.append(u)\n                continue\n            for v in\
    \ self.span[u]:\n                if self.ord[u] <= self.low[v]:\n            \
    \        points.append(u)\n                    break\n        return points\n"
  dependsOn: []
  isVerificationFile: false
  path: library/lowlink.py
  requiredBy: []
  timestamp: '2022-12-14 18:34:44+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/grl_3_a.test.py
  - tests/aoj/grl_3_b.test.py
documentation_of: library/lowlink.py
layout: document
redirect_from:
- /library/library/lowlink.py
- /library/library/lowlink.py.html
title: library/lowlink.py
---
