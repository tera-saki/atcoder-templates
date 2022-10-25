---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/tree_diameter.test.py
    title: tests/yosupo/tree_diameter.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class TreeDiameter:\n    def __init__(self, N, E, inf=1 << 50):\n       \
    \ self.N = N\n        self.E = E\n        self.inf = inf\n\n        self.prev\
    \ = [None] * N\n\n        u, c0 = self._dfs1(0)\n        v, cu = self._dfs2(u)\n\
    \        self.diameter = (u, v)\n        self.diameter_weight = cu[v]\n\n    def\
    \ get_path(self):\n        _, v = self.diameter\n        cur = v\n        p =\
    \ []\n        while cur >= 0:\n            p.append(cur)\n            cur = self.prev[cur]\n\
    \        return p\n\n    def _dfs1(self, s):\n        cost = [self.inf] * self.N\n\
    \        cost[s] = 0\n        stack = [s]\n        farthest = s\n        while\
    \ stack:\n            v = stack.pop()\n            if cost[v] > cost[farthest]:\n\
    \                farthest = v\n            for c, d in self.E[v]:\n          \
    \      if cost[d] > cost[v] + c:\n                    cost[d] = cost[v] + c\n\
    \                    stack.append(d)\n        return farthest, cost\n\n    def\
    \ _dfs2(self, s):\n        cost = [self.inf] * self.N\n        cost[s] = 0\n \
    \       stack = [(s, -1)]\n        farthest = s\n        while stack:\n      \
    \      v, p = stack.pop()\n            self.prev[v] = p\n            if cost[v]\
    \ > cost[farthest]:\n                farthest = v\n            for c, d in self.E[v]:\n\
    \                if cost[d] > cost[v] + c:\n                    cost[d] = cost[v]\
    \ + c\n                    stack.append((d, v))\n        return farthest, cost\n"
  dependsOn: []
  isVerificationFile: false
  path: library/tree_diameter.py
  requiredBy: []
  timestamp: '2022-10-25 20:08:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/yosupo/tree_diameter.test.py
documentation_of: library/tree_diameter.py
layout: document
redirect_from:
- /library/library/tree_diameter.py
- /library/library/tree_diameter.py.html
title: library/tree_diameter.py
---
