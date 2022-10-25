---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/grl_6_a.test.py
    title: tests/aoj/grl_6_a.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\n\n\nclass Dinic:\n    def __init__(self, N,\
    \ inf=1 << 50):\n        self.N = N\n        self.G = [[] for _ in range(self.N)]\n\
    \        self.inf = inf\n\n    def add_edge(self, u, v, cap):\n        forward\
    \ = [cap, v, None]\n        backward = [0, u, None]\n        forward[2] = backward\n\
    \        backward[2] = forward\n        self.G[u].append(forward)\n        self.G[v].append(backward)\n\
    \n    def flow(self, s, t):\n        flow = 0\n        while True:\n         \
    \   self._bfs(s, t)\n            if self.level[t] is None:\n                return\
    \ flow\n            *self.iter, = map(iter, self.G)\n            f = self.inf\n\
    \            while f > 0:\n                f = self._dfs(s, t, self.inf)\n   \
    \             flow += f\n\n    def _bfs(self, s, t):\n        self.level = [None]\
    \ * self.N\n        dq = deque([s])\n        self.level[s] = 0\n        while\
    \ dq:\n            v = dq.popleft()\n            for cap, d, _ in self.G[v]:\n\
    \                if cap == 0:\n                    continue\n                if\
    \ self.level[d] is None:\n                    self.level[d] = self.level[v] +\
    \ 1\n                    dq.append(d)\n\n    def _dfs(self, u, t, f):\n      \
    \  if u == t:\n            return f\n        for e in self.iter[u]:\n        \
    \    cap, v, rev = e\n            if cap == 0:\n                continue\n   \
    \         if self.level[v] > self.level[u]:\n                delta = self._dfs(v,\
    \ t, min(f, cap))\n                if delta > 0:\n                    e[0] -=\
    \ delta\n                    rev[0] += delta\n                    return delta\n\
    \        return 0\n"
  dependsOn: []
  isVerificationFile: false
  path: library/dinic.py
  requiredBy: []
  timestamp: '2022-10-25 20:08:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/grl_6_a.test.py
documentation_of: library/dinic.py
layout: document
redirect_from:
- /library/library/dinic.py
- /library/library/dinic.py.html
title: library/dinic.py
---
