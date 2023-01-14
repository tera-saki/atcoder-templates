---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/2667.test.py
    title: tests/aoj/2667.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/lca-hld.test.py
    title: tests/yosupo/lca-hld.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/vertex_add_path_sum.test.py
    title: tests/yosupo/vertex_add_path_sum.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/vertex_add_subtree_sum.test.py
    title: tests/yosupo/vertex_add_subtree_sum.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://codeforces.com/blog/entry/53170
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, Tuple\n\n\nclass HLD:\n    # reference: https://codeforces.com/blog/entry/53170\n\
    \    def __init__(self, N, E, root: int = 0):\n        self.N = N\n        self.E\
    \ = E\n        self.root = root\n\n        self.D = [0] * self.N\n        self.par\
    \ = [-1] * self.N\n        self.sz = [0] * self.N\n        self.top = [0] * self.N\n\
    \n        self.ord = [None] * self.N\n\n        self._dfs_sz()\n        self._dfs_hld()\n\
    \n    def path_query_range(self, u: int, v: int, is_edge_query: bool = False)\
    \ -> List[Tuple[int, int]]:\n        \"\"\"return list of [l, r) ranges that cover\
    \ u-v path\"\"\"\n        ret = []\n        while True:\n            if self.ord[u]\
    \ > self.ord[v]:\n                u, v = v, u\n            if self.top[u] == self.top[v]:\n\
    \                ret.append((self.ord[u] + is_edge_query, self.ord[v] + 1))\n\
    \                return ret\n            ret.append((self.ord[self.top[v]], self.ord[v]\
    \ + 1))\n            v = self.par[self.top[v]]\n\n    def subtree_query_range(self,\
    \ v: int, is_edge_query: bool = False) -> Tuple[int, int]:\n        \"\"\"return\
    \ [l, r) range that cover vertices of subtree v\"\"\"\n        return (self.ord[v]\
    \ + is_edge_query, self.ord[v] + self.sz[v])\n\n    def get_index(self, v: int)\
    \ -> int:\n        \"\"\"return euler tour order of given vertex\"\"\"\n     \
    \   return self.ord[v]\n\n    def lca(self, u, v):\n        while True:\n    \
    \        if self.ord[u] > self.ord[v]:\n                u, v = v, u\n        \
    \    if self.top[u] == self.top[v]:\n                return u\n            v =\
    \ self.par[self.top[v]]\n\n    def dist(self, u, v):\n        return self.D[u]\
    \ + self.D[v] - 2 * self.D[self.lca(u, v)]\n\n    def _dfs_sz(self):\n       \
    \ stack = [(self.root, -1)]\n        while stack:\n            v, p = stack.pop()\n\
    \            if v < 0:\n                v = ~v\n                self.sz[v] = 1\n\
    \                for i, dst in enumerate(self.E[v]):\n                    if dst\
    \ == p:\n                        continue\n                    self.sz[v] += self.sz[dst]\n\
    \                    # v -> E[v][0] will be heavy path\n                    if\
    \ self.sz[self.E[v][0]] < self.sz[dst]:\n                        self.E[v][0],\
    \ self.E[v][i] = self.E[v][i], self.E[v][0]\n            else:\n             \
    \   if ~p:\n                    self.D[v] = self.D[p] + 1\n                  \
    \  self.par[v] = p\n                # avoid first element of E[v] is parent of\
    \ vertex v if v has some children\n                if len(self.E[v]) >= 2 and\
    \ self.E[v][0] == p:\n                    self.E[v][0], self.E[v][1] = self.E[v][1],\
    \ self.E[v][0]\n                stack.append((~v, p))\n                for dst\
    \ in self.E[v]:\n                    if dst == p:\n                        continue\n\
    \                    stack.append((dst, v))\n\n    def _dfs_hld(self):\n     \
    \   stack = [(self.root, -1)]\n        cnt = 0\n        while stack:\n       \
    \     v, p = stack.pop()\n            self.ord[v] = cnt\n            cnt += 1\n\
    \            heavy_path_idx = len(self.E[v]) - 1\n            for i, dst in enumerate(self.E[v][::-1]):\n\
    \                if dst == p:\n                    continue\n                #\
    \ top[dst] is top[v] if v -> dst is heavy path otherwise dst itself\n        \
    \        self.top[dst] = self.top[v] if i == heavy_path_idx else dst\n       \
    \         stack.append((dst, v))\n"
  dependsOn: []
  isVerificationFile: false
  path: library/hld.py
  requiredBy: []
  timestamp: '2023-01-14 22:09:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/2667.test.py
  - tests/yosupo/vertex_add_path_sum.test.py
  - tests/yosupo/lca-hld.test.py
  - tests/yosupo/vertex_add_subtree_sum.test.py
documentation_of: library/hld.py
layout: document
redirect_from:
- /library/library/hld.py
- /library/library/hld.py.html
title: library/hld.py
---
