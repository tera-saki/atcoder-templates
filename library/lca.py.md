---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/lca.test.py
    title: tests/lca.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\n\ninput = sys.stdin.readline\nsys.setrecursionlimit(10 ** 6)\n\
    \n\nclass LCA:\n    def __init__(self, N, E, root=0):\n        self.N = N\n  \
    \      self.E = E\n        self.K = N.bit_length()\n        self.par = [[-1 for\
    \ _ in range(N)] for _ in range(self.K)]\n        self.depth = [None] * N\n\n\
    \        self.dfs(root, 0, -1)\n        for k in range(self.K - 1):\n        \
    \    for i in range(self.N):\n                if self.par[k][i] < 0:\n       \
    \             continue\n                self.par[k + 1][i] = self.par[k][self.par[k][i]]\n\
    \n    def dfs(self, v, d, p):\n        self.par[0][v] = p\n        self.depth[v]\
    \ = d\n        for dest in self.E[v]:\n            if dest == p:\n           \
    \     continue\n            self.dfs(dest, d + 1, v)\n\n    def lca(self, u, v):\n\
    \        if self.depth[u] > self.depth[v]:\n            u, v = v, u\n        d\
    \ = self.depth[v] - self.depth[u]\n        for k in range(self.K):\n         \
    \   if d & (1 << k):\n                v = self.par[k][v]\n\n        if u == v:\n\
    \            return u\n        for k in range(self.K)[::-1]:\n            if self.par[k][u]\
    \ != self.par[k][v]:\n                u = self.par[k][u]\n                v =\
    \ self.par[k][v]\n        return self.par[0][v]\n\n    def dist(self, u, v):\n\
    \        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]"
  dependsOn: []
  isVerificationFile: false
  path: library/lca.py
  requiredBy: []
  timestamp: '2022-09-25 18:32:29+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/lca.test.py
documentation_of: library/lca.py
layout: document
redirect_from:
- /library/library/lca.py
- /library/library/lca.py.html
title: library/lca.py
---
